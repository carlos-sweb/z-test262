#!/usr/bin/env python3
"""Test262 runner for the z-* engine (z-run binary).

No dependencies: the YAML frontmatter is parsed with regexes for the
fields that matter (negative, flags, features, includes). One fresh
z-run process per test, under timeout. Emits JSONL; report.py aggregates.
"""
import argparse, json, os, re, subprocess, sys, tempfile
from multiprocessing import Pool

FRONTMATTER = re.compile(r"/\*---(.*?)---\*/", re.S)

def parse_meta(src):
    m = FRONTMATTER.search(src)
    meta = {"flags": [], "features": [], "includes": [], "negative": None}
    if not m:
        return meta
    y = m.group(1)
    fm = re.search(r"^\s*flags:\s*\[(.*?)\]", y, re.M)
    if fm:
        meta["flags"] = [f.strip() for f in fm.group(1).split(",") if f.strip()]
    ft = re.search(r"^\s*features:\s*\[(.*?)\]", y, re.M)
    if ft:
        meta["features"] = [f.strip() for f in ft.group(1).split(",") if f.strip()]
    inc = re.search(r"^\s*includes:\s*\[(.*?)\]", y, re.M)
    if inc:
        meta["includes"] = [f.strip() for f in inc.group(1).split(",") if f.strip()]
    else:
        inc2 = re.search(r"^\s*includes:\s*\n((?:\s*-\s*\S+\n?)+)", y, re.M)
        if inc2:
            meta["includes"] = re.findall(r"-\s*(\S+)", inc2.group(1))
    neg = re.search(r"^\s*negative:", y, re.M)
    if neg:
        phase = re.search(r"phase:\s*(\S+)", y)
        typ = re.search(r"type:\s*(\S+)", y)
        meta["negative"] = {
            "phase": phase.group(1) if phase else "",
            "type": typ.group(1) if typ else "",
        }
    return meta

def run_one(job):
    path, suite, zrun, timeout_s = job
    rel = os.path.relpath(path, suite)
    try:
        src = open(path, encoding="utf-8").read()
    except Exception as e:
        return {"path": rel, "result": "ERROR", "reason": f"read: {e}", "features": []}
    meta = parse_meta(src)
    flags = meta["flags"]

    if "noStrict" in flags:
        # sloppy-only semantics: the engine is always-strict BY DESIGN
        return {"path": rel, "result": "SKIP", "reason": "noStrict (always-strict by design)", "features": meta["features"]}
    if "CanBlockIsFalse" in flags:
        return {"path": rel, "result": "SKIP", "reason": "agent flag", "features": meta["features"]}

    harness_dir = os.path.join(suite, "harness")
    parts = []
    if "raw" not in flags:
        for h in ["sta.js", "assert.js"] + meta["includes"] + (["doneprintHandle.js"] if "async" in flags else []):
            try:
                parts.append(open(os.path.join(harness_dir, h), encoding="utf-8").read())
            except FileNotFoundError:
                return {"path": rel, "result": "SKIP", "reason": f"missing harness include {h}", "features": meta["features"]}
    parts.append(src)
    composed = "\n".join(parts)

    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as tf:
        tf.write(composed)
        tmp = tf.name
    try:
        proc = subprocess.run([zrun, tmp], capture_output=True, text=True, timeout=timeout_s)
        exit_code = proc.returncode
        out, err = proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        os.unlink(tmp)
        return {"path": rel, "result": "TIMEOUT", "reason": "", "features": meta["features"]}
    finally:
        try: os.unlink(tmp)
        except FileNotFoundError: pass

    if exit_code < 0 or exit_code > 1:
        return {"path": rel, "result": "CRASH", "reason": f"exit {exit_code}: {err.strip()[:160]}", "features": meta["features"]}

    if meta["negative"]:
        if exit_code != 0:
            return {"path": rel, "result": "PASS", "reason": "negative", "features": meta["features"]}
        return {"path": rel, "result": "FAIL", "reason": f"expected {meta['negative']['type']} ({meta['negative']['phase']}), got success", "features": meta["features"]}

    if "async" in flags:
        if "Test262:AsyncTestComplete" in out:
            return {"path": rel, "result": "PASS", "reason": "", "features": meta["features"]}
        return {"path": rel, "result": "FAIL", "reason": f"async incomplete: {err.strip()[:160] or out.strip()[:160]}", "features": meta["features"]}

    if exit_code == 0:
        return {"path": rel, "result": "PASS", "reason": "", "features": meta["features"]}
    return {"path": rel, "result": "FAIL", "reason": err.strip()[:200], "features": meta["features"]}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", default="/home/sweb/test262")
    ap.add_argument("--zrun", default="/home/sweb/z-run/zig-out/bin/z-run")
    ap.add_argument("--out", default="results.jsonl")
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--timeout", type=float, default=5.0)
    ap.add_argument("dirs", nargs="+", help="test dirs relative to the suite, e.g. test/language")
    args = ap.parse_args()

    files = []
    for d in args.dirs:
        for root, _, names in os.walk(os.path.join(args.suite, d)):
            for n in sorted(names):
                if n.endswith(".js") and not n.endswith("_FIXTURE.js"):
                    files.append(os.path.join(root, n))
    print(f"{len(files)} tests", file=sys.stderr)

    jobs = [(f, args.suite, args.zrun, args.timeout) for f in files]
    done = 0
    with open(args.out, "w", encoding="utf-8") as out, Pool(args.jobs) as pool:
        for res in pool.imap_unordered(run_one, jobs, chunksize=32):
            out.write(json.dumps(res) + "\n")
            done += 1
            if done % 2000 == 0:
                print(f"{done}/{len(files)}", file=sys.stderr)
    print("done", file=sys.stderr)

if __name__ == "__main__":
    main()
