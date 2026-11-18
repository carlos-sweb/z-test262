# Test262 — z-* engine divergence report

Total: 47381 tests | ran: 45639 | **PASS: 36924 (80.9% of those ran)** | FAIL: 8691 | CRASH: 0 | TIMEOUT: 24 | SKIP (by design): 1742


## Pass rate by area

| area | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 23 | 2 | 0 | 0 | 0 | 92.0% |
| test/built-ins/Array | 2445 | 596 | 0 | 4 | 36 | 80.3% |
| test/built-ins/ArrayBuffer | 96 | 125 | 0 | 0 | 0 | 43.4% |
| test/built-ins/ArrayIteratorPrototype | 10 | 9 | 0 | 0 | 8 | 52.6% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 8 | 28 | 0 | 2 | 0 | 21.1% |
| test/built-ins/AsyncFunction | 10 | 8 | 0 | 0 | 0 | 55.6% |
| test/built-ins/AsyncGeneratorFunction | 9 | 14 | 0 | 0 | 0 | 39.1% |
| test/built-ins/AsyncGeneratorPrototype | 2 | 45 | 0 | 1 | 0 | 4.2% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 210 | 177 | 0 | 0 | 2 | 54.3% |
| test/built-ins/BigInt | 70 | 7 | 0 | 0 | 0 | 90.9% |
| test/built-ins/Boolean | 49 | 2 | 0 | 0 | 0 | 96.1% |
| test/built-ins/DataView | 451 | 110 | 0 | 0 | 0 | 80.4% |
| test/built-ins/Date | 571 | 23 | 0 | 0 | 0 | 96.1% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 54 | 39 | 0 | 0 | 0 | 58.1% |
| test/built-ins/FinalizationRegistry | 46 | 1 | 0 | 0 | 0 | 97.9% |
| test/built-ins/Function | 223 | 198 | 0 | 0 | 88 | 53.0% |
| test/built-ins/GeneratorFunction | 9 | 14 | 0 | 0 | 0 | 39.1% |
| test/built-ins/GeneratorPrototype | 15 | 45 | 0 | 1 | 0 | 24.6% |
| test/built-ins/Infinity | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/Iterator | 363 | 151 | 0 | 0 | 0 | 70.6% |
| test/built-ins/JSON | 82 | 83 | 0 | 0 | 0 | 49.7% |
| test/built-ins/Map | 151 | 50 | 0 | 2 | 1 | 74.4% |
| test/built-ins/MapIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/Math | 327 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/NaN | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/NativeErrors | 82 | 12 | 0 | 0 | 0 | 87.2% |
| test/built-ins/Number | 279 | 61 | 0 | 0 | 0 | 82.1% |
| test/built-ins/Object | 3193 | 207 | 0 | 0 | 11 | 93.9% |
| test/built-ins/Promise | 264 | 461 | 0 | 1 | 3 | 36.4% |
| test/built-ins/Proxy | 194 | 106 | 0 | 0 | 11 | 64.7% |
| test/built-ins/Reflect | 138 | 15 | 0 | 0 | 0 | 90.2% |
| test/built-ins/RegExp | 1773 | 105 | 0 | 0 | 1 | 94.4% |
| test/built-ins/RegExpStringIteratorPrototype | 16 | 1 | 0 | 0 | 0 | 94.1% |
| test/built-ins/Set | 220 | 162 | 0 | 0 | 1 | 57.6% |
| test/built-ins/SetIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 74 | 30 | 0 | 0 | 0 | 71.2% |
| test/built-ins/String | 1188 | 32 | 0 | 0 | 3 | 97.4% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 0 | 22 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Symbol | 71 | 25 | 0 | 0 | 2 | 74.0% |
| test/built-ins/Temporal | 4579 | 24 | 0 | 0 | 0 | 99.5% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 1213 | 225 | 0 | 0 | 8 | 84.4% |
| test/built-ins/TypedArrayConstructors | 655 | 67 | 0 | 0 | 16 | 90.7% |
| test/built-ins/Uint8Array | 8 | 62 | 0 | 0 | 0 | 11.4% |
| test/built-ins/WeakMap | 112 | 28 | 0 | 1 | 0 | 79.4% |
| test/built-ins/WeakRef | 28 | 1 | 0 | 0 | 0 | 96.6% |
| test/built-ins/WeakSet | 83 | 2 | 0 | 0 | 0 | 97.6% |
| test/built-ins/decodeURI | 54 | 0 | 0 | 1 | 0 | 98.2% |
| test/built-ins/decodeURIComponent | 55 | 0 | 0 | 1 | 0 | 98.2% |
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
| test/language/expressions | 7925 | 2585 | 0 | 4 | 588 | 75.4% |
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
| test/language/statements | 7047 | 1812 | 0 | 6 | 472 | 79.5% |
| test/language/types | 101 | 3 | 0 | 0 | 9 | 97.1% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top FAIL causes (normalized message)

- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - e.g.: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **516x** `SyntaxError: UnexpectedToken`
  - e.g.: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **486x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/arguments-object/10.6-13-c-1-s.js`
- **453x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/expressions/assignment/dstr/array-empty-iter-close-err.js`
- **401x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - e.g.: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-id-iter-val-array-prototype.js`
- **228x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: TypeError Expected SameValue(«[object Functio`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-not-callable-boolean-throw.js`
- **196x** `SyntaxError: MissingSemicolon`
  - e.g.: `test/language/asi/do-while-same-line.js`
- **186x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«N», «N») to be true`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-null-sync-get-abrupt.js`
- **182x** `Uncaught { message: Expected SameValue(«[object Function]», «N») to be true }`
  - e.g.: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **172x** `Uncaught TypeError: resize is not a function`
  - e.g.: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **172x** `Uncaught TypeError: createRealm is not a function`
  - e.g.: `test/language/eval-code/indirect/realm.js`
- **166x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/language/arguments-object/10.6-13-c-3-s.js`
- **142x** `Uncaught { message: Expected a ReferenceError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/expressions/arrow-function/dflt-params-ref-self.js`
- **132x** `Uncaught RangeError: Maximum call stack size exceeded`
  - e.g.: `test/language/expressions/tco-pos.js`
- **131x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - e.g.: `test/language/expressions/object/method-definition/generator-prototype-prop.js`
- **116x** `async incomplete: Out of memory: OutOfMemory`
  - e.g.: `test/language/expressions/async-generator/dstr/ary-init-iter-close.js`
- **111x** `Out of memory: OutOfMemory`
  - e.g.: `test/language/expressions/arrow-function/dstr/ary-init-iter-close.js`
- **110x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - e.g.: `test/language/eval-code/indirect/var-env-func-non-strict.js`
- **96x** `Uncaught { message: Expected SameValue(«undefined», «N») to be true }`
  - e.g.: `test/language/expressions/array/spread-obj-mult-spread-getter.js`
- **96x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: reject reason Expected SameValue(«TestNError:`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-get-abrupt.js`
- **87x** `Uncaught ReferenceError: DisposableStack is not defined`
  - e.g.: `test/built-ins/DisposableStack/instance-extensible.js`
- **84x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: it should not get Symbol.iterator`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-next-then-non-callable-boolean-fulfillpromise.js`
- **76x** `Uncaught { message: implements ArrayBuffer.prototype.resize Expected SameValue(«"undefined"», «"function"») to`
  - e.g.: `test/built-ins/DataView/prototype/getBigInt64/resizable-buffer.js`
- **70x** `Uncaught ReferenceError: AsyncDisposableStack is not defined`
  - e.g.: `test/built-ins/AsyncDisposableStack/instance-extensible.js`
- **66x** `Uncaught { message: testResult !== true }`
  - e.g.: `test/built-ins/Array/prototype/forEach/15.4.4.18-3-16.js`
- **64x** `async incomplete: TestN:AsyncTestFailure:TypeError: fromAsync is not a function`
  - e.g.: `test/built-ins/Array/fromAsync/async-iterable-async-mapped-awaits-once.js`
- **61x** `async incomplete: Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/built-ins/AsyncGeneratorFunction/invoked-as-constructor-no-arguments.js`
- **57x** `Uncaught ReferenceError: ShadowRealm is not defined`
  - e.g.: `test/built-ins/ShadowRealm/extensibility.js`
- **56x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«[object Function]», «N») `
  - e.g.: `test/language/expressions/class/elements/after-same-line-static-async-gen-rs-private-getter-alt.js`
- **55x** `Uncaught { message: Expected a SyntaxError but got a ReferenceError }`
  - e.g.: `test/language/arguments-object/10.5-1-s.js`

## Top features present in FAILs

- 1491x async-iteration
- 1207x generators
- 1122x Symbol.iterator
- 1065x class
- 1060x destructuring-binding
- 680x class-fields-public
- 604x dynamic-import
- 500x Symbol.asyncIterator
- 449x TypedArray
- 439x class-methods-private
- 436x default-parameters
- 402x resizable-arraybuffer
- 395x class-fields-private
- 350x explicit-resource-management
- 347x class-static-methods-private
- 258x top-level-await
- 221x Symbol
- 209x Proxy
- 191x arrow-function
- 185x BigInt
- 183x SharedArrayBuffer
- 177x Atomics
- 175x cross-realm
- 168x Reflect
- 157x async-functions
