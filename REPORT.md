# Test262 — z-* engine divergence report

Total: 47381 tests | ran: 45639 | **PASS: 41226 (90.3% of those ran)** | FAIL: 4413 | CRASH: 0 | TIMEOUT: 0 | SKIP (by design): 1742


## Pass rate by area

| area | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 23 | 2 | 0 | 0 | 0 | 92.0% |
| test/built-ins/Array | 2828 | 217 | 0 | 0 | 36 | 92.9% |
| test/built-ins/ArrayBuffer | 96 | 125 | 0 | 0 | 0 | 43.4% |
| test/built-ins/ArrayIteratorPrototype | 13 | 6 | 0 | 0 | 8 | 68.4% |
| test/built-ins/AsyncDisposableStack | 101 | 3 | 0 | 0 | 0 | 97.1% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 38 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/AsyncFunction | 10 | 8 | 0 | 0 | 0 | 55.6% |
| test/built-ins/AsyncGeneratorFunction | 9 | 14 | 0 | 0 | 0 | 39.1% |
| test/built-ins/AsyncGeneratorPrototype | 26 | 22 | 0 | 0 | 0 | 54.2% |
| test/built-ins/AsyncIteratorPrototype | 13 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/Atomics | 210 | 177 | 0 | 0 | 2 | 54.3% |
| test/built-ins/BigInt | 70 | 7 | 0 | 0 | 0 | 90.9% |
| test/built-ins/Boolean | 49 | 2 | 0 | 0 | 0 | 96.1% |
| test/built-ins/DataView | 514 | 47 | 0 | 0 | 0 | 91.6% |
| test/built-ins/Date | 571 | 23 | 0 | 0 | 0 | 96.1% |
| test/built-ins/DisposableStack | 91 | 2 | 0 | 0 | 0 | 97.8% |
| test/built-ins/Error | 54 | 39 | 0 | 0 | 0 | 58.1% |
| test/built-ins/FinalizationRegistry | 46 | 1 | 0 | 0 | 0 | 97.9% |
| test/built-ins/Function | 266 | 155 | 0 | 0 | 88 | 63.2% |
| test/built-ins/GeneratorFunction | 9 | 14 | 0 | 0 | 0 | 39.1% |
| test/built-ins/GeneratorPrototype | 47 | 14 | 0 | 0 | 0 | 77.0% |
| test/built-ins/Infinity | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/Iterator | 492 | 22 | 0 | 0 | 0 | 95.7% |
| test/built-ins/JSON | 82 | 83 | 0 | 0 | 0 | 49.7% |
| test/built-ins/Map | 185 | 18 | 0 | 0 | 1 | 91.1% |
| test/built-ins/MapIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/Math | 327 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/NaN | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/NativeErrors | 82 | 12 | 0 | 0 | 0 | 87.2% |
| test/built-ins/Number | 310 | 30 | 0 | 0 | 0 | 91.2% |
| test/built-ins/Object | 3275 | 125 | 0 | 0 | 11 | 96.3% |
| test/built-ins/Promise | 659 | 67 | 0 | 0 | 3 | 90.8% |
| test/built-ins/Proxy | 201 | 99 | 0 | 0 | 11 | 67.0% |
| test/built-ins/Reflect | 147 | 6 | 0 | 0 | 0 | 96.1% |
| test/built-ins/RegExp | 1773 | 105 | 0 | 0 | 1 | 94.4% |
| test/built-ins/RegExpStringIteratorPrototype | 17 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/Set | 354 | 28 | 0 | 0 | 1 | 92.7% |
| test/built-ins/SetIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 74 | 30 | 0 | 0 | 0 | 71.2% |
| test/built-ins/String | 1188 | 32 | 0 | 0 | 3 | 97.4% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 20 | 2 | 0 | 0 | 0 | 90.9% |
| test/built-ins/Symbol | 71 | 25 | 0 | 0 | 2 | 74.0% |
| test/built-ins/Temporal | 4579 | 24 | 0 | 0 | 0 | 99.5% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 1213 | 225 | 0 | 0 | 8 | 84.4% |
| test/built-ins/TypedArrayConstructors | 682 | 40 | 0 | 0 | 16 | 94.5% |
| test/built-ins/Uint8Array | 68 | 2 | 0 | 0 | 0 | 97.1% |
| test/built-ins/WeakMap | 116 | 25 | 0 | 0 | 0 | 82.3% |
| test/built-ins/WeakRef | 28 | 1 | 0 | 0 | 0 | 96.6% |
| test/built-ins/WeakSet | 84 | 1 | 0 | 0 | 0 | 98.8% |
| test/built-ins/decodeURI | 55 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/decodeURIComponent | 56 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/encodeURI | 26 | 5 | 0 | 0 | 0 | 83.9% |
| test/built-ins/encodeURIComponent | 26 | 5 | 0 | 0 | 0 | 83.9% |
| test/built-ins/eval | 10 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/global | 29 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/isFinite | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/isNaN | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/parseFloat | 54 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/parseInt | 55 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/undefined | 5 | 0 | 0 | 0 | 3 | 100.0% |
| test/language/arguments-object | 194 | 12 | 0 | 0 | 57 | 94.2% |
| test/language/asi | 101 | 1 | 0 | 0 | 0 | 99.0% |
| test/language/block-scope | 145 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/comments | 46 | 6 | 0 | 0 | 0 | 88.5% |
| test/language/computed-property-names | 47 | 1 | 0 | 0 | 0 | 97.9% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 96 | 31 | 0 | 0 | 220 | 75.6% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 9359 | 1155 | 0 | 0 | 588 | 89.0% |
| test/language/function-code | 100 | 8 | 0 | 0 | 109 | 92.6% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 24 | 13 | 0 | 0 | 5 | 64.9% |
| test/language/identifier-resolution | 8 | 1 | 0 | 0 | 5 | 88.9% |
| test/language/identifiers | 264 | 4 | 0 | 0 | 0 | 98.5% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 39 | 2 | 0 | 0 | 0 | 95.1% |
| test/language/literals | 519 | 1 | 0 | 0 | 14 | 99.8% |
| test/language/module-code | 216 | 383 | 0 | 0 | 0 | 36.1% |
| test/language/punctuators | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/reserved-words | 27 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/rest-parameters | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/source-text | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/statementList | 76 | 4 | 0 | 0 | 0 | 95.0% |
| test/language/statements | 8196 | 669 | 0 | 0 | 472 | 92.5% |
| test/language/types | 101 | 3 | 0 | 0 | 9 | 97.1% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top FAIL causes (normalized message)

- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - e.g.: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **516x** `SyntaxError: UnexpectedToken`
  - e.g.: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **196x** `SyntaxError: MissingSemicolon`
  - e.g.: `test/language/asi/do-while-same-line.js`
- **172x** `Uncaught TypeError: createRealm is not a function`
  - e.g.: `test/language/eval-code/indirect/realm.js`
- **150x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/arguments-object/10.6-13-c-1-s.js`
- **148x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/language/arguments-object/10.6-13-c-3-s.js`
- **99x** `Uncaught TypeError: resize is not a function`
  - e.g.: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **86x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - e.g.: `test/language/expressions/arrow-function/dstr/dflt-obj-ptrn-rest-getter.js`
- **77x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - e.g.: `test/language/eval-code/indirect/var-env-func-non-strict.js`
- **76x** `Uncaught { message: implements ArrayBuffer.prototype.resize Expected SameValue(«"undefined"», «"function"») to`
  - e.g.: `test/built-ins/DataView/prototype/getBigInt64/resizable-buffer.js`
- **75x** `Uncaught TypeError: undefined is not a function`
  - e.g.: `test/built-ins/Array/prototype/at/coerced-index-resize.js`
- **61x** `async incomplete: Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/built-ins/AsyncGeneratorFunction/invoked-as-constructor-no-arguments.js`
- **58x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - e.g.: `test/language/expressions/object/method-definition/generator-prototype-prop.js`
- **57x** `Uncaught ReferenceError: ShadowRealm is not defined`
  - e.g.: `test/built-ins/ShadowRealm/extensibility.js`
- **55x** `Uncaught { message: Expected a SyntaxError but got a ReferenceError }`
  - e.g.: `test/language/arguments-object/10.5-1-s.js`
- **51x** `async incomplete: SyntaxError: MissingSemicolon`
  - e.g.: `test/language/import/import-attributes/json-idempotency.js`
- **43x** `Uncaught { message: Expected SameValue(«undefined», «N») to be true }`
  - e.g.: `test/language/expressions/array/spread-obj-mult-spread-getter.js`
- **40x** `Uncaught { message: Expected SameValue(«true», «false») to be true }`
  - e.g.: `test/language/eval-code/direct/super-call-fn.js`
- **36x** `Uncaught { message: Expected a TypeError but got a TestNError }`
  - e.g.: `test/language/expressions/compound-assignment/S11.13.2_A7.10_T1.js`
- **33x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«Error», «TypeError») to b`
  - e.g.: `test/built-ins/Promise/allSettled/iter-arg-is-false-reject.js`
- **32x** `Uncaught { message: The value of `typeof Atomics.waitAsync` is "function" Expected SameValue(«"undefined"», «"`
  - e.g.: `test/built-ins/Atomics/waitAsync/bad-range.js`
- **31x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/expressions/assignment/dstr/obj-rest-getter-abrupt-get-error.js`
- **30x** `Uncaught { message: Expected true but got false }`
  - e.g.: `test/language/expressions/compound-assignment/S11.13.2_A7.10_T4.js`
- **28x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«N», «N») to be true`
  - e.g.: `test/language/expressions/async-generator/dstr/dflt-obj-ptrn-rest-getter.js`
- **28x** `Uncaught TypeError: object is not iterable`
  - e.g.: `test/language/statements/for-of/float32array-mutate.js`
- **22x** `Engine error: StackOverflow`
  - e.g.: `test/language/expressions/tco-pos.js`
- **22x** `Uncaught { message: Expected a SyntaxError but got a TypeError }`
  - e.g.: `test/language/expressions/class/elements/arrow-body-private-derived-cls-direct-eval-err-contains-supercall-1.js`
- **21x** `Uncaught { message: Expected SameValue(«"inside"», «"outside"») to be true }`
  - e.g.: `test/language/expressions/arrow-function/scope-paramsbody-var-open.js`
- **20x** `Uncaught TypeError: toLocaleString is not a function`
  - e.g.: `test/built-ins/Array/prototype/toLocaleString/S15.4.4.3_A1_T1.js`
- **19x** `Uncaught TypeError: Cannot set properties of undefined (setting '…')`
  - e.g.: `test/built-ins/Function/S15.3.5_A2_T1.js`

## Top features present in FAILs

- 604x dynamic-import
- 401x resizable-arraybuffer
- 362x TypedArray
- 349x class
- 276x destructuring-binding
- 258x top-level-await
- 220x async-iteration
- 183x SharedArrayBuffer
- 181x Proxy
- 179x Symbol
- 177x Atomics
- 175x cross-realm
- 166x generators
- 165x BigInt
- 154x import-defer
- 136x class-fields-public
- 132x arrow-function
- 127x Reflect
- 123x explicit-resource-management
- 101x Atomics.waitAsync
- 98x source-phase-imports
- 91x object-rest
- 89x Symbol.iterator
- 89x class-fields-private
- 88x async-functions
