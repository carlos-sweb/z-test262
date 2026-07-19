# Test262 — reporte de divergencias del motor z-*

Total: 35015 tests | corridos: 33326 | **PASS: 11733 (35.2% de los corridos)** | FAIL: 21518 | CRASH: 0 | TIMEOUT: 75 | SKIP (by design): 1689


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/Array | 409 | 2636 | 0 | 0 | 36 | 13.4% |
| test/built-ins/Boolean | 17 | 34 | 0 | 0 | 0 | 33.3% |
| test/built-ins/Date | 31 | 563 | 0 | 0 | 0 | 5.2% |
| test/built-ins/Error | 4 | 89 | 0 | 0 | 0 | 4.3% |
| test/built-ins/Function | 78 | 343 | 0 | 0 | 88 | 18.5% |
| test/built-ins/JSON | 54 | 111 | 0 | 0 | 0 | 32.7% |
| test/built-ins/Map | 0 | 203 | 0 | 0 | 1 | 0.0% |
| test/built-ins/Math | 56 | 271 | 0 | 0 | 0 | 17.1% |
| test/built-ins/NativeErrors | 12 | 82 | 0 | 0 | 0 | 12.8% |
| test/built-ins/Number | 58 | 282 | 0 | 0 | 0 | 17.1% |
| test/built-ins/Object | 1163 | 2237 | 0 | 0 | 11 | 34.2% |
| test/built-ins/Promise | 34 | 692 | 0 | 0 | 3 | 4.7% |
| test/built-ins/Set | 0 | 382 | 0 | 0 | 1 | 0.0% |
| test/built-ins/String | 207 | 1013 | 0 | 0 | 3 | 17.0% |
| test/built-ins/Symbol | 17 | 79 | 0 | 0 | 2 | 17.7% |
| test/language/arguments-object | 80 | 126 | 0 | 0 | 57 | 38.8% |
| test/language/asi | 98 | 4 | 0 | 0 | 0 | 96.1% |
| test/language/block-scope | 144 | 1 | 0 | 0 | 0 | 99.3% |
| test/language/comments | 38 | 14 | 0 | 0 | 0 | 73.1% |
| test/language/computed-property-names | 12 | 36 | 0 | 0 | 0 | 25.0% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 10 | 117 | 0 | 0 | 220 | 7.9% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 4357 | 6109 | 0 | 48 | 588 | 41.4% |
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
| test/language/rest-parameters | 7 | 4 | 0 | 0 | 0 | 63.6% |
| test/language/source-text | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/language/statementList | 32 | 48 | 0 | 0 | 0 | 40.0% |
| test/language/statements | 3566 | 5272 | 0 | 27 | 472 | 40.2% |
| test/language/types | 78 | 26 | 0 | 0 | 9 | 75.0% |
| test/language/white-space | 26 | 41 | 0 | 0 | 0 | 38.8% |

## Top causas de FAIL (mensaje normalizado)

- **3659x** `Uncaught [object]`
  - ej: `test/language/arguments-object/10.5-1-s.js`
- **3571x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/cls-expr-private-gen-meth-args-trailing-comma-multiple.js`
- **3195x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/arguments-object/10.5-7-b-2-s.js`
- **2854x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/cls-expr-async-private-gen-meth-args-trailing-comma-multiple.js`
- **1572x** `async incomplete: Uncaught TypeError: async generators are not supported yet`
  - ej: `test/language/arguments-object/async-gen-meth-args-trailing-comma-multiple.js`
- **1389x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/comments/S7.4_A2_T1.js`
- **762x** `Uncaught TypeError: Object.getOwnPropertyDescriptor called on non-object`
  - ej: `test/language/arguments-object/10.6-11-b-1.js`
- **612x** `Uncaught TypeError: Object.defineProperty called on non-object`
  - ej: `test/language/eval-code/indirect/var-env-func-init-global-update-configurable.js`
- **347x** `Uncaught ReferenceError: eval is not defined`
  - ej: `test/language/comments/mongolian-vowel-separator-single-eval.js`
- **302x** `Uncaught ReferenceError: Set is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-Set.js`
- **255x** `async incomplete: `
  - ej: `test/language/expressions/async-arrow-function/try-reject-finally-reject.js`
- **196x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **161x** `Uncaught ReferenceError: Map is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-Map.js`
- **138x** `async incomplete: Uncaught ReferenceError: globalThis is not defined`
  - ej: `test/language/expressions/async-function/named-strict-error-reassign-fn-name-in-body-in-arrow.js`
- **128x** `Uncaught TypeError: getPrototypeOf is not a function`
  - ej: `test/language/arguments-object/10.6-5-1.js`
- **125x** `Uncaught ReferenceError: RegExp is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-RegExp.js`
- **121x** `Uncaught ReferenceError: Proxy is not defined`
  - ej: `test/language/expressions/object/object-spread-proxy-get-not-called-on-dontenum-keys.js`
- **102x** `Uncaught ReferenceError: UintNArray is not defined`
  - ej: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **100x** `Uncaught TypeError: hasOwnProperty is not a function`
  - ej: `test/language/expressions/arrow-function/ArrowFunction_restricted-properties.js`
- **84x** `Uncaught ReferenceError: $N is not defined`
  - ej: `test/language/eval-code/indirect/realm.js`
- **78x** `async incomplete: Uncaught ReferenceError: print is not defined`
  - ej: `test/built-ins/Promise/all/iter-arg-is-false-reject.js`
- **75x** `Uncaught TypeError: Property description must be an object`
  - ej: `test/built-ins/Object/create/15.2.3.5-4-10.js`
- **73x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-arrow-function/dflt-params-ref-self.js`
- **69x** `Uncaught TypeError: Object.defineProperties called on non-object`
  - ej: `test/language/expressions/typeof/get-value.js`
- **53x** `Uncaught TypeError: hasOwn is not a function`
  - ej: `test/built-ins/Object/hasOwn/hasown_inherited_exists.js`
- **51x** `async incomplete: SyntaxError: MissingSemicolon`
  - ej: `test/language/import/import-attributes/json-idempotency.js`
- **51x** `Uncaught TypeError: split is not a function`
  - ej: `test/built-ins/String/prototype/split/arguments-are-boolean-expression-function-call-and-null-and-instance-is-boolean.js`
- **50x** `Uncaught TypeError: Cannot set properties of undefined (setting '…')`
  - ej: `test/language/expressions/postfix-decrement/S11.3.2_A2.1_T1.js`
- **47x** `Uncaught TypeError: Cannot redefine property: foo`
  - ej: `test/built-ins/Object/defineProperties/15.2.3.7-6-a-42.js`
- **33x** `async incomplete: Uncaught TypeError: any is not a function`
  - ej: `test/built-ins/Promise/any/invoke-resolve-error-close.js`

## Top features presentes en FAILs

- 4027x async-iteration
- 3735x class
- 3422x destructuring-binding
- 2399x generators
- 1757x class-fields-public
- 1368x Symbol.iterator
- 1356x class-methods-private
- 1342x class-static-methods-private
- 1133x default-parameters
- 743x class-fields-private
- 604x dynamic-import
- 534x Symbol.asyncIterator
- 417x Symbol
- 399x computed-property-names
- 351x async-functions
- 339x object-rest
- 325x class-static-fields-private
- 272x arrow-function
- 258x top-level-await
- 237x Reflect.construct
- 208x BigInt
- 186x set-methods
- 185x class-static-fields-public
- 154x import-defer
- 144x Symbol.toPrimitive

---

## Análisis (actualizado 2026-07-19, post Symbol)

### Delta de esta fase

En el subconjunto comparable (mismos dirs que antes): **34.2% → 35.9%
(+1.7 pts, ~560 tests)**. Con Symbol/Map/Set agregados al scope: 35.2%
global. El salto grande fue en language/expressions (35.8%→41.4%) y
statements (34.7%→40.2%) — el cableado de `Symbol.iterator` al protocolo
de iteración real (for-of/spread/Array.from/destructuring sobre iterables
de usuario) destrabó cientos de tests. CRASH sigue en 0.

Symbol dir: 17.7% (el primitivo, claves-símbolo y Symbol.iterator andan;
los well-known toPrimitive/toStringTag/hasInstance existen como
identidad pero no están cableados — narrowing).

### Historial

| corrida | PASS (subset comparable) |
|---|---|
| baseline 2026-07-18 | 23.7% |
| stack guard (CRASH 30→0) | 23.7% |
| descriptors + constructores | 31.9% |
| gramática gen/async | 33.6% |
| arguments | 34.2% |
| Symbol + iterator protocol | **35.9%** |

### Prioridades restantes

1. Cobertura de métodos Array.prototype / String.prototype (splice, sort,
   flat, at, charCodeAt, replace, padStart, matchAll...) — mecánico, alto
   volumen; ahora que iterables/harness corren, cuentan.
2. **`arr[i] = x`** (asignación a índice de array por member) — gap chico
   y transversal, NotImplemented.
3. Well-known symbols cableados de verdad (toPrimitive en coercion,
   hasInstance en instanceof, toStringTag).
4. Map/Set con constructores + métodos JS (los tipos existen, sin API).
5. Class fields / #private / computed method keys; bug ASI do-while.
