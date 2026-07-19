# Test262 — reporte de divergencias del motor z-*

Total: 35015 tests | corridos: 33326 | **PASS: 12071 (36.2% de los corridos)** | FAIL: 21159 | CRASH: 0 | TIMEOUT: 96 | SKIP (by design): 1689


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/Array | 607 | 2417 | 0 | 21 | 36 | 19.9% |
| test/built-ins/Boolean | 17 | 34 | 0 | 0 | 0 | 33.3% |
| test/built-ins/Date | 31 | 563 | 0 | 0 | 0 | 5.2% |
| test/built-ins/Error | 4 | 89 | 0 | 0 | 0 | 4.3% |
| test/built-ins/Function | 78 | 343 | 0 | 0 | 88 | 18.5% |
| test/built-ins/JSON | 64 | 101 | 0 | 0 | 0 | 38.8% |
| test/built-ins/Map | 0 | 203 | 0 | 0 | 1 | 0.0% |
| test/built-ins/Math | 78 | 249 | 0 | 0 | 0 | 23.9% |
| test/built-ins/NativeErrors | 12 | 82 | 0 | 0 | 0 | 12.8% |
| test/built-ins/Number | 58 | 282 | 0 | 0 | 0 | 17.1% |
| test/built-ins/Object | 1166 | 2234 | 0 | 0 | 11 | 34.3% |
| test/built-ins/Promise | 34 | 692 | 0 | 0 | 3 | 4.7% |
| test/built-ins/Set | 0 | 382 | 0 | 0 | 1 | 0.0% |
| test/built-ins/String | 246 | 974 | 0 | 0 | 3 | 20.2% |
| test/built-ins/Symbol | 17 | 79 | 0 | 0 | 2 | 17.7% |
| test/language/arguments-object | 86 | 120 | 0 | 0 | 57 | 41.7% |
| test/language/asi | 98 | 4 | 0 | 0 | 0 | 96.1% |
| test/language/block-scope | 144 | 1 | 0 | 0 | 0 | 99.3% |
| test/language/comments | 38 | 14 | 0 | 0 | 0 | 73.1% |
| test/language/computed-property-names | 12 | 36 | 0 | 0 | 0 | 25.0% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 10 | 117 | 0 | 0 | 220 | 7.9% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 4391 | 6075 | 0 | 48 | 588 | 41.8% |
| test/language/function-code | 90 | 18 | 0 | 0 | 109 | 83.3% |
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
| test/language/rest-parameters | 8 | 3 | 0 | 0 | 0 | 72.7% |
| test/language/source-text | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/language/statementList | 32 | 48 | 0 | 0 | 0 | 40.0% |
| test/language/statements | 3585 | 5253 | 0 | 27 | 472 | 40.4% |
| test/language/types | 80 | 24 | 0 | 0 | 9 | 76.9% |
| test/language/white-space | 26 | 41 | 0 | 0 | 0 | 38.8% |

## Top causas de FAIL (mensaje normalizado)

- **3803x** `Uncaught [object]`
  - ej: `test/language/arguments-object/S10.6_A5_T4.js`
- **3571x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/cls-decl-private-gen-meth-args-trailing-comma-multiple.js`
- **2854x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/cls-decl-async-private-gen-meth-args-trailing-comma-multiple.js`
- **2651x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/arguments-object/S10.6_A3_T1.js`
- **1572x** `async incomplete: Uncaught TypeError: async generators are not supported yet`
  - ej: `test/language/arguments-object/async-gen-meth-args-trailing-comma-multiple.js`
- **1403x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/comments/S7.4_A2_T1.js`
- **763x** `Uncaught TypeError: Object.getOwnPropertyDescriptor called on non-object`
  - ej: `test/language/arguments-object/arguments-caller.js`
- **621x** `Uncaught TypeError: Object.defineProperty called on non-object`
  - ej: `test/language/eval-code/indirect/var-env-func-init-global-update-configurable.js`
- **347x** `Uncaught ReferenceError: eval is not defined`
  - ej: `test/language/comments/mongolian-vowel-separator-single-eval.js`
- **302x** `Uncaught ReferenceError: Set is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-Set.js`
- **256x** `async incomplete: `
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
- **74x** `Uncaught TypeError: Object.defineProperties called on non-object`
  - ej: `test/language/expressions/typeof/get-value.js`
- **72x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-function/named-dflt-params-ref-self.js`
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
- 2391x generators
- 1757x class-fields-public
- 1368x Symbol.iterator
- 1356x class-methods-private
- 1342x class-static-methods-private
- 1119x default-parameters
- 743x class-fields-private
- 604x dynamic-import
- 534x Symbol.asyncIterator
- 407x Symbol
- 399x computed-property-names
- 351x async-functions
- 339x object-rest
- 325x class-static-fields-private
- 271x arrow-function
- 258x top-level-await
- 236x Reflect.construct
- 208x BigInt
- 186x set-methods
- 185x class-static-fields-public
- 154x import-defer
- 144x Symbol.toPrimitive

---

## Análisis (actualizado 2026-07-19, post cobertura Array/String)

### Delta de esta fase

Subconjunto comparable: **35.9% → 36.9% (+1.0 pt, ~340 tests)**. Global
36.2%. built-ins/Array 12.1%→19.9%, built-ins/String ~11.6%→20.2%. Se
cableó casi todo Array.prototype (splice/sort/fill/copyWithin/flat/at/
findIndex/findLast/reduceRight/flatMap/keys/values/entries) y
String.prototype (charCodeAt/codePointAt/at/padStart/padEnd/substring/
substr/lastIndexOf/concat/trimStart/trimEnd/replace/replaceAll/
localeCompare), reusando z-array/z-string; y el gap transversal
**arr[i]=x / arr.length=n / arr[i]+=1**. CRASH sigue en 0.

Los dirs built-ins/Array y /String quedan en ~20% porque Test262 ahí
testea muchísimo edge exótico (this-coercion genérico, descriptors de
length, getters, sparse real) fuera del alcance narrowed; el grueso del
valor está en los usos incidentales a lo largo de language/.

### Historial

| corrida | PASS (subset comparable) |
|---|---|
| baseline 2026-07-18 | 23.7% |
| descriptors + constructores | 31.9% |
| gramática gen/async | 33.6% |
| arguments | 34.2% |
| Symbol + iterator protocol | 35.9% |
| Array/String coverage + arr[i]=x | **36.9%** |

### Prioridades restantes

1. **Regex (zregexp cableado)**: regex literals a `.regex` runtime, y los
   String methods regex (match/matchAll/search, replace-con-regex) —
   gap grande, fase propia; el existe (zregexp) pero no está conectado.
2. **Map/Set con API JS** (constructores + get/set/has/delete/size +
   iteración) — los tipos existen, sin métodos.
3. Well-known symbols cableados (toPrimitive en coercion, hasInstance en
   instanceof).
4. Class fields / #private / computed method keys; bug ASI do-while.
5. Exotic array semantics (sparse, length descriptors) para subir los
   dirs built-ins/Array/String.
