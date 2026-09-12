# Test262 — reporte de divergencias del motor z-*

Total: 47381 tests | corridos: 45639 | **PASS: 26999 (59.2% de los corridos)** | FAIL: 17978 | CRASH: 0 | TIMEOUT: 662 | SKIP (by design): 1742


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 0 | 25 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Array | 915 | 2110 | 0 | 20 | 36 | 30.0% |
| test/built-ins/ArrayBuffer | 29 | 192 | 0 | 0 | 0 | 13.1% |
| test/built-ins/ArrayIteratorPrototype | 10 | 9 | 0 | 0 | 8 | 52.6% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 6 | 11 | 0 | 21 | 0 | 15.8% |
| test/built-ins/AsyncFunction | 9 | 9 | 0 | 0 | 0 | 50.0% |
| test/built-ins/AsyncGeneratorFunction | 7 | 16 | 0 | 0 | 0 | 30.4% |
| test/built-ins/AsyncGeneratorPrototype | 2 | 45 | 0 | 1 | 0 | 4.2% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 0 | 387 | 0 | 0 | 2 | 0.0% |
| test/built-ins/BigInt | 63 | 14 | 0 | 0 | 0 | 81.8% |
| test/built-ins/Boolean | 46 | 5 | 0 | 0 | 0 | 90.2% |
| test/built-ins/DataView | 342 | 219 | 0 | 0 | 0 | 61.0% |
| test/built-ins/Date | 520 | 74 | 0 | 0 | 0 | 87.5% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 28 | 65 | 0 | 0 | 0 | 30.1% |
| test/built-ins/FinalizationRegistry | 0 | 47 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Function | 200 | 221 | 0 | 0 | 88 | 47.5% |
| test/built-ins/GeneratorFunction | 7 | 16 | 0 | 0 | 0 | 30.4% |
| test/built-ins/GeneratorPrototype | 15 | 45 | 0 | 1 | 0 | 24.6% |
| test/built-ins/Infinity | 3 | 1 | 0 | 0 | 2 | 75.0% |
| test/built-ins/Iterator | 7 | 507 | 0 | 0 | 0 | 1.4% |
| test/built-ins/JSON | 79 | 86 | 0 | 0 | 0 | 47.9% |
| test/built-ins/Map | 129 | 69 | 0 | 5 | 1 | 63.5% |
| test/built-ins/MapIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/Math | 326 | 1 | 0 | 0 | 0 | 99.7% |
| test/built-ins/NaN | 3 | 1 | 0 | 0 | 2 | 75.0% |
| test/built-ins/NativeErrors | 44 | 50 | 0 | 0 | 0 | 46.8% |
| test/built-ins/Number | 262 | 78 | 0 | 0 | 0 | 77.1% |
| test/built-ins/Object | 2169 | 1215 | 0 | 16 | 11 | 63.8% |
| test/built-ins/Promise | 199 | 527 | 0 | 0 | 3 | 27.4% |
| test/built-ins/Proxy | 82 | 218 | 0 | 0 | 11 | 27.3% |
| test/built-ins/Reflect | 109 | 44 | 0 | 0 | 0 | 71.2% |
| test/built-ins/RegExp | 617 | 872 | 0 | 389 | 1 | 32.9% |
| test/built-ins/RegExpStringIteratorPrototype | 0 | 17 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Set | 205 | 176 | 0 | 1 | 1 | 53.7% |
| test/built-ins/SetIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/String | 948 | 272 | 0 | 0 | 3 | 77.7% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 0 | 22 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Symbol | 63 | 33 | 0 | 0 | 2 | 65.6% |
| test/built-ins/Temporal | 1489 | 3114 | 0 | 0 | 0 | 32.3% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 469 | 969 | 0 | 0 | 8 | 32.6% |
| test/built-ins/TypedArrayConstructors | 296 | 426 | 0 | 0 | 16 | 41.0% |
| test/built-ins/Uint8Array | 6 | 64 | 0 | 0 | 0 | 8.6% |
| test/built-ins/WeakMap | 0 | 141 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakRef | 0 | 29 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakSet | 0 | 85 | 0 | 0 | 0 | 0.0% |
| test/built-ins/decodeURI | 48 | 0 | 0 | 7 | 0 | 87.3% |
| test/built-ins/decodeURIComponent | 49 | 0 | 0 | 7 | 0 | 87.5% |
| test/built-ins/encodeURI | 24 | 7 | 0 | 0 | 0 | 77.4% |
| test/built-ins/encodeURIComponent | 24 | 7 | 0 | 0 | 0 | 77.4% |
| test/built-ins/eval | 10 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/global | 27 | 2 | 0 | 0 | 0 | 93.1% |
| test/built-ins/isFinite | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/isNaN | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/parseFloat | 50 | 4 | 0 | 0 | 0 | 92.6% |
| test/built-ins/parseInt | 49 | 6 | 0 | 0 | 0 | 89.1% |
| test/built-ins/undefined | 3 | 2 | 0 | 0 | 3 | 60.0% |
| test/language/arguments-object | 189 | 15 | 0 | 2 | 57 | 91.7% |
| test/language/asi | 101 | 1 | 0 | 0 | 0 | 99.0% |
| test/language/block-scope | 145 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/comments | 46 | 6 | 0 | 0 | 0 | 88.5% |
| test/language/computed-property-names | 46 | 2 | 0 | 0 | 0 | 95.8% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 96 | 31 | 0 | 0 | 220 | 75.6% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 7871 | 2540 | 0 | 103 | 588 | 74.9% |
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
| test/language/statements | 6936 | 1844 | 0 | 85 | 472 | 78.2% |
| test/language/types | 101 | 3 | 0 | 0 | 9 | 97.1% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top causas de FAIL (mensaje normalizado)

- **1119x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/arguments-object/10.6-13-c-3-s.js`
- **1100x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/arguments-object/10.6-14-c-4-s.js`
- **689x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - ej: `test/language/arguments-object/10.6-13-c-1-s.js`
- **640x** `Uncaught TypeError: expression is not a constructor`
  - ej: `test/built-ins/Temporal/Duration/compare/blank-duration.js`
- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **516x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **477x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - ej: `test/language/expressions/assignment/dstr/array-elem-iter-nrml-close-err.js`
- **408x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - ej: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-ary-elision-init.js`
- **333x** `Uncaught ReferenceError: Iterator is not defined`
  - ej: `test/built-ins/Iterator/length.js`
- **323x** `Uncaught ReferenceError: $N is not defined`
  - ej: `test/language/eval-code/indirect/realm.js`
- **278x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-generator/expression-yield-star-before-newline.js`
- **275x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - ej: `test/language/expressions/object/method-definition/generator-prototype-prop.js`
- **260x** `Uncaught ReferenceError: SharedArrayBuffer is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-SharedArrayBuffer.js`
- **228x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: TypeError Expected SameValue(«[object Functio`
  - ej: `test/language/expressions/async-generator/named-yield-star-getiter-async-not-callable-boolean-throw.js`
- **196x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **188x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«N», «N») to be true`
  - ej: `test/language/expressions/async-function/named-strict-error-reassign-fn-name-in-body-in-arrow.js`
- **182x** `Uncaught { message: Expected SameValue(«[object Function]», «N») to be true }`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **175x** `Uncaught { message: Expected a TypeError but got a ReferenceError }`
  - ej: `test/language/global-code/script-decl-func-err-non-extensible.js`
- **166x** `Uncaught { message: Expected a ReferenceError to be thrown but no exception was thrown at all }`
  - ej: `test/language/expressions/arrow-function/dflt-params-ref-self.js`
- **146x** `Uncaught { message: Expected a TestNError but got a TypeError }`
  - ej: `test/language/expressions/assignment/dstr/array-elem-trlg-iter-rest-rtrn-close-err.js`
- **132x** `Uncaught RangeError: Maximum call stack size exceeded`
  - ej: `test/language/expressions/tco-pos.js`
- **128x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - ej: `test/language/eval-code/indirect/var-env-func-non-strict.js`
- **123x** `Uncaught TypeError: Object.defineProperty called on non-object`
  - ej: `test/built-ins/Array/prototype/methods-called-as-functions.js`
- **114x** `Uncaught TypeError: Array.prototype.reduce called on a non-array`
  - ej: `test/built-ins/Array/prototype/reduce/15.4.4.21-1-10.js`
- **113x** `Uncaught { message: Built-in objects must be extensible. Expected SameValue(«false», «true») to be true }`
  - ej: `test/built-ins/Set/prototype/difference/builtins.js`
- **112x** `Uncaught TypeError: Array.prototype.reduceRight called on a non-array`
  - ej: `test/built-ins/Array/prototype/reduceRight/15.4.4.22-1-10.js`
- **108x** `Uncaught { message: Expected SameValue(«undefined», «N») to be true }`
  - ej: `test/language/expressions/array/spread-obj-mult-spread-getter.js`
- **101x** `Uncaught { message: Expected a RangeError but got a TypeError }`
  - ej: `test/built-ins/Array/prototype/every/15.4.4.16-7-c-i-30.js`
- **96x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: reject reason Expected SameValue(«TestNError:`
  - ej: `test/language/expressions/async-generator/named-yield-star-getiter-async-get-abrupt.js`
- **95x** `Uncaught ReferenceError: Atomics is not defined`
  - ej: `test/built-ins/Atomics/Symbol.toStringTag.js`

## Top features presentes en FAILs

- 3122x Temporal
- 1699x TypedArray
- 1420x async-iteration
- 1165x generators
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
- 281x Symbol.species
