# Test262 — reporte de divergencias del motor z-*

Total: 34330 tests | corridos: 32645 | **PASS: 10965 (33.6% de los corridos)** | FAIL: 21680 | CRASH: 0 | TIMEOUT: 0 | SKIP (by design): 1685


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/Array | 369 | 2676 | 0 | 0 | 36 | 12.1% |
| test/built-ins/Boolean | 17 | 34 | 0 | 0 | 0 | 33.3% |
| test/built-ins/Date | 28 | 566 | 0 | 0 | 0 | 4.7% |
| test/built-ins/Error | 4 | 89 | 0 | 0 | 0 | 4.3% |
| test/built-ins/Function | 66 | 355 | 0 | 0 | 88 | 15.7% |
| test/built-ins/JSON | 50 | 115 | 0 | 0 | 0 | 30.3% |
| test/built-ins/Math | 56 | 271 | 0 | 0 | 0 | 17.1% |
| test/built-ins/NativeErrors | 12 | 82 | 0 | 0 | 0 | 12.8% |
| test/built-ins/Number | 54 | 286 | 0 | 0 | 0 | 15.9% |
| test/built-ins/Object | 1130 | 2270 | 0 | 0 | 11 | 33.2% |
| test/built-ins/Promise | 32 | 694 | 0 | 0 | 3 | 4.4% |
| test/built-ins/String | 198 | 1022 | 0 | 0 | 3 | 16.2% |
| test/language/arguments-object | 1 | 205 | 0 | 0 | 57 | 0.5% |
| test/language/asi | 98 | 4 | 0 | 0 | 0 | 96.1% |
| test/language/block-scope | 144 | 1 | 0 | 0 | 0 | 99.3% |
| test/language/comments | 38 | 14 | 0 | 0 | 0 | 73.1% |
| test/language/computed-property-names | 8 | 40 | 0 | 0 | 0 | 16.7% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 10 | 117 | 0 | 0 | 220 | 7.9% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 4079 | 6435 | 0 | 0 | 588 | 38.8% |
| test/language/function-code | 86 | 22 | 0 | 0 | 109 | 79.6% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 19 | 18 | 0 | 0 | 5 | 51.4% |
| test/language/identifier-resolution | 6 | 3 | 0 | 0 | 5 | 66.7% |
| test/language/identifiers | 200 | 68 | 0 | 0 | 0 | 74.6% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 27 | 14 | 0 | 0 | 0 | 65.9% |
| test/language/literals | 442 | 78 | 0 | 0 | 14 | 85.0% |
| test/language/module-code | 217 | 382 | 0 | 0 | 0 | 36.2% |
| test/language/punctuators | 10 | 1 | 0 | 0 | 0 | 90.9% |
| test/language/reserved-words | 27 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/rest-parameters | 6 | 5 | 0 | 0 | 0 | 54.5% |
| test/language/source-text | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/language/statementList | 32 | 48 | 0 | 0 | 0 | 40.0% |
| test/language/statements | 3287 | 5578 | 0 | 0 | 472 | 37.1% |
| test/language/types | 75 | 29 | 0 | 0 | 9 | 72.1% |
| test/language/white-space | 26 | 41 | 0 | 0 | 0 | 38.8% |

## Top causas de FAIL (mensaje normalizado)

- **3567x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/cls-decl-private-gen-meth-args-trailing-comma-multiple.js`
- **2944x** `Uncaught [object]`
  - ej: `test/language/arguments-object/10.5-1-s.js`
- **2854x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/cls-expr-async-private-gen-meth-args-trailing-comma-multiple.js`
- **2497x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/asi/S7.9_A10_T1.js`
- **1619x** `Uncaught ReferenceError: arguments is not defined`
  - ej: `test/language/arguments-object/10.5-7-b-2-s.js`
- **1334x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/comments/S7.4_A1_T1.js`
- **1076x** `async incomplete: Uncaught TypeError: async generators are not supported yet`
  - ej: `test/language/arguments-object/async-gen-meth-args-trailing-comma-multiple.js`
- **1062x** `Uncaught ReferenceError: Symbol is not defined`
  - ej: `test/language/computed-property-names/basics/symbol.js`
- **533x** `async incomplete: Uncaught ReferenceError: Symbol is not defined`
  - ej: `test/language/expressions/async-generator/named-yield-star-async-next.js`
- **488x** `Uncaught TypeError: Object.defineProperty called on non-object`
  - ej: `test/language/eval-code/indirect/var-env-func-init-global-update-configurable.js`
- **343x** `Uncaught ReferenceError: eval is not defined`
  - ej: `test/language/comments/mongolian-vowel-separator-single-eval.js`
- **305x** `Uncaught TypeError: object is not iterable`
  - ej: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-ary-elision-init.js`
- **238x** `async incomplete: `
  - ej: `test/language/expressions/async-arrow-function/try-reject-finally-reject.js`
- **196x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **134x** `async incomplete: Uncaught ReferenceError: globalThis is not defined`
  - ej: `test/language/expressions/async-function/named-strict-error-reassign-fn-name-in-body-in-arrow.js`
- **124x** `Uncaught ReferenceError: RegExp is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-RegExp.js`
- **117x** `Uncaught TypeError: getPrototypeOf is not a function`
  - ej: `test/language/arguments-object/10.6-5-1.js`
- **105x** `Uncaught TypeError: Object.getOwnPropertyDescriptor called on non-object`
  - ej: `test/language/eval-code/indirect/non-definable-function-with-function.js`
- **103x** `Uncaught ReferenceError: Proxy is not defined`
  - ej: `test/language/expressions/typeof/proxy.js`
- **102x** `Uncaught ReferenceError: UintNArray is not defined`
  - ej: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **99x** `Uncaught TypeError: hasOwnProperty is not a function`
  - ej: `test/language/expressions/arrow-function/ArrowFunction_restricted-properties.js`
- **84x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-function/named-dflt-params-ref-self.js`
- **78x** `async incomplete: Uncaught ReferenceError: print is not defined`
  - ej: `test/built-ins/Promise/all/iter-arg-is-false-reject.js`
- **69x** `Uncaught TypeError: Property description must be an object`
  - ej: `test/built-ins/Object/create/15.2.3.5-4-10.js`
- **65x** `Uncaught ReferenceError: $N is not defined`
  - ej: `test/language/eval-code/indirect/realm.js`
- **60x** `Uncaught TypeError: Object.defineProperties called on non-object`
  - ej: `test/language/expressions/typeof/get-value.js`
- **51x** `async incomplete: SyntaxError: MissingSemicolon`
  - ej: `test/language/import/import-attributes/json-idempotency.js`
- **51x** `Uncaught TypeError: split is not a function`
  - ej: `test/built-ins/String/prototype/split/arguments-are-boolean-expression-function-call-and-null-and-instance-is-boolean.js`
- **49x** `Uncaught TypeError: hasOwn is not a function`
  - ej: `test/built-ins/Object/hasOwn/hasown_inherited_exists.js`
- **47x** `Uncaught TypeError: Cannot set properties of undefined (setting '…')`
  - ej: `test/language/expressions/postfix-increment/S11.3.1_A2.1_T1.js`

## Top features presentes en FAILs

- 4043x async-iteration
- 3879x destructuring-binding
- 3735x class
- 2732x generators
- 1757x class-fields-public
- 1687x Symbol.iterator
- 1356x class-methods-private
- 1342x class-static-methods-private
- 1278x default-parameters
- 743x class-fields-private
- 604x dynamic-import
- 532x Symbol.asyncIterator
- 399x computed-property-names
- 386x Symbol
- 351x async-functions
- 339x object-rest
- 325x class-static-fields-private
- 258x top-level-await
- 242x arrow-function
- 208x Reflect.construct
- 204x BigInt
- 185x class-static-fields-public
- 154x import-defer
- 143x Proxy
- 139x Symbol.toPrimitive

---

## Análisis (actualizado 2026-07-19, post gramática gen/async)

### Delta de esta fase

**PASS 31.9% → 33.6% (+1.650 tests).** Entró: métodos generator/async en
object literals y clases (`*m()`, `async m()`, `async *m()`), async
arrows, y `yield*` delegación. CRASH sigue en 0.

Nota de lectura: el bucket "UnexpectedToken" bajó pero no se derrumbó
porque contenía MÁS que gen/async — class fields (`x = 1`), `#private`,
computed method keys, `for await`, etc. Y "Uncaught [object]" creció: son
tests que ahora corren lo bastante para tirar un `Test262Error` en una
aserción (fail legítimo detectado, antes ni parseaban) — señal de
progreso, no regresión.

### Historial

| corrida | PASS |
|---|---|
| baseline 2026-07-18 | 23.7% |
| + stack guard / JSON ciclos (CRASH 30→0) | 23.7% |
| + descriptors y constructores | 31.9% |
| + gramática gen/async | **33.6%** |

### Prioridades restantes

1. **arguments object** (1.619 `arguments is not defined` directos + los
   `Cannot read properties of undefined` que dependen — el gap ES1 más
   grande sin tocar).
2. **Symbol** (1.062+ `Symbol is not defined`) — habilita Symbol.iterator,
   well-known symbols, gran parte de built-ins.
3. Cobertura de métodos Array.prototype / String.prototype (splice, sort,
   flat, charCodeAt, replace, padStart...).
4. Class fields / #private / computed method keys (parte del
   UnexpectedToken restante).
5. Bug ASI do-while (chico, real).

### Cómo re-correr

```bash
python3 runner.py --jobs 8 --out results.jsonl test/language test/built-ins/...
python3 report.py results.jsonl > REPORT.md
```
