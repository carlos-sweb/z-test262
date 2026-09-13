# Test262 — reporte de divergencias del motor z-*

Total: 47381 tests | corridos: 45639 | **PASS: 27480 (60.2% de los corridos)** | FAIL: 17439 | CRASH: 74 | TIMEOUT: 646 | SKIP (by design): 1742


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 0 | 25 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Array | 1007 | 2010 | 22 | 6 | 36 | 33.1% |
| test/built-ins/ArrayBuffer | 30 | 191 | 0 | 0 | 0 | 13.6% |
| test/built-ins/ArrayIteratorPrototype | 10 | 9 | 0 | 0 | 8 | 52.6% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 6 | 11 | 0 | 21 | 0 | 15.8% |
| test/built-ins/AsyncFunction | 9 | 9 | 0 | 0 | 0 | 50.0% |
| test/built-ins/AsyncGeneratorFunction | 8 | 15 | 0 | 0 | 0 | 34.8% |
| test/built-ins/AsyncGeneratorPrototype | 2 | 45 | 0 | 1 | 0 | 4.2% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 0 | 387 | 0 | 0 | 2 | 0.0% |
| test/built-ins/BigInt | 63 | 14 | 0 | 0 | 0 | 81.8% |
| test/built-ins/Boolean | 46 | 5 | 0 | 0 | 0 | 90.2% |
| test/built-ins/DataView | 343 | 218 | 0 | 0 | 0 | 61.1% |
| test/built-ins/Date | 521 | 73 | 0 | 0 | 0 | 87.7% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 28 | 65 | 0 | 0 | 0 | 30.1% |
| test/built-ins/FinalizationRegistry | 0 | 47 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Function | 202 | 219 | 0 | 0 | 88 | 48.0% |
| test/built-ins/GeneratorFunction | 8 | 15 | 0 | 0 | 0 | 34.8% |
| test/built-ins/GeneratorPrototype | 15 | 45 | 0 | 1 | 0 | 24.6% |
| test/built-ins/Infinity | 3 | 1 | 0 | 0 | 2 | 75.0% |
| test/built-ins/Iterator | 7 | 507 | 0 | 0 | 0 | 1.4% |
| test/built-ins/JSON | 81 | 84 | 0 | 0 | 0 | 49.1% |
| test/built-ins/Map | 129 | 69 | 0 | 5 | 1 | 63.5% |
| test/built-ins/MapIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/Math | 326 | 1 | 0 | 0 | 0 | 99.7% |
| test/built-ins/NaN | 3 | 1 | 0 | 0 | 2 | 75.0% |
| test/built-ins/NativeErrors | 44 | 50 | 0 | 0 | 0 | 46.8% |
| test/built-ins/Number | 262 | 78 | 0 | 0 | 0 | 77.1% |
| test/built-ins/Object | 2273 | 1111 | 16 | 0 | 11 | 66.9% |
| test/built-ins/Promise | 201 | 525 | 0 | 0 | 3 | 27.7% |
| test/built-ins/Proxy | 82 | 218 | 0 | 0 | 11 | 27.3% |
| test/built-ins/Reflect | 109 | 44 | 0 | 0 | 0 | 71.2% |
| test/built-ins/RegExp | 836 | 641 | 0 | 401 | 1 | 44.5% |
| test/built-ins/RegExpStringIteratorPrototype | 0 | 17 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Set | 205 | 176 | 0 | 1 | 1 | 53.7% |
| test/built-ins/SetIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/String | 953 | 267 | 0 | 0 | 3 | 78.1% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 0 | 22 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Symbol | 63 | 33 | 0 | 0 | 2 | 65.6% |
| test/built-ins/Temporal | 1570 | 3033 | 0 | 0 | 0 | 34.1% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 468 | 969 | 0 | 1 | 8 | 32.5% |
| test/built-ins/TypedArrayConstructors | 296 | 426 | 0 | 0 | 16 | 41.0% |
| test/built-ins/Uint8Array | 6 | 64 | 0 | 0 | 0 | 8.6% |
| test/built-ins/WeakMap | 0 | 141 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakRef | 0 | 29 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakSet | 0 | 85 | 0 | 0 | 0 | 0.0% |
| test/built-ins/decodeURI | 44 | 0 | 0 | 11 | 0 | 80.0% |
| test/built-ins/decodeURIComponent | 45 | 0 | 0 | 11 | 0 | 80.4% |
| test/built-ins/encodeURI | 22 | 5 | 0 | 4 | 0 | 71.0% |
| test/built-ins/encodeURIComponent | 22 | 5 | 0 | 4 | 0 | 71.0% |
| test/built-ins/eval | 10 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/global | 27 | 2 | 0 | 0 | 0 | 93.1% |
| test/built-ins/isFinite | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/isNaN | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/parseFloat | 49 | 4 | 0 | 1 | 0 | 90.7% |
| test/built-ins/parseInt | 48 | 6 | 0 | 1 | 0 | 87.3% |
| test/built-ins/undefined | 3 | 2 | 0 | 0 | 3 | 60.0% |
| test/language/arguments-object | 189 | 15 | 2 | 0 | 57 | 91.7% |
| test/language/asi | 101 | 1 | 0 | 0 | 0 | 99.0% |
| test/language/block-scope | 145 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/comments | 45 | 6 | 0 | 1 | 0 | 86.5% |
| test/language/computed-property-names | 46 | 2 | 0 | 0 | 0 | 95.8% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 96 | 31 | 0 | 0 | 220 | 75.6% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 7874 | 2537 | 17 | 86 | 588 | 74.9% |
| test/language/function-code | 100 | 8 | 0 | 0 | 109 | 92.6% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 20 | 17 | 0 | 0 | 5 | 54.1% |
| test/language/identifier-resolution | 8 | 1 | 0 | 0 | 5 | 88.9% |
| test/language/identifiers | 246 | 4 | 0 | 18 | 0 | 91.8% |
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
| test/language/statements | 6936 | 1844 | 17 | 68 | 472 | 78.2% |
| test/language/types | 101 | 3 | 0 | 0 | 9 | 97.1% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top causas de FAIL (mensaje normalizado)

- **1075x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/arguments-object/10.6-13-c-3-s.js`
- **683x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - ej: `test/language/arguments-object/10.6-13-c-1-s.js`
- **640x** `Uncaught TypeError: expression is not a constructor`
  - ej: `test/built-ins/Temporal/Duration/compare/blank-duration.js`
- **572x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/comments/hashbang/use-strict.js`
- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **516x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **485x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - ej: `test/language/expressions/assignment/dstr/array-empty-iter-close-err.js`
- **329x** `Uncaught ReferenceError: Iterator is not defined`
  - ej: `test/built-ins/Iterator/length.js`
- **323x** `Uncaught ReferenceError: $N is not defined`
  - ej: `test/language/eval-code/indirect/realm.js`
- **308x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - ej: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-id-iter-val-array-prototype.js`
- **261x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - ej: `test/language/expressions/object/method-definition/generator-prototype-prop.js`
- **260x** `Uncaught ReferenceError: SharedArrayBuffer is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-SharedArrayBuffer.js`
- **209x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-generator/expression-yield-star-before-newline.js`
- **196x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **182x** `Uncaught { message: Expected SameValue(«[object Function]», «N») to be true }
error(DebugAllocator): memory ad`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **173x** `Uncaught { message: Expected a TypeError but got a ReferenceError }`
  - ej: `test/language/global-code/script-decl-func-err-non-extensible.js`
- **165x** `Uncaught { message: Expected a ReferenceError to be thrown but no exception was thrown at all }`
  - ej: `test/language/expressions/arrow-function/lexical-super-call-from-within-constructor.js`
- **152x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: TypeError Expected SameValue(«[object Functio`
  - ej: `test/language/expressions/async-generator/named-yield-star-getiter-async-not-callable-boolean-throw.js`
- **144x** `Uncaught { message: Expected a TestNError but got a TypeError }`
  - ej: `test/language/expressions/instanceof/symbol-hasinstance-get-err.js`
- **132x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«N», «N») to be true`
  - ej: `test/language/expressions/async-function/named-strict-error-reassign-fn-name-in-body-in-arrow.js`
- **128x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - ej: `test/language/eval-code/indirect/var-env-func-non-strict.js`
- **122x** `Uncaught TypeError: Object.defineProperty called on non-object`
  - ej: `test/built-ins/Array/prototype/methods-called-as-functions.js`
- **119x** `Uncaught TypeError: Property description must be an object`
  - ej: `test/built-ins/Object/create/15.2.3.5-4-10.js`
- **111x** `Uncaught TypeError: Array.prototype.reduce called on a non-array`
  - ej: `test/built-ins/Array/prototype/reduce/15.4.4.21-1-10.js`
- **109x** `Uncaught TypeError: Array.prototype.reduceRight called on a non-array`
  - ej: `test/built-ins/Array/prototype/reduceRight/15.4.4.22-2-12.js`
- **99x** `Uncaught { message: Expected a RangeError but got a TypeError }`
  - ej: `test/built-ins/Array/prototype/every/15.4.4.16-7-c-i-30.js`
- **95x** `Uncaught ReferenceError: Atomics is not defined`
  - ej: `test/built-ins/Atomics/Symbol.toStringTag.js`
- **93x** `Uncaught ReferenceError: WeakMap is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-WeakMap.js`
- **92x** `Uncaught TypeError: expression is not a function`
  - ej: `test/built-ins/Function/prototype/Symbol.hasInstance/this-val-bound-target.js`
- **89x** `Uncaught TypeError: Array.prototype.filter called on a non-array`
  - ej: `test/built-ins/Array/prototype/filter/15.4.4.20-1-9.js`

## Top features presentes en FAILs

- 3041x Temporal
- 1699x TypedArray
- 1419x async-iteration
- 1164x generators
- 1026x class
- 1022x Symbol.iterator
- 1000x destructuring-binding
- 761x BigInt
- 744x Symbol
- 653x class-fields-public
- 604x dynamic-import
- 489x Symbol.asyncIterator
- 459x SharedArrayBuffer
- 455x resizable-arraybuffer
- 433x class-methods-private
- 422x arrow-function
- 413x default-parameters
- 397x class-fields-private
- 386x iterator-helpers
- 382x Atomics
- 364x Proxy
- 350x explicit-resource-management
- 324x Reflect
- 297x class-static-methods-private
- 271x Symbol.species

## CRASHES (los más graves)

- **72x** `exit -N: `
  - ej: `test/language/arguments-object/10.6-6-2.js`
- **2x** `exit -N: thread N panic: index out of bounds: index N, len N
/home/sweb/z-interpreter/src/array_builtins.zig:N`
  - ej: `test/built-ins/Array/prototype/copyWithin/coerced-values-start-change-start.js`
