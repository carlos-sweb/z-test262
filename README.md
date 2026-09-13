# Z-Test262

Runner for the official [Test262](https://github.com/tc39/test262) TC39 suite against the [z-*](https://github.com/carlos-sweb) engine (via the `z-run` binary). Deliverable of roadmap item 16: the objective conformance metric and the divergence report that guides Stage D.

- `runner.py` — no dependencies: parses the YAML frontmatter via regex (negative/flags/features/includes), composes harness+test, one fresh `z-run` process per test under `timeout`, classifies PASS/FAIL/CRASH/TIMEOUT/SKIP (`noStrict` tests are skipped: the engine is always-strict by design), emits JSONL in parallel.
- `report.py` — aggregates the JSONL into `REPORT.md`: pass rate by area, root causes grouped by message shape, features in fails, crashes.
- `REPORT.md` — the current baseline with the divergence analysis.

The suite is cloned separately (`git clone --depth 1 https://github.com/tc39/test262 ~/test262`) and does NOT live in this repo.

```bash
python3 runner.py --suite ~/test262 --zrun ~/z-run/zig-out/bin/z-run \
  --jobs 8 --out results.jsonl test/language
python3 report.py results.jsonl > REPORT.md
```
