# Test262 — reporte de divergencias del motor z-*

Total: 34330 tests | corridos: 32645 | **PASS: 10430 (31.9% de los corridos)** | FAIL: 22215 | CRASH: 0 | TIMEOUT: 0 | SKIP (by design): 1685


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
| test/language/computed-property-names | 7 | 41 | 0 | 0 | 0 | 14.6% |
| test/language/destructuring | 15 | 3 | 0 | 0 | 1 | 83.3% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 10 | 117 | 0 | 0 | 220 | 7.9% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 3762 | 6752 | 0 | 0 | 588 | 35.8% |
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
| test/language/statements | 3072 | 5793 | 0 | 0 | 472 | 34.7% |
| test/language/types | 75 | 29 | 0 | 0 | 9 | 72.1% |
| test/language/white-space | 26 | 41 | 0 | 0 | 0 | 38.8% |

## Top causas de FAIL (mensaje normalizado)

- **4901x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/cls-decl-gen-meth-args-trailing-comma-multiple.js`
- **4082x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/async-gen-meth-args-trailing-comma-multiple.js`
- **2491x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/asi/S7.9_A10_T1.js`
- **2471x** `Uncaught [object]`
  - ej: `test/language/arguments-object/10.5-1-s.js`
- **1557x** `Uncaught ReferenceError: arguments is not defined`
  - ej: `test/language/arguments-object/10.5-7-b-2-s.js`
- **1334x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/comments/S7.4_A2_T1.js`
- **893x** `Uncaught ReferenceError: Symbol is not defined`
  - ej: `test/language/computed-property-names/basics/symbol.js`
- **488x** `Uncaught TypeError: Object.defineProperty called on non-object`
  - ej: `test/language/eval-code/indirect/var-env-func-init-global-update-configurable.js`
- **401x** `async incomplete: Uncaught TypeError: async generators are not supported yet`
  - ej: `test/language/arguments-object/async-gen-named-func-expr-args-trailing-comma-multiple.js`
- **343x** `Uncaught ReferenceError: eval is not defined`
  - ej: `test/language/comments/mongolian-vowel-separator-single-eval.js`
- **235x** `Uncaught TypeError: object is not iterable`
  - ej: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-ary-elision-init.js`
- **197x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **175x** `async incomplete: `
  - ej: `test/language/expressions/async-function/named-dflt-params-abrupt.js`
- **124x** `Uncaught ReferenceError: RegExp is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-RegExp.js`
- **114x** `Uncaught TypeError: getPrototypeOf is not a function`
  - ej: `test/language/arguments-object/10.6-5-1.js`
- **108x** `async incomplete: Uncaught ReferenceError: globalThis is not defined`
  - ej: `test/language/expressions/await/await-awaits-thenable-not-callable.js`
- **105x** `Uncaught TypeError: Object.getOwnPropertyDescriptor called on non-object`
  - ej: `test/language/eval-code/indirect/non-definable-function-with-function.js`
- **102x** `Uncaught ReferenceError: UintNArray is not defined`
  - ej: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **102x** `async incomplete: SyntaxError: MissingSemicolon`
  - ej: `test/language/expressions/async-arrow-function/dflt-params-abrupt.js`
- **101x** `Uncaught ReferenceError: Proxy is not defined`
  - ej: `test/language/expressions/typeof/proxy.js`
- **87x** `Uncaught TypeError: hasOwnProperty is not a function`
  - ej: `test/language/expressions/arrow-function/ArrowFunction_restricted-properties.js`
- **78x** `async incomplete: Uncaught ReferenceError: print is not defined`
  - ej: `test/built-ins/Promise/all/iter-arg-is-false-reject.js`
- **69x** `Uncaught TypeError: Property description must be an object`
  - ej: `test/built-ins/Object/create/15.2.3.5-4-10.js`
- **65x** `Uncaught ReferenceError: $N is not defined`
  - ej: `test/language/eval-code/indirect/realm.js`
- **61x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-function/named-dflt-params-ref-self.js`
- **60x** `Uncaught TypeError: Object.defineProperties called on non-object`
  - ej: `test/language/expressions/typeof/get-value.js`
- **51x** `async incomplete: Uncaught ReferenceError: Symbol is not defined`
  - ej: `test/language/expressions/async-generator/dstr/dflt-ary-init-iter-close.js`
- **51x** `Uncaught TypeError: split is not a function`
  - ej: `test/built-ins/String/prototype/split/arguments-are-boolean-expression-function-call-and-null-and-instance-is-boolean.js`
- **49x** `Uncaught TypeError: hasOwn is not a function`
  - ej: `test/built-ins/Object/hasOwn/hasown_inherited_exists.js`
- **47x** `Uncaught TypeError: Cannot set properties of undefined (setting '…')`
  - ej: `test/language/expressions/postfix-increment/S11.3.1_A2.1_T1.js`

## Top features presentes en FAILs

- 4251x destructuring-binding
- 4124x async-iteration
- 3735x class
- 3183x generators
- 1757x class-fields-public
- 1697x Symbol.iterator
- 1478x default-parameters
- 1356x class-methods-private
- 1342x class-static-methods-private
- 743x class-fields-private
- 604x dynamic-import
- 532x Symbol.asyncIterator
- 399x computed-property-names
- 386x Symbol
- 352x async-functions
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

## Análisis de divergencias (actualizado 2026-07-19, post property descriptors + constructores)

### Delta de esta fase

**PASS 23.7% → 31.9% (+2.700 tests).** built-ins/Object saltó de 0.4% a
33.2% (×83), language/expressions 30.5% → 35.8%, statements 28.7% →
34.7%. Lo que entró: Object.defineProperty/getOwnPropertyDescriptor/
getOwnPropertyNames/create/freeze/seal + enforcement strict de
descriptors (readonly/frozen/delete = TypeErrors reales), los métodos de
Object.prototype en todo objeto plano, constructores reales (Object/
Array/Function-que-parsea/String/Number/Boolean + statics), y
`.constructor` en errores — el contrato exacto de assert.throws.
CRASH sigue en 0.

### Historial

| corrida | PASS | delta |
|---|---|---|
| baseline 2026-07-18 | 23.7% (7.730) | — |
| + stack guard / JSON ciclos | 23.7%, CRASH 30→0 | robustez |
| + descriptors y constructores | **31.9% (10.430)** | +2.700 |

### Prioridades restantes (por costo/beneficio)

1. **Gramática restante 12/13b**: métodos generator/async en objetos y
   clases, async arrows, `yield*` — sigue siendo el bucket más grande
   (~9k tests con UnexpectedToken).
2. **arguments object** (ES1 básico, ~265 directos y muchos indirectos).
3. **Bug ASI do-while** (197 fails, área de 93%).
4. Métodos faltantes de Array.prototype (splice/sort/flat/findIndex/
   lastIndexOf...) y String.prototype (charCodeAt/replace/substring/
   padStart...) — ahora que el harness corre, estos cuentan de verdad.
5. Wrapper objects reales / Symbol / eval — gaps grandes de diseño.

### Cómo re-correr

```bash
python3 runner.py --jobs 8 --out results.jsonl test/language test/built-ins/...
python3 report.py results.jsonl > REPORT.md   # y re-agregar este análisis
```
