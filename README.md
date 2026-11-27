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

## Current measurement: z-interpreter@c7bb14b (v0.4.19 + Parser Capa 1/2 + Fases 7–8 + JIT J2.5–J3 + Spec Quickwins 1–3 + Temporal 100%) / Zig 0.17.0

The **2026-11-26** ReleaseFast sweep uses **z-interpreter** (`c7bb14b`), **z-run** (`a1725e0`), and package cascade: **z-parser v0.1.2**, **z-statements v0.2.2**, **z-functions v0.2.2**, **z-array v0.2.1**, **z-object v0.2.1**, **z-buffer v0.1.2**, **z-value v0.1.5**, **z-json v0.1.5**, **z-yaml v0.2.4**, **z-toml v0.2.4**, **z-temporal v0.2.9** (`913675a`), and **z-regex v0.9.1**.
Test262 checkout: `9e61c12835c5e4a3bdba93850427e6742c4f64c4`.
Scope: `test/language test/built-ins`, 4 workers, 5-second timeout and a
2 GiB per-process address-space cap. The runner is unchanged and has no
separately selectable UTF-16/WTF-8 modes.

| Result | Count |
|---|---:|
| PASS | 42,975 |
| FAIL | 2,664 |
| CRASH | 0 |
| TIMEOUT | 0 |
| SKIP | 1,742 |
| Total | 47,381 |
| Executed | 45,639 |

Pass rate: **94.16% of executed tests** (42,975 / 45,639; up +155 PASS from `f684bf7` / +934 PASS from `v0.4.19`, 0 regressions). Key consolidation milestones across this progression:
- **Bytecode VM**: JSValue 16B execution loop (fib 1.02s vs tree-walker 6.3s).
- **Temporal 100.0%**: 4,602 PASS / 1 FAIL in `test/built-ins/Temporal/` (4,610 / 4,611 including the 8 `Date.prototype.toTemporalInstant` tests; zero regressions).
- **Object & Array conformance**: E3/E4 conformance consolidated with zero generic array regressions.
- **18 E3/E4 gaps resolved**: TypedArray exotic numeric index traps, Object.assign string coercion, Object.defineProperty bag synchronization, Object.getOwnPropertySymbols Proxy invariants, Promise newTarget, and Proxy.setPrototypeOf.
- **Small battles batch 1**: NativeErrors prototype inheritance & properties (`EvalError`, `RangeError`, `ReferenceError`, `SyntaxError`, `TypeError`, `URIError`), `Number.isSafeInteger`, generic `Date.prototype.toJSON` per spec, and `BigInt.asIntN`/`asUintN` `ToIndex` (+60 net PASS).
- **Small battles batch 2**: `Date.prototype.set*` order & undefined handling (+30), `Error.prototype` own `name`/`message`/`constructor` properties (+4), `Reflect.setPrototypeOf` (+11) (+47 PASS vs v0.3.2).
- **Small battles batch 3**: String small battles — `String.prototype.isWellFormed` (+8), `toWellFormed` (+8), `indexOf`/`lastIndexOf` position & searchValue coercion (+24), RegExp validation & position in `startsWith`/`endsWith`/`includes` (+25), and `normalize` (+10) (+75 PASS vs v0.3.3). 1 structural residual documented in `z-interpreter/docs/reports/STRING_RESIDUAL.md`.
- **TypedArray intrinsic hierarchy + methods**: `%TypedArray%` intrinsic constructor, prototype & constructor inheritance chain, `from`/`of`, `@@species`, `@@toStringTag`, `thisArg`, `fromIndex`, `set` array-like, `toLocaleString`, `fill` coercion order, `sort` `-0`, `toReversed`/`toSorted`/`with`, and constructor overloads (+564 PASS; 26 deferred to Groups 4/5, documented in `z-interpreter/docs/reports/TYPEDARRAY_RESIDUAL.md`).
- **for-of IteratorClose fix (+21 PASS general engine) + TypedArray Groups 3+4 (+443 desde v0.3.5)**: Integer-Indexed Exotic Object 10.4.5 complete, `TypedArraySpeciesCreate`/`GetPrototypeFromConstructor`/subclassing (plus `ArrayBuffer`/`DataView`/`SharedArrayBuffer` subclassing), and ES2015 7.4.11 `IteratorClose` on `return`/`break` in `for-of` loops.
- **Bytecode VM gaps — bitwise operators, typeof/void, ++/-- superinstructions (+12 opcodes, 3 turns, 0 regressions).** Closure captures deferred to ScopeAnalyzer redesign (`BYTECODE_VM_RESIDUAL.md`).
- **Bytecode VM — sequence expressions, exponentiation (zmath.pow spec-compliant), do-while (+15 opcodes total across 4 turns, 0 regressions).**
- **v0.3.12: Unificación de Error/NativeError/AggregateError en ZObject con [[ErrorData]] + Error.isError (+75 PASS)**.
- **v0.3.14 / v0.3.15: Soporte real de Detached ArrayBuffer en `z-buffer` (`v0.1.2`) + `$262.detachArrayBuffer` + guardas mid-call (+210 PASS, 0 CRASH, 0 regresiones PASS->FAIL)**.
- **v0.3.16–v0.3.20: Bloques 1–4 de E3/E4 — `Array.prototype` array-like genérico, descriptores/bags en builtins, `delete`/`for-in` en `Array`/`arguments`, `ArraySpeciesCreate` + `@@isConcatSpreadable`, `Reflect.preventExtensions`/`isExtensible`, invariantes de `Proxy`, `hoistDeclarations` + `liveElem` descriptors, Annex B `Object.prototype` accessors, `Object.groupBy` y `Object.fromEntries` (+856 PASS desde v0.3.15, 37,153 PASS / 81.4%, 0 CRASH)**.
- **v0.4.x–v0.4.16 (Fases 1–3 Test262, 40,499 PASS / 88.74%, 0 CRASH)**: Fase 1 (Parser/Runtime/Builtins), Fase 2 (`Array.prototype[Symbol.iterator]` en destructuring, `GetMethod`/`AsyncFromSyncIterator` estricto, `yield*` sync/async: 40,335 PASS / 88.38%), Fase 3 (`DataView.prototype.{getFloat16,setFloat16}` + detached, `Uint8Array` Base64/Hex, `TypedArray` exotic `[[Set]]`/`[[DefineOwnProperty]]`/`[[Delete]]` + `Reflect.set` `Receiver`: +164 PASS, 0 regresiones, `Temporal` 4,587/4,611).
- **v0.4.17 (Fase 4 Test262, 40,863 PASS / 89.54%, `TIMEOUT=1`, 0 CRASH)**: `SuppressedError`, `DisposableStack`, `AsyncDisposableStack`, `Symbol.{dispose,asyncDispose}` en iteradores, `Iterator.{concat,zip,zipKeyed}`, `%ArrayIteratorPrototype%` en Array/TypedArray, y cierre de 12/13 `TIMEOUT` en `Map`/`WeakMap`/`Set`/`WeakSet` y `Array.prototype.{splice,with}` (+364 PASS, 0 regresiones, `Temporal` 4,587/4,611).
- **v0.4.18 (Fase 5 Test262, 41,226 PASS / 90.33%, `TIMEOUT=0`, 0 CRASH)**: `Promise.{allKeyed,allSettledKeyed}`, `AsyncGeneratorQueue` FIFO (`TIMEOUT` 1→0), huecos reales en `new Array(len)` y elisiones `[,]`, `liveElem` con prototipos, `Array.prototype.{indexOf,lastIndexOf}` e índices de `Array` en `hasProperty`/`Object.keys`, literales `0x`/`0b`/`0o` en `toNumber`, `Function.prototype.{toString,apply,bind,Symbol.hasInstance}` y `OrdinaryHasInstance` (+363 PASS, 0 regresiones, `Temporal` 4,587/4,611).
- **v0.4.19 (Fase 6 Test262, 42,041 PASS / 92.12%, `TIMEOUT=0`, 0 CRASH)**: `JSON.{parse,stringify,rawJSON,isRawJSON}` (reviver/context-source/replacer/space/toJSON), `toLocaleString` y `toNumber` estricto; `Proxy` `[[Construct]]`/traps/callable; `Promise` genérico (`catch`/`finally`/combinadores), `Array.fromAsync`, `Map.groupBy`, `Set` `GetSetRecord`; `Error.prototype.stack`, `for..of` TypedArray/TDZ y compound-assignment; `CopyDataProperties` (`{ ...rest }` y object spread) y `%ThrowTypeError%` (`Function.prototype.{caller,arguments}` / `arguments.callee`); class field `eval` early `SyntaxError`, `#private` léxico en clases anidadas, `DefineField` `CreateDataPropertyOrThrow`, `fn-name`, `%GeneratorPrototype%`/`%AsyncGeneratorPrototype%`, `WeakMap.prototype.getOrInsert*`, `ArrayBuffer.isView` y `Array.prototype[Symbol.unscopables]` (+815 PASS, 0 regresiones, `Temporal` 4,587/4,611).
- **Parser Capa 1 + `z-interpreter@cda23db` (42,211 PASS / 92.49%, `TIMEOUT=0`, 0 CRASH)**: `z-parser v0.1.1` (`CoverInitializedName` `{ x = def }` y claves `BigInt`), `z-statements v0.2.1` (claves numéricas/string en `ObjectPattern`, ASI en `export default class/function`, LHS miembro/paréntesis en `for-in`/`for-of`), `z-functions v0.2.1` (contexto `async`/`yield` en computed property names y claves `BigInt` en clases) y dispatch de `bindForIteration` a `destructuringAssignTarget` (+170 PASS, 0 regresiones, `Temporal` 4,587/4,611).
- **Parser Capa 2 + `z-interpreter@47da5d9` (42,383 PASS / 92.87%, `TIMEOUT=0`, 0 CRASH)**: `z-parser v0.1.2` (`new.target` + *tagged templates* con escapes inválidos y `raw` normalizado), `z-statements v0.2.2` (claves computadas `[expr]: pat` en `ObjectPattern`), `z-functions v0.2.2` (`new_target_allowed` en scopes de función/clase) y runtime en `z-interpreter` (`new.target` en `Environment`/constructores/arrows/`eval`, `GetTemplateObject` cacheado/congelado y `setArrayProperty` en arrays congelados) (+172 PASS vs `cda23db` / +342 vs `v0.4.19`, 0 regresiones, `Temporal` 4,587/4,611).
- **Fase 7 + `z-interpreter@c4d5ca5` (42,602 PASS / 93.35%, `TIMEOUT=0`, 0 CRASH)**: `Function.prototype.toString` (Proxy callable, métodos/getters/setters/computed/privados, `Function`/`GeneratorFunction`/`AsyncFunction`/`AsyncGeneratorFunction`), `call`/`apply` strict vs sloppy (`this` boxing / `globalThis`), `ArrayBuffer.prototype.{transfer,transferToFixedLength}` + `slice` detached, `Object.prototype.{toString,valueOf,isPrototypeOf,hasOwnProperty,propertyIsEnumerable}` + inmutabilidad de `Object.prototype` y prototipos intrínsecos `async`/generadores (+219 PASS vs `47da5d9` / +561 vs `v0.4.19`, 0 regresiones, `Temporal` 4,587/4,611).
- **Fase 8 + fix JIT OSR (`z-interpreter@f684bf7`, 42,820 PASS / 93.82%, `TIMEOUT=0`, 0 CRASH)**: `eval` indirecto, `Array.prototype`, `%*IteratorPrototype%` (`Array`/`Map`/`Set`/`String`), `OOM→RangeError`, clases/`super`/`extends null`/TDZ de `this` derivado, `String.prototype` (`replaceAll`/`Symbol.iterator`/`localeCompare`/`toString`/`valueOf`), `TypedArray.prototype` (detached/species/`copyWithin`/`join`/`slice`/`subarray`), `for-in` (TDZ, shadowing no-enumerable, eliminación, completion value), `expressions/object` (`__proto__`, Proxy Symbol spread/rest, métodos generadores `.prototype`) y fix SIGSEGV en Baseline JIT OSR `.get_elem`/`.set_elem` (+218 PASS vs `c4d5ca5` / +779 vs `v0.4.19`, 0 regresiones, `Temporal` 4,587/4,611).
- **JIT Fases J2.5–J3 + Spec Quickwins 1–3 + Temporal 100.0% (`z-interpreter@c7bb14b`, 42,975 PASS / 94.16%, `TIMEOUT=0`, 0 CRASH)**: Fase J2.5 (fast-paths `i32` para índices/bitwise y hoisting de arrays invariantes en OSR), Fase J3.1 (`OsrPropIC` inline para valores heap con retain/release y `.load_global` inline vía `JitGlobalSlot`), Fase J3.2 (8 intrínsecos `Math.*` en OSR con elisión en preheader), Fase J3.3 (inlining OSR de funciones/métodos hoja `ops.len <= 16`), Spec Quickwins 1–3 (`NamedEvaluation` en `&&=`/`||=`/`??=`, `delete super`/`null`, single-eval `++`/`--`, `var_env` separado con default params, `UpdateEmpty` en sentencias/bucles, adopción de subclases `Promise`/`Date`, `Promise.prototype.then` species y métodos privados de instancia) y cierre de Temporal (`4,610/4,611`, `100.0%` en `REPORT.md`) (+155 PASS vs `f684bf7` / +934 vs `v0.4.19`, 0 regresiones).

Compared with the October v0.2.0 sweep, zero real PASS regressions reproduced.
The lookbehind test `test/built-ins/RegExp/named-groups/lookbehind.js` remains a known gap: z-regex v0.9.1 does not support backward lookbehind with captures under `u` (`/(?<=(?<a>\w){3})f/u`).

Input: `/tmp/sweep-c7bb14b.jsonl`.
Regenerate the committed report with:

```sh
python3 report.py /tmp/sweep-c7bb14b.jsonl > REPORT.md
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
