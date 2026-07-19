#!/usr/bin/env python3
"""Aggregates runner.py's JSONL into REPORT.md: pass rates by area, top
failure causes (grouped by error message shape), feature breakdown."""
import json, re, sys, collections

def area_of(path):
    parts = path.split("/")
    if parts[1] == "language":
        return "/".join(parts[:3])
    return "/".join(parts[:3])  # built-ins/<Name>

def norm_reason(reason):
    r = reason
    r = re.sub(r"'[^']*'", "'…'", r)
    r = re.sub(r"\d+", "N", r)
    return r[:110]

rows = [json.loads(l) for l in open(sys.argv[1] if len(sys.argv) > 1 else "results.jsonl")]
total = len(rows)
by_result = collections.Counter(r["result"] for r in rows)
ran = total - by_result["SKIP"]
passed = by_result["PASS"]

areas = collections.defaultdict(lambda: collections.Counter())
for r in rows:
    areas[area_of(r["path"])][r["result"]] += 1

fail_reasons = collections.Counter()
crash_reasons = collections.Counter()
fail_features = collections.Counter()
examples = {}
for r in rows:
    if r["result"] == "FAIL":
        k = norm_reason(r["reason"])
        fail_reasons[k] += 1
        examples.setdefault(k, r["path"])
        for f in r["features"]:
            fail_features[f] += 1
    elif r["result"] == "CRASH":
        k = norm_reason(r["reason"])
        crash_reasons[k] += 1
        examples.setdefault(k, r["path"])

out = []
out.append("# Test262 — reporte de divergencias del motor z-*\n")
out.append(f"Total: {total} tests | corridos: {ran} | **PASS: {passed} ({100.0*passed/ran:.1f}% de los corridos)** | "
           f"FAIL: {by_result['FAIL']} | CRASH: {by_result['CRASH']} | TIMEOUT: {by_result['TIMEOUT']} | SKIP (by design): {by_result['SKIP']}\n")

out.append("\n## Pass-rate por área\n")
out.append("| área | pass | fail | crash | timeout | skip | % pass |")
out.append("|---|---|---|---|---|---|---|")
for area in sorted(areas):
    c = areas[area]
    a_ran = sum(c.values()) - c["SKIP"]
    pct = 100.0 * c["PASS"] / a_ran if a_ran else 0
    out.append(f"| {area} | {c['PASS']} | {c['FAIL']} | {c['CRASH']} | {c['TIMEOUT']} | {c['SKIP']} | {pct:.1f}% |")

out.append("\n## Top causas de FAIL (mensaje normalizado)\n")
for reason, n in fail_reasons.most_common(30):
    out.append(f"- **{n}x** `{reason or '(sin mensaje)'}`\n  - ej: `{examples.get(reason, '')}`")

out.append("\n## Top features presentes en FAILs\n")
for feat, n in fail_features.most_common(25):
    out.append(f"- {n}x {feat}")

if crash_reasons:
    out.append("\n## CRASHES (los más graves)\n")
    for reason, n in crash_reasons.most_common(20):
        out.append(f"- **{n}x** `{reason}`\n  - ej: `{examples.get(reason, '')}`")

print("\n".join(out))
