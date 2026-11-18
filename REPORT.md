# Test262 — z-* engine divergence report

Total: 47381 tests | ran: 45639 | **PASS: 36297 (79.5% of those ran)** | FAIL: 9321 | CRASH: 0 | TIMEOUT: 21 | SKIP (by design): 1742


## Pass rate by area

| area | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 22 | 3 | 0 | 0 | 0 | 88.0% |
| test/built-ins/Array | 2120 | 924 | 0 | 1 | 36 | 69.6% |
| test/built-ins/ArrayBuffer | 96 | 125 | 0 | 0 | 0 | 43.4% |
| test/built-ins/ArrayIteratorPrototype | 10 | 9 | 0 | 0 | 8 | 52.6% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 8 | 28 | 0 | 2 | 0 | 21.1% |
| test/built-ins/AsyncFunction | 9 | 9 | 0 | 0 | 0 | 50.0% |
| test/built-ins/AsyncGeneratorFunction | 8 | 15 | 0 | 0 | 0 | 34.8% |
| test/built-ins/AsyncGeneratorPrototype | 2 | 45 | 0 | 1 | 0 | 4.2% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 210 | 177 | 0 | 0 | 2 | 54.3% |
| test/built-ins/BigInt | 70 | 7 | 0 | 0 | 0 | 90.9% |
| test/built-ins/Boolean | 47 | 4 | 0 | 0 | 0 | 92.2% |
| test/built-ins/DataView | 448 | 113 | 0 | 0 | 0 | 79.9% |
| test/built-ins/Date | 569 | 25 | 0 | 0 | 0 | 95.8% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 52 | 41 | 0 | 0 | 0 | 55.9% |
| test/built-ins/FinalizationRegistry | 45 | 2 | 0 | 0 | 0 | 95.7% |
| test/built-ins/Function | 223 | 198 | 0 | 0 | 88 | 53.0% |
| test/built-ins/GeneratorFunction | 8 | 15 | 0 | 0 | 0 | 34.8% |
| test/built-ins/GeneratorPrototype | 15 | 45 | 0 | 1 | 0 | 24.6% |
| test/built-ins/Infinity | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/Iterator | 362 | 152 | 0 | 0 | 0 | 70.4% |
| test/built-ins/JSON | 82 | 83 | 0 | 0 | 0 | 49.7% |
| test/built-ins/Map | 150 | 51 | 0 | 2 | 1 | 73.9% |
| test/built-ins/MapIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/Math | 327 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/NaN | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/NativeErrors | 76 | 18 | 0 | 0 | 0 | 80.9% |
| test/built-ins/Number | 276 | 64 | 0 | 0 | 0 | 81.2% |
| test/built-ins/Object | 3009 | 391 | 0 | 0 | 11 | 88.5% |
| test/built-ins/Promise | 261 | 463 | 0 | 2 | 3 | 36.0% |
| test/built-ins/Proxy | 148 | 152 | 0 | 0 | 11 | 49.3% |
| test/built-ins/Reflect | 123 | 30 | 0 | 0 | 0 | 80.4% |
| test/built-ins/RegExp | 1766 | 112 | 0 | 0 | 1 | 94.0% |
| test/built-ins/RegExpStringIteratorPrototype | 16 | 1 | 0 | 0 | 0 | 94.1% |
| test/built-ins/Set | 220 | 162 | 0 | 0 | 1 | 57.6% |
| test/built-ins/SetIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 73 | 31 | 0 | 0 | 0 | 70.2% |
| test/built-ins/String | 1187 | 33 | 0 | 0 | 3 | 97.3% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 0 | 22 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Symbol | 71 | 25 | 0 | 0 | 2 | 74.0% |
| test/built-ins/Temporal | 4579 | 24 | 0 | 0 | 0 | 99.5% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 1209 | 229 | 0 | 0 | 8 | 84.1% |
| test/built-ins/TypedArrayConstructors | 655 | 67 | 0 | 0 | 16 | 90.7% |
| test/built-ins/Uint8Array | 8 | 62 | 0 | 0 | 0 | 11.4% |
| test/built-ins/WeakMap | 111 | 29 | 0 | 1 | 0 | 78.7% |
| test/built-ins/WeakRef | 27 | 2 | 0 | 0 | 0 | 93.1% |
| test/built-ins/WeakSet | 82 | 3 | 0 | 0 | 0 | 96.5% |
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
| test/language/arguments-object | 189 | 17 | 0 | 0 | 57 | 91.7% |
| test/language/asi | 101 | 1 | 0 | 0 | 0 | 99.0% |
| test/language/block-scope | 145 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/comments | 46 | 6 | 0 | 0 | 0 | 88.5% |
| test/language/computed-property-names | 47 | 1 | 0 | 0 | 0 | 97.9% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 96 | 31 | 0 | 0 | 220 | 75.6% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 7922 | 2586 | 0 | 6 | 588 | 75.3% |
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
| test/language/statements | 7042 | 1820 | 0 | 3 | 472 | 79.4% |
| test/language/types | 101 | 3 | 0 | 0 | 9 | 97.1% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top FAIL causes (normalized message)

- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - e.g.: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **530x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/arguments-object/10.6-13-c-1-s.js`
- **516x** `SyntaxError: UnexpectedToken`
  - e.g.: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **470x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/expressions/assignment/dstr/array-empty-iter-close-err.js`
- **403x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - e.g.: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-id-iter-val-array-prototype.js`
- **228x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: TypeError Expected SameValue(«[object Functio`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-not-callable-boolean-throw.js`
- **218x** `async incomplete: `
  - e.g.: `test/language/expressions/async-generator/expression-yield-star-before-newline.js`
- **196x** `SyntaxError: MissingSemicolon`
  - e.g.: `test/language/asi/do-while-same-line.js`
- **184x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«N», «N») to be true`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-null-sync-get-abrupt.js`
- **182x** `Uncaught { message: Expected SameValue(«[object Function]», «N») to be true }`
  - e.g.: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **172x** `Uncaught TypeError: createRealm is not a function`
  - e.g.: `test/language/eval-code/indirect/realm.js`
- **168x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/language/arguments-object/10.6-13-c-3-s.js`
- **153x** `Uncaught TypeError: resize is not a function`
  - e.g.: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **142x** `Uncaught { message: Expected a ReferenceError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/expressions/arrow-function/dflt-params-ref-self.js`
- **135x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - e.g.: `test/language/expressions/object/method-definition/generator-prototype-prop.js`
- **132x** `Uncaught RangeError: Maximum call stack size exceeded`
  - e.g.: `test/language/expressions/tco-pos.js`
- **114x** `async incomplete: Out of memory: OutOfMemory`
  - e.g.: `test/language/expressions/async-generator/dstr/ary-init-iter-close.js`
- **111x** `Out of memory: OutOfMemory`
  - e.g.: `test/language/expressions/arrow-function/dstr/ary-init-iter-close.js`
- **110x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - e.g.: `test/language/eval-code/indirect/var-env-func-non-strict.js`
- **97x** `Uncaught { message: Expected SameValue(«undefined», «N») to be true }`
  - e.g.: `test/language/expressions/array/spread-obj-mult-spread-getter.js`
- **96x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: reject reason Expected SameValue(«TestNError:`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-get-abrupt.js`
- **87x** `Uncaught ReferenceError: DisposableStack is not defined`
  - e.g.: `test/built-ins/DisposableStack/instance-extensible.js`
- **84x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: it should not get Symbol.iterator`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-next-then-non-callable-boolean-fulfillpromise.js`
- **81x** `Uncaught { message: testResult !== true }`
  - e.g.: `test/built-ins/Array/prototype/forEach/15.4.4.18-3-16.js`
- **77x** `Uncaught { message: N descriptor should be configurable }`
  - e.g.: `test/language/arguments-object/10.6-11-b-1.js`
- **76x** `Uncaught { message: implements ArrayBuffer.prototype.resize Expected SameValue(«"undefined"», «"function"») to`
  - e.g.: `test/built-ins/DataView/prototype/getBigInt64/resizable-buffer.js`
- **70x** `Uncaught ReferenceError: AsyncDisposableStack is not defined`
  - e.g.: `test/built-ins/AsyncDisposableStack/instance-extensible.js`
- **61x** `async incomplete: Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/built-ins/AsyncGeneratorFunction/invoked-as-constructor-no-arguments.js`
- **58x** `Uncaught { message: Expected a TestNError but got a TypeError }`
  - e.g.: `test/language/expressions/assignment/dstr/array-elem-trlg-iter-rest-rtrn-close-err.js`
- **57x** `Uncaught ReferenceError: ShadowRealm is not defined`
  - e.g.: `test/built-ins/ShadowRealm/extensibility.js`

## Top features present in FAILs

- 1492x async-iteration
- 1210x generators
- 1125x Symbol.iterator
- 1065x class
- 1061x destructuring-binding
- 680x class-fields-public
- 604x dynamic-import
- 500x Symbol.asyncIterator
- 453x TypedArray
- 439x class-methods-private
- 436x default-parameters
- 402x resizable-arraybuffer
- 395x class-fields-private
- 350x explicit-resource-management
- 347x class-static-methods-private
- 274x Proxy
- 258x top-level-await
- 228x Symbol
- 193x arrow-function
- 188x BigInt
- 188x Reflect
- 185x SharedArrayBuffer
- 177x Atomics
- 175x cross-realm
- 158x async-functions
