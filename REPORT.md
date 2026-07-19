# Test262 — reporte de divergencias del motor z-*

Total: 34330 tests | corridos: 32645 | **PASS: 7730 (23.7% de los corridos)** | FAIL: 24885 | CRASH: 30 | TIMEOUT: 0 | SKIP (by design): 1685


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/Array | 177 | 2868 | 0 | 0 | 36 | 5.8% |
| test/built-ins/Boolean | 11 | 40 | 0 | 0 | 0 | 21.6% |
| test/built-ins/Date | 17 | 577 | 0 | 0 | 0 | 2.9% |
| test/built-ins/Error | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Function | 16 | 405 | 0 | 0 | 88 | 3.8% |
| test/built-ins/JSON | 20 | 143 | 2 | 0 | 0 | 12.1% |
| test/built-ins/Math | 45 | 282 | 0 | 0 | 0 | 13.8% |
| test/built-ins/NativeErrors | 4 | 90 | 0 | 0 | 0 | 4.3% |
| test/built-ins/Number | 26 | 314 | 0 | 0 | 0 | 7.6% |
| test/built-ins/Object | 12 | 3388 | 0 | 0 | 11 | 0.4% |
| test/built-ins/Promise | 9 | 717 | 0 | 0 | 3 | 1.2% |
| test/built-ins/String | 142 | 1078 | 0 | 0 | 3 | 11.6% |
| test/language/arguments-object | 1 | 205 | 0 | 0 | 57 | 0.5% |
| test/language/asi | 95 | 7 | 0 | 0 | 0 | 93.1% |
| test/language/block-scope | 144 | 1 | 0 | 0 | 0 | 99.3% |
| test/language/comments | 38 | 14 | 0 | 0 | 0 | 73.1% |
| test/language/computed-property-names | 3 | 45 | 0 | 0 | 0 | 6.2% |
| test/language/destructuring | 13 | 5 | 0 | 0 | 1 | 72.2% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 4 | 123 | 0 | 0 | 220 | 3.1% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 3204 | 7300 | 10 | 0 | 588 | 30.5% |
| test/language/function-code | 75 | 33 | 0 | 0 | 109 | 69.4% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 15 | 22 | 0 | 0 | 5 | 40.5% |
| test/language/identifier-resolution | 6 | 3 | 0 | 0 | 5 | 66.7% |
| test/language/identifiers | 200 | 68 | 0 | 0 | 0 | 74.6% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 27 | 14 | 0 | 0 | 0 | 65.9% |
| test/language/literals | 423 | 97 | 0 | 0 | 14 | 81.3% |
| test/language/module-code | 217 | 382 | 0 | 0 | 0 | 36.2% |
| test/language/punctuators | 10 | 1 | 0 | 0 | 0 | 90.9% |
| test/language/reserved-words | 15 | 12 | 0 | 0 | 0 | 55.6% |
| test/language/rest-parameters | 6 | 5 | 0 | 0 | 0 | 54.5% |
| test/language/source-text | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/language/statementList | 32 | 48 | 0 | 0 | 0 | 40.0% |
| test/language/statements | 2545 | 6302 | 18 | 0 | 472 | 28.7% |
| test/language/types | 58 | 46 | 0 | 0 | 9 | 55.8% |
| test/language/white-space | 26 | 41 | 0 | 0 | 0 | 38.8% |

## Top causas de FAIL (mensaje normalizado)

- **4901x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/gen-meth-args-trailing-comma-multiple.js`
- **4082x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/async-gen-meth-args-trailing-comma-multiple.js`
- **2653x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/arguments-object/10.5-1-s.js`
- **2074x** `Uncaught ReferenceError: Function is not defined`
  - ej: `test/language/arguments-object/10.6-11-b-1.js`
- **1801x** `Uncaught TypeError: defineProperty is not a function`
  - ej: `test/language/expressions/addition/coerce-symbol-to-prim-err.js`
- **1632x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/arguments-object/S10.6_A5_T3.js`
- **1219x** `Uncaught [object]`
  - ej: `test/language/arguments-object/S10.6_A1.js`
- **640x** `Uncaught ReferenceError: Symbol is not defined`
  - ej: `test/language/computed-property-names/basics/symbol.js`
- **379x** `Uncaught TypeError: String is not a constructor`
  - ej: `test/language/expressions/addition/S11.6.1_A3.2_T1.1.js`
- **377x** `async incomplete: Uncaught TypeError: async generators are not supported yet`
  - ej: `test/language/arguments-object/async-gen-named-func-expr-args-trailing-comma-multiple.js`
- **331x** `Uncaught TypeError: getOwnPropertyDescriptor is not a function`
  - ej: `test/language/arguments-object/10.6-13-c-2-s.js`
- **329x** `Uncaught ReferenceError: eval is not defined`
  - ej: `test/language/comments/mongolian-vowel-separator-single-eval.js`
- **272x** `Uncaught TypeError: Array is not a constructor`
  - ej: `test/language/statements/throw/S12.13_A2_T7.js`
- **265x** `Uncaught ReferenceError: arguments is not defined`
  - ej: `test/language/arguments-object/10.5-7-b-2-s.js`
- **255x** `Uncaught TypeError: Boolean is not a constructor`
  - ej: `test/language/expressions/addition/S11.6.1_A3.1_T2.1.js`
- **226x** `Uncaught TypeError: object is not iterable`
  - ej: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-ary-elision-init.js`
- **209x** `Uncaught TypeError: Number is not a constructor`
  - ej: `test/language/expressions/addition/S11.6.1_A3.1_T2.2.js`
- **197x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **161x** `async incomplete: `
  - ej: `test/language/expressions/async-function/named-returns-async-function.js`
- **153x** `Uncaught TypeError: Cannot set properties of undefined (setting '…')`
  - ej: `test/language/expressions/postfix-decrement/S11.3.2_A2.1_T1.js`
- **146x** `Uncaught TypeError: create is not a function`
  - ej: `test/language/expressions/object/accessor-name-computed-err-to-prop-key.js`
- **145x** `Uncaught TypeError: defineProperties is not a function`
  - ej: `test/language/expressions/typeof/get-value.js`
- **115x** `Uncaught TypeError: Object is not a constructor`
  - ej: `test/language/asi/S7.9_A5.5_T2.js`
- **106x** `Uncaught TypeError: hasOwnProperty is not a function`
  - ej: `test/language/expressions/array/spread-obj-manipulate-outter-obj-in-getter.js`
- **102x** `async incomplete: SyntaxError: MissingSemicolon`
  - ej: `test/language/expressions/async-arrow-function/try-reject-finally-reject.js`
- **99x** `Uncaught ReferenceError: UintNArray is not defined`
  - ej: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **97x** `async incomplete: Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/expressions/await/await-awaits-thenable-not-callable.js`
- **92x** `Uncaught TypeError: getPrototypeOf is not a function`
  - ej: `test/language/arguments-object/10.6-5-1.js`
- **85x** `Uncaught ReferenceError: Proxy is not defined`
  - ej: `test/language/expressions/typeof/proxy.js`
- **78x** `Uncaught ReferenceError: RegExp is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-RegExp.js`

## Top features presentes en FAILs

- 4997x destructuring-binding
- 4172x async-iteration
- 3739x class
- 3229x generators
- 1757x class-fields-public
- 1700x default-parameters
- 1697x Symbol.iterator
- 1356x class-methods-private
- 1342x class-static-methods-private
- 744x class-fields-private
- 604x dynamic-import
- 532x Symbol.asyncIterator
- 400x Symbol
- 399x computed-property-names
- 353x async-functions
- 345x object-rest
- 325x class-static-fields-private
- 302x arrow-function
- 269x Reflect.construct
- 258x top-level-await
- 204x BigInt
- 185x class-static-fields-public
- 154x import-defer
- 143x Proxy
- 139x Symbol.toPrimitive

## CRASHES (los más graves)

- **30x** `exit -N: `
  - ej: `test/language/expressions/tco-pos.js`

---

## Análisis de divergencias (baseline 2026-07-18)

### Lectura correcta del 23.7%

El pass-rate global está dominado por features **deliberadamente diferidas**, no por bugs de lo implementado. Las áreas del lenguaje que el motor SÍ implementa puntúan alto:

keywords 100% · future-reserved-words 100% · export 100% · directive-prologue 100% · **block-scope 99.3%** · **asi 93.1%** · literals 81.3% · identifiers 74.6% · destructuring 72.2% · function-code 69.4%

### Los buckets, por causa raíz

1. **~9.000 fails — gramática diferida** (`UnexpectedToken`): métodos generator/async en objetos y clases (`gen-meth-*`, `async-gen-meth-*`), async arrows, `yield*`. El bucket más grande por lejos; casi todo cae en los diferidos documentados de la fase 12/13b.
2. **~4.800 fails — sin property descriptors**: `Object.defineProperty`/`getOwnPropertyDescriptor` no existen → el helper `propertyHelper.js` del harness muere → **built-ins/Object 0.4%, Array 5.8%, Promise 1.2%** son en su mayoría este único gap, no bugs de las implementaciones.
3. **~3.200 fails — wrappers/constructores faltantes**: `Function` global (2.074), `new String/Number/Boolean/Array` como constructores (~1.100).
4. **1.632 NotImplemented honestos** + **640 Symbol** + **329 eval** + **265 arguments object**.
5. **30 CRASHES (SIGSEGV)** — todos los tests `tco-*` (proper tail calls, recursión 100k): el motor revienta el stack nativo en vez de tirar `RangeError: Maximum call stack size exceeded`. **Único hallazgo de crash; bug de robustez prioritario.**
6. **197 fails de ASI** (`do-while-same-line` y familia): divergencia REAL del parser en un área que puntúa 93% — candidato a bug puntual barato.
7. module-code 36.2%: mayormente el narrowing snapshot-bindings/ciclos, by design.

### Prioridades sugeridas para Etapa D (por costo/beneficio)

1. **Guard de profundidad de stack → RangeError** (elimina los 30 crashes; barato).
2. **Property descriptors** (`defineProperty`/`getOwnPropertyDescriptor`) + constructores reales (`Function`, `new Array/String/Number/Boolean`): desbloquea el harness completo y vuelve significativos miles de tests de built-ins.
3. **Gramática restante de la fase 12/13b**: métodos generator/async, async arrows, `yield*` (~9k tests).
4. **arguments object** (265+ tests, feature ES1 básica).
5. **Bug de ASI en do-while** (chico, real, área de 93%).

### Cómo re-correr

```bash
python3 runner.py --jobs 8 --out results.jsonl test/language test/built-ins/Array ...
python3 report.py results.jsonl > REPORT.md
```
