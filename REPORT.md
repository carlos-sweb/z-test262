# Test262 — z-* engine divergence report

Total: 47381 tests | ran: 45639 | **PASS: 35010 (76.7% of those ran)** | FAIL: 10620 | CRASH: 0 | TIMEOUT: 9 | SKIP (by design): 1742


## Pass rate by area

| area | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 22 | 3 | 0 | 0 | 0 | 88.0% |
| test/built-ins/Array | 2083 | 962 | 0 | 0 | 36 | 68.4% |
| test/built-ins/ArrayBuffer | 73 | 148 | 0 | 0 | 0 | 33.0% |
| test/built-ins/ArrayIteratorPrototype | 10 | 9 | 0 | 0 | 8 | 52.6% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 6 | 31 | 0 | 1 | 0 | 15.8% |
| test/built-ins/AsyncFunction | 9 | 9 | 0 | 0 | 0 | 50.0% |
| test/built-ins/AsyncGeneratorFunction | 8 | 15 | 0 | 0 | 0 | 34.8% |
| test/built-ins/AsyncGeneratorPrototype | 2 | 45 | 0 | 1 | 0 | 4.2% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 207 | 180 | 0 | 0 | 2 | 53.5% |
| test/built-ins/BigInt | 70 | 7 | 0 | 0 | 0 | 90.9% |
| test/built-ins/Boolean | 47 | 4 | 0 | 0 | 0 | 92.2% |
| test/built-ins/DataView | 400 | 161 | 0 | 0 | 0 | 71.3% |
| test/built-ins/Date | 569 | 25 | 0 | 0 | 0 | 95.8% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 33 | 60 | 0 | 0 | 0 | 35.5% |
| test/built-ins/FinalizationRegistry | 44 | 3 | 0 | 0 | 0 | 93.6% |
| test/built-ins/Function | 218 | 203 | 0 | 0 | 88 | 51.8% |
| test/built-ins/GeneratorFunction | 8 | 15 | 0 | 0 | 0 | 34.8% |
| test/built-ins/GeneratorPrototype | 15 | 45 | 0 | 1 | 0 | 24.6% |
| test/built-ins/Infinity | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/Iterator | 362 | 152 | 0 | 0 | 0 | 70.4% |
| test/built-ins/JSON | 82 | 83 | 0 | 0 | 0 | 49.7% |
| test/built-ins/Map | 150 | 51 | 0 | 2 | 1 | 73.9% |
| test/built-ins/MapIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/Math | 327 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/NaN | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/NativeErrors | 68 | 26 | 0 | 0 | 0 | 72.3% |
| test/built-ins/Number | 276 | 64 | 0 | 0 | 0 | 81.2% |
| test/built-ins/Object | 2973 | 427 | 0 | 0 | 11 | 87.4% |
| test/built-ins/Promise | 261 | 465 | 0 | 0 | 3 | 36.0% |
| test/built-ins/Proxy | 139 | 161 | 0 | 0 | 11 | 46.3% |
| test/built-ins/Reflect | 123 | 30 | 0 | 0 | 0 | 80.4% |
| test/built-ins/RegExp | 1766 | 112 | 0 | 0 | 1 | 94.0% |
| test/built-ins/RegExpStringIteratorPrototype | 16 | 1 | 0 | 0 | 0 | 94.1% |
| test/built-ins/Set | 220 | 162 | 0 | 0 | 1 | 57.6% |
| test/built-ins/SetIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 57 | 47 | 0 | 0 | 0 | 54.8% |
| test/built-ins/String | 1187 | 33 | 0 | 0 | 3 | 97.3% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 0 | 22 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Symbol | 71 | 25 | 0 | 0 | 2 | 74.0% |
| test/built-ins/Temporal | 4579 | 24 | 0 | 0 | 0 | 99.5% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 480 | 958 | 0 | 0 | 8 | 33.4% |
| test/built-ins/TypedArrayConstructors | 392 | 330 | 0 | 0 | 16 | 54.3% |
| test/built-ins/Uint8Array | 6 | 64 | 0 | 0 | 0 | 8.6% |
| test/built-ins/WeakMap | 111 | 29 | 0 | 1 | 0 | 78.7% |
| test/built-ins/WeakRef | 26 | 3 | 0 | 0 | 0 | 89.7% |
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
| test/language/expressions | 7911 | 2602 | 0 | 1 | 588 | 75.2% |
| test/language/function-code | 100 | 8 | 0 | 0 | 109 | 92.6% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 21 | 16 | 0 | 0 | 5 | 56.8% |
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
| test/language/statements | 6971 | 1894 | 0 | 0 | 472 | 78.6% |
| test/language/types | 101 | 3 | 0 | 0 | 9 | 97.1% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top FAIL causes (normalized message)

- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - e.g.: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **539x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/arguments-object/10.6-13-c-1-s.js`
- **516x** `SyntaxError: UnexpectedToken`
  - e.g.: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **472x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/expressions/assignment/dstr/array-empty-iter-close-err.js`
- **405x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - e.g.: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-id-iter-val-array-prototype.js`
- **386x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/language/arguments-object/10.6-13-c-3-s.js`
- **335x** `Uncaught ReferenceError: $N is not defined`
  - e.g.: `test/language/eval-code/indirect/realm.js`
- **228x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: TypeError Expected SameValue(«[object Functio`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-not-callable-boolean-throw.js`
- **219x** `async incomplete: `
  - e.g.: `test/language/expressions/async-generator/expression-yield-star-before-newline.js`
- **202x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - e.g.: `test/language/expressions/object/method-definition/generator-prototype-prop.js`
- **196x** `SyntaxError: MissingSemicolon`
  - e.g.: `test/language/asi/do-while-same-line.js`
- **186x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«N», «N») to be true`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-null-sync-get-abrupt.js`
- **182x** `Uncaught { message: Expected SameValue(«[object Function]», «N») to be true }`
  - e.g.: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **168x** `Uncaught { message: Expected a ReferenceError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/expressions/arrow-function/dflt-params-ref-self.js`
- **132x** `Uncaught RangeError: Maximum call stack size exceeded`
  - e.g.: `test/language/expressions/tco-pos.js`
- **121x** `Uncaught TypeError: resize is not a function`
  - e.g.: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **119x** `Out of memory: OutOfMemory`
  - e.g.: `test/language/expressions/arrow-function/dstr/ary-init-iter-close.js`
- **118x** `async incomplete: Out of memory: OutOfMemory`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-sync-return.js`
- **116x** `Uncaught TypeError: Setting a function's prototype to a non-object is not supported yet`
  - e.g.: `test/language/expressions/async-generator/default-proto.js`
- **105x** `Uncaught TypeError: Cannot set property constructor of a typed array: named properties are not supported yet (`
  - e.g.: `test/built-ins/TypedArray/prototype/filter/callbackfn-called-before-ctor.js`
- **102x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - e.g.: `test/language/eval-code/indirect/var-env-func-non-strict.js`
- **97x** `Uncaught { message: Expected SameValue(«undefined», «N») to be true }`
  - e.g.: `test/language/expressions/array/spread-obj-mult-spread-getter.js`
- **96x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: reject reason Expected SameValue(«TestNError:`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-get-abrupt.js`
- **86x** `Uncaught ReferenceError: DisposableStack is not defined`
  - e.g.: `test/built-ins/DisposableStack/instance-extensible.js`
- **84x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: it should not get Symbol.iterator`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-next-then-non-callable-boolean-fulfillpromise.js`
- **81x** `Uncaught { message: testResult !== true }`
  - e.g.: `test/built-ins/Array/prototype/forEach/15.4.4.18-3-16.js`
- **77x** `Uncaught { message: N descriptor should be configurable }`
  - e.g.: `test/language/arguments-object/10.6-11-b-1.js`
- **69x** `Uncaught ReferenceError: AsyncDisposableStack is not defined`
  - e.g.: `test/built-ins/AsyncDisposableStack/instance-extensible.js`
- **65x** `Uncaught ReferenceError: $N is not defined (Testing with FloatNArray and makePassthrough.)`
  - e.g.: `test/built-ins/TypedArray/prototype/Symbol.toStringTag/detached-buffer.js`
- **62x** `Uncaught ReferenceError: $N is not defined (Testing with BigIntNArray and makePassthrough.)`
  - e.g.: `test/built-ins/TypedArray/prototype/Symbol.toStringTag/BigInt/detached-buffer.js`

## Top features present in FAILs

- 1501x async-iteration
- 1433x TypedArray
- 1222x generators
- 1160x Symbol.iterator
- 1078x class
- 1069x destructuring-binding
- 683x class-fields-public
- 604x dynamic-import
- 518x BigInt
- 501x Symbol.asyncIterator
- 449x class-methods-private
- 436x default-parameters
- 415x resizable-arraybuffer
- 397x class-fields-private
- 350x explicit-resource-management
- 347x class-static-methods-private
- 330x Symbol
- 289x Proxy
- 258x top-level-await
- 256x Reflect
- 227x arrow-function
- 216x SharedArrayBuffer
- 213x Symbol.species
- 180x Atomics
- 175x cross-realm
