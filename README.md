# Z-Test262

Runner for the official [Test262](https://github.com/tc39/test262) TC39 suite against the [z-*](https://github.com/carlos-sweb) engine (via the `z-run` binary). Deliverable of roadmap item 16: the objective conformance metric and the divergence report that guides Stage D.

- `runner.py` — no dependencies: parses the YAML frontmatter via regex (negative/flags/features/includes), composes harness+test, one fresh `z-run` process per test under `timeout`, classifies PASS/FAIL/CRASH/TIMEOUT/SKIP (`noStrict` tests are skipped: the engine is always-strict by design), emits JSONL in parallel.
- `report.py` — aggregates the JSONL into `REPORT.md`: pass rate by area, root causes grouped by message shape, features in fails, crashes.
- `REPORT.md` — the current baseline with the divergence analysis.
- `compare.py` — checks identical, duplicate-free coverage and compares outcomes
  per test; accepts plain JSONL or gzip archives.
- `recheck.py` — reruns historical PASS losses and current crashes serially using
  the unchanged runner, with a longer timeout.
- `REGRESSIONS.md` — the measured outcome changes and individual rechecks.
- `runs/2026-10-14-zig017/` — compressed baseline/current/recheck records,
  binary and suite metadata, detailed comparison, and crash diagnostics.

The additional diagnostic helpers (`compare.py`, `recheck.py`,
`REGRESSIONS.md` and `runs/`) described here are preserved local artifacts,
not included in this report-only publication. The committed runner and
report generator remain `runner.py` and `report.py`.

The suite is cloned separately (`git clone --depth 1 https://github.com/tc39/test262 ~/test262`) and does NOT live in this repo.

Use the capped ReleaseFast recipe below for measurements comparable to the
historical baseline; a default Debug binary or an uncapped sweep changes results.

## Current measurement: z-interpreter v0.2.0 / Zig 0.17.0

The **2026-10-14** ReleaseFast sweep uses **z-interpreter v0.2.0**
(commit `8d922fb46112e77215d33a197f7f9a0333000996`) and **z-regex v0.9.1**.
Test262 checkout: `9e61c12835c5e4a3bdba93850427e6742c4f64c4`.
Scope: `test/language test/built-ins`, 8 workers, 5-second timeout and a
2 GiB per-process address-space cap. The runner is unchanged and has no
separately selectable UTF-16/WTF-8 modes.

| Result | Count |
|---|---:|
| PASS | 31,726 |
| FAIL | 13,803 |
| CRASH | 2 |
| TIMEOUT | 108 |
| SKIP | 1,742 |
| Total | 47,381 |
| Executed | 45,639 |

Pass rate: **69.5% of executed tests**. The previous committed REPORT.md
had **29,615 PASS**; the immediately preceding local v0.1.0 sweep had
**29,856 PASS**. The table preserves the raw sweep; serial rechecks do not
replace its TIMEOUT records.

Compared with the local v0.1.0 sweep, one PASS loss reproduced:
`test/built-ins/RegExp/named-groups/lookbehind.js`. v0.2.0 now correctly
forwards `u`; z-regex v0.9.1 does not support backward lookbehind with
captures under `u`, and the interpreter reports SyntaxError. The pattern
`/(?<=(?<a>\w){3})f/u` passed previously because `u` was ignored.

Four PASS-to-TIMEOUT cases passed alone, as did all 99 new FAIL-to-TIMEOUT
cases: **103/108 timeouts recovered** with a 60-second serial budget.
The two generator reentry crashes also reproduced with the old binary;
they are not shown to have been introduced by v0.2.0.

Input: `/tmp/zrun-v020-test262-20261014/results.jsonl`.
The local analysis, transitions and rechecks remain in that directory.
Regenerate the committed report with:

```sh
python3 report.py /tmp/zrun-v020-test262-20261014/results.jsonl > REPORT.md
```

## Historical measurement: z-interpreter v0.1.0 / Zig 0.17.0

The 2026-10-14 ReleaseFast sweep covered the same **47,381 unique test paths** as
the September baseline: **29,856 PASS / 45,639 executed (65.42%)**, 15,766 FAIL,
6 CRASH, 11 TIMEOUT, and 1,742 SKIP. This is a **historical compatibility metric**,
not a percentage of all ECMA-262 requirements.

The net increase of 241 PASS hides **414 reproducible PASS losses**: 409 FAIL
and 5 CRASH. All losses were repeated individually with a 60-second timeout;
none recovered to PASS. See the local `REGRESSIONS.md`. The sixth sweep
crash was previously a FAIL and returned FAIL in the serial ReleaseFast recheck;
Debug still crashes on that case. The old executable was unavailable for a
same-day A/B, so these outcomes identify regressions against the stored results
without assigning their introduction to a particular compiler or source commit.

## Reproducible historical sweep

Use an isolated binary prefix and a **2 GiB per-process address-space limit**.
Claude's earlier sessions recorded machine-wide OOMs when this limit was omitted;
a smaller limit also changes legitimate sparse-array results.

```sh
cd ~/z-run
zig build install -Doptimize=ReleaseFast --prefix /tmp/zrun-conformance
printf '%s\n' '#!/bin/bash' 'ulimit -v 2097152' \
  'exec /tmp/zrun-conformance/bin/z-run "$@"' > /tmp/zrun-capped.sh
chmod +x /tmp/zrun-capped.sh

cd ~/z-test262
python3 runner.py --suite ~/test262 --zrun /tmp/zrun-capped.sh \
  --jobs 8 --timeout 5 --out results_NEW.jsonl test/language test/built-ins
python3 recheck.py runs/2026-10-14-zig017/results.jsonl.gz results_NEW.jsonl \
  --suite ~/test262 --zrun /tmp/zrun-capped.sh --timeout 60 --out rechecks_NEW.jsonl
python3 compare.py runs/2026-10-14-zig017/results.jsonl.gz results_NEW.jsonl \
  --rechecks rechecks_NEW.jsonl --json comparison_NEW.json > REGRESSIONS_NEW.md
python3 report.py results_NEW.jsonl > REPORT_NEW.md
```

Never use bare `test` for a historical sweep: that adds Intl, staging, Annex B,
and harness folders not present in the baseline. Record the suite commit, binary
SHA-256, build mode, timeout, process cap, worker count, and selected directories.
Do not overwrite a previous raw sweep. A rise in total PASS does not establish
absence of regressions; compare individual paths and rerun losses in isolation.

Reproduce the stored comparison without running the engine:

```sh
python3 compare.py runs/2026-10-14-zig017/baseline.jsonl.gz \
  runs/2026-10-14-zig017/results.jsonl.gz \
  --rechecks runs/2026-10-14-zig017/rechecks.jsonl.gz
python3 -m unittest test_compare.py
```

`compare.py --fail-on-regression` returns exit 1 for reproduced or unresolved
PASS losses; malformed/incomparable input returns exit 2.

## Harness limitations

The original runner is deliberately unchanged for this comparison. A conforming
host must implement the [Test262 interpretation rules](https://github.com/tc39/test262/blob/9e61c12835c5e4a3bdba93850427e6742c4f64c4/INTERPRETING.md).
This historical runner has important limitations:

- `z-run file.js` executes all composed tests as modules, including tests that
  require global Script semantics. Temporary files also break relative module
  fixture resolution.
- The always-strict engine skips `noStrict` and does not run both strict and
  non-strict scenarios for unflagged tests.
- Any ordinary nonzero exit passes a negative test; expected error type and phase
  are not verified. **4,592 of this sweep's PASS records are negative tests** and
  therefore require separate validation before claiming conformance.
- Metadata parsing is not complete YAML parsing; the full `$262` host API
  (realms, buffer detachment, agents) is not implemented.
- Async completion uses output markers and does not validate every exit/failure
  combination required by Test262.

Correcting the harness must establish a new, separately versioned baseline;
mixing changed harness semantics into this comparison would hide their effect.
The engine/dependency gaps and the host/measurement gaps are distinct work items.
