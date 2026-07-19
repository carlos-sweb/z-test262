# Z-Test262

Runner de la suite oficial [Test262](https://github.com/tc39/test262) de TC39 contra el motor [z-*](https://github.com/carlos-sweb) (via el binario `z-run`). Deliverable del item 16 del roadmap: la métrica objetiva de conformance y el reporte de divergencias que guía la Etapa D.

- `runner.py` — sin dependencias: parsea el frontmatter YAML por regex (negative/flags/features/includes), compone harness+test, un proceso `z-run` fresco por test bajo `timeout`, clasifica PASS/FAIL/CRASH/TIMEOUT/SKIP (los `noStrict` se skipean: el motor es always-strict por diseño), emite JSONL en paralelo.
- `report.py` — agrega el JSONL a `REPORT.md`: pass-rate por área, causas raíz agrupadas por forma del mensaje, features en fails, crashes.
- `REPORT.md` — el baseline actual con el análisis de divergencias.

La suite se clona aparte (`git clone --depth 1 https://github.com/tc39/test262 ~/test262`) y NO vive en este repo.

```bash
python3 runner.py --suite ~/test262 --zrun ~/z-run/zig-out/bin/z-run \
  --jobs 8 --out results.jsonl test/language
python3 report.py results.jsonl > REPORT.md
```
