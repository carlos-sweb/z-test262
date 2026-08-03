# Test262 — reporte de divergencias del motor z-*

Total: 47381 tests | corridos: 45639 | **PASS: 25493 (55.9% de los corridos)** | FAIL: 19476 | CRASH: 0 | TIMEOUT: 670 | SKIP (by design): 1742


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 0 | 25 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Array | 883 | 2139 | 0 | 23 | 36 | 29.0% |
| test/built-ins/ArrayBuffer | 23 | 198 | 0 | 0 | 0 | 10.4% |
| test/built-ins/ArrayIteratorPrototype | 10 | 9 | 0 | 0 | 8 | 52.6% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 6 | 11 | 0 | 21 | 0 | 15.8% |
| test/built-ins/AsyncFunction | 9 | 9 | 0 | 0 | 0 | 50.0% |
| test/built-ins/AsyncGeneratorFunction | 7 | 16 | 0 | 0 | 0 | 30.4% |
| test/built-ins/AsyncGeneratorPrototype | 2 | 45 | 0 | 1 | 0 | 4.2% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 0 | 387 | 0 | 0 | 2 | 0.0% |
| test/built-ins/BigInt | 43 | 34 | 0 | 0 | 0 | 55.8% |
| test/built-ins/Boolean | 44 | 7 | 0 | 0 | 0 | 86.3% |
| test/built-ins/DataView | 269 | 292 | 0 | 0 | 0 | 48.0% |
| test/built-ins/Date | 444 | 150 | 0 | 0 | 0 | 74.7% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 24 | 69 | 0 | 0 | 0 | 25.8% |
| test/built-ins/FinalizationRegistry | 0 | 47 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Function | 181 | 240 | 0 | 0 | 88 | 43.0% |
| test/built-ins/GeneratorFunction | 7 | 16 | 0 | 0 | 0 | 30.4% |
| test/built-ins/GeneratorPrototype | 15 | 45 | 0 | 1 | 0 | 24.6% |
| test/built-ins/Infinity | 3 | 1 | 0 | 0 | 2 | 75.0% |
| test/built-ins/Iterator | 7 | 507 | 0 | 0 | 0 | 1.4% |
| test/built-ins/JSON | 78 | 87 | 0 | 0 | 0 | 47.3% |
| test/built-ins/Map | 128 | 70 | 0 | 5 | 1 | 63.1% |
| test/built-ins/MapIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/Math | 306 | 21 | 0 | 0 | 0 | 93.6% |
| test/built-ins/NaN | 3 | 1 | 0 | 0 | 2 | 75.0% |
| test/built-ins/NativeErrors | 36 | 58 | 0 | 0 | 0 | 38.3% |
| test/built-ins/Number | 206 | 134 | 0 | 0 | 0 | 60.6% |
| test/built-ins/Object | 2103 | 1281 | 0 | 16 | 11 | 61.9% |
| test/built-ins/Promise | 198 | 528 | 0 | 0 | 3 | 27.3% |
| test/built-ins/Proxy | 81 | 219 | 0 | 0 | 11 | 27.0% |
| test/built-ins/Reflect | 102 | 51 | 0 | 0 | 0 | 66.7% |
| test/built-ins/RegExp | 589 | 899 | 0 | 390 | 1 | 31.4% |
| test/built-ins/RegExpStringIteratorPrototype | 0 | 17 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Set | 204 | 177 | 0 | 1 | 1 | 53.4% |
| test/built-ins/SetIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/String | 658 | 562 | 0 | 0 | 3 | 53.9% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 0 | 22 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Symbol | 57 | 39 | 0 | 0 | 2 | 59.4% |
| test/built-ins/Temporal | 1488 | 3115 | 0 | 0 | 0 | 32.3% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 395 | 1043 | 0 | 0 | 8 | 27.5% |
| test/built-ins/TypedArrayConstructors | 264 | 458 | 0 | 0 | 16 | 36.6% |
| test/built-ins/Uint8Array | 6 | 64 | 0 | 0 | 0 | 8.6% |
| test/built-ins/WeakMap | 0 | 141 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakRef | 0 | 29 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakSet | 0 | 85 | 0 | 0 | 0 | 0.0% |
| test/built-ins/decodeURI | 45 | 2 | 0 | 8 | 0 | 81.8% |
| test/built-ins/decodeURIComponent | 46 | 2 | 0 | 8 | 0 | 82.1% |
| test/built-ins/encodeURI | 21 | 9 | 0 | 1 | 0 | 67.7% |
| test/built-ins/encodeURIComponent | 21 | 9 | 0 | 1 | 0 | 67.7% |
| test/built-ins/eval | 9 | 1 | 0 | 0 | 0 | 90.0% |
| test/built-ins/global | 26 | 3 | 0 | 0 | 0 | 89.7% |
| test/built-ins/isFinite | 5 | 10 | 0 | 0 | 0 | 33.3% |
| test/built-ins/isNaN | 5 | 10 | 0 | 0 | 0 | 33.3% |
| test/built-ins/parseFloat | 45 | 9 | 0 | 0 | 0 | 83.3% |
| test/built-ins/parseInt | 40 | 15 | 0 | 0 | 0 | 72.7% |
| test/built-ins/undefined | 3 | 2 | 0 | 0 | 3 | 60.0% |
| test/language/arguments-object | 189 | 15 | 0 | 2 | 57 | 91.7% |
| test/language/asi | 98 | 4 | 0 | 0 | 0 | 96.1% |
| test/language/block-scope | 145 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/comments | 46 | 6 | 0 | 0 | 0 | 88.5% |
| test/language/computed-property-names | 42 | 6 | 0 | 0 | 0 | 87.5% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 96 | 31 | 0 | 0 | 220 | 75.6% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 7275 | 3136 | 0 | 103 | 588 | 69.2% |
| test/language/function-code | 100 | 8 | 0 | 0 | 109 | 92.6% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 20 | 17 | 0 | 0 | 5 | 54.1% |
| test/language/identifier-resolution | 8 | 1 | 0 | 0 | 5 | 88.9% |
| test/language/identifiers | 264 | 4 | 0 | 0 | 0 | 98.5% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 39 | 2 | 0 | 0 | 0 | 95.1% |
| test/language/literals | 497 | 19 | 0 | 4 | 14 | 95.6% |
| test/language/module-code | 216 | 383 | 0 | 0 | 0 | 36.1% |
| test/language/punctuators | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/reserved-words | 27 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/rest-parameters | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/source-text | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/statementList | 76 | 4 | 0 | 0 | 0 | 95.0% |
| test/language/statements | 6914 | 1866 | 0 | 85 | 472 | 78.0% |
| test/language/types | 93 | 11 | 0 | 0 | 9 | 89.4% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top causas de FAIL (mensaje normalizado)

- **2228x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/asi/S7.9_A10_T1.js`
- **1137x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/arguments-object/10.6-13-c-3-s.js`
- **704x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - ej: `test/language/eval-code/indirect/non-definable-global-function.js`
- **640x** `Uncaught TypeError: expression is not a constructor`
  - ej: `test/built-ins/Temporal/Duration/compare/blank-duration.js`
- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **516x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **470x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - ej: `test/language/expressions/assignment/dstr/array-empty-iter-close-err.js`
- **405x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - ej: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-id-iter-val-array-prototype.js`
- **333x** `Uncaught ReferenceError: Iterator is not defined`
  - ej: `test/built-ins/Iterator/length.js`
- **323x** `Uncaught ReferenceError: $N is not defined`
  - ej: `test/language/eval-code/indirect/realm.js`
- **285x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - ej: `test/language/expressions/object/method-definition/generator-prototype-prop.js`
- **278x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-generator/expression-yield-star-before-newline.js`
- **260x** `Uncaught ReferenceError: SharedArrayBuffer is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-SharedArrayBuffer.js`
- **228x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: TypeError Expected SameValue(«[object Functio`
  - ej: `test/language/expressions/async-generator/named-yield-star-getiter-async-not-callable-boolean-throw.js`
- **196x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **191x** `Uncaught RangeError: Invalid length: must be a non-negative safe integer`
  - ej: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **188x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«N», «N») to be true`
  - ej: `test/language/expressions/async-function/named-strict-error-reassign-fn-name-in-body-in-arrow.js`
- **182x** `Uncaught { message: Expected SameValue(«[object Function]», «N») to be true }`
  - ej: `test/language/expressions/class/elements/after-same-line-static-method-rs-static-privatename-identifier-initializer-alt.js`
- **176x** `Uncaught { message: Expected a TestNError but got a TypeError }`
  - ej: `test/language/expressions/assignment/dstr/array-elem-trlg-iter-rest-rtrn-close-err.js`
- **172x** `Uncaught { message: Expected a TypeError but got a ReferenceError }`
  - ej: `test/language/global-code/script-decl-func-err-non-extensible.js`
- **166x** `Uncaught { message: Expected a ReferenceError to be thrown but no exception was thrown at all }`
  - ej: `test/language/expressions/arrow-function/dflt-params-ref-self.js`
- **132x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - ej: `test/language/eval-code/indirect/var-env-func-non-strict.js`
- **132x** `Uncaught RangeError: Maximum call stack size exceeded`
  - ej: `test/language/expressions/tco-pos.js`
- **123x** `Uncaught TypeError: Object.defineProperty called on non-object`
  - ej: `test/built-ins/Array/prototype/methods-called-as-functions.js`
- **113x** `Uncaught { message: Built-in objects must be extensible. Expected SameValue(«false», «true») to be true }`
  - ej: `test/built-ins/Set/prototype/difference/builtins.js`
- **112x** `Uncaught { message: Expected SameValue(«undefined», «N») to be true }`
  - ej: `test/language/expressions/array/spread-obj-mult-spread-getter.js`
- **111x** `Uncaught TypeError: Array.prototype.reduce called on a non-array`
  - ej: `test/built-ins/Array/prototype/reduce/15.4.4.21-1-10.js`
- **109x** `Uncaught TypeError: Array.prototype.reduceRight called on a non-array`
  - ej: `test/built-ins/Array/prototype/reduceRight/15.4.4.22-2-12.js`
- **102x** `Uncaught { message: Expected a RangeError but got a TypeError }`
  - ej: `test/built-ins/Array/prototype/indexOf/15.4.4.14-5-29.js`
- **96x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: reject reason Expected SameValue(«TestNError:`
  - ej: `test/language/expressions/async-generator/named-yield-star-getiter-async-get-abrupt.js`

## Top features presentes en FAILs

- 3123x Temporal
- 1800x TypedArray
- 1420x async-iteration
- 1165x generators
- 1045x class
- 1022x Symbol.iterator
- 1000x destructuring-binding
- 889x BigInt
- 837x Symbol
- 679x class-fields-public
- 604x dynamic-import
- 489x Symbol.asyncIterator
- 459x resizable-arraybuffer
- 459x SharedArrayBuffer
- 433x class-methods-private
- 427x arrow-function
- 413x default-parameters
- 409x class-fields-private
- 386x iterator-helpers
- 382x Atomics
- 364x Proxy
- 350x explicit-resource-management
- 331x Reflect
- 297x class-static-methods-private
- 281x Symbol.species
