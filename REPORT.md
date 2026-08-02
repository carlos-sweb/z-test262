# Test262 — reporte de divergencias del motor z-*

Total: 47381 tests | corridos: 45639 | **PASS: 23057 (50.5% de los corridos)** | FAIL: 21943 | CRASH: 0 | TIMEOUT: 639 | SKIP (by design): 1742


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 0 | 25 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Array | 843 | 2176 | 0 | 26 | 36 | 27.7% |
| test/built-ins/ArrayBuffer | 22 | 199 | 0 | 0 | 0 | 10.0% |
| test/built-ins/ArrayIteratorPrototype | 10 | 9 | 0 | 0 | 8 | 52.6% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 4 | 21 | 0 | 13 | 0 | 10.5% |
| test/built-ins/AsyncFunction | 9 | 9 | 0 | 0 | 0 | 50.0% |
| test/built-ins/AsyncGeneratorFunction | 7 | 16 | 0 | 0 | 0 | 30.4% |
| test/built-ins/AsyncGeneratorPrototype | 1 | 46 | 0 | 1 | 0 | 2.1% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 0 | 387 | 0 | 0 | 2 | 0.0% |
| test/built-ins/BigInt | 38 | 39 | 0 | 0 | 0 | 49.4% |
| test/built-ins/Boolean | 38 | 13 | 0 | 0 | 0 | 74.5% |
| test/built-ins/DataView | 250 | 311 | 0 | 0 | 0 | 44.6% |
| test/built-ins/Date | 409 | 185 | 0 | 0 | 0 | 68.9% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 21 | 72 | 0 | 0 | 0 | 22.6% |
| test/built-ins/FinalizationRegistry | 0 | 47 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Function | 158 | 263 | 0 | 0 | 88 | 37.5% |
| test/built-ins/GeneratorFunction | 7 | 16 | 0 | 0 | 0 | 30.4% |
| test/built-ins/GeneratorPrototype | 14 | 46 | 0 | 1 | 0 | 23.0% |
| test/built-ins/Infinity | 2 | 2 | 0 | 0 | 2 | 50.0% |
| test/built-ins/Iterator | 7 | 507 | 0 | 0 | 0 | 1.4% |
| test/built-ins/JSON | 75 | 90 | 0 | 0 | 0 | 45.5% |
| test/built-ins/Map | 122 | 76 | 0 | 5 | 1 | 60.1% |
| test/built-ins/MapIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/Math | 106 | 221 | 0 | 0 | 0 | 32.4% |
| test/built-ins/NaN | 2 | 2 | 0 | 0 | 2 | 50.0% |
| test/built-ins/NativeErrors | 30 | 64 | 0 | 0 | 0 | 31.9% |
| test/built-ins/Number | 186 | 154 | 0 | 0 | 0 | 54.7% |
| test/built-ins/Object | 1980 | 1404 | 0 | 16 | 11 | 58.2% |
| test/built-ins/Promise | 185 | 541 | 0 | 0 | 3 | 25.5% |
| test/built-ins/Proxy | 81 | 219 | 0 | 0 | 11 | 27.0% |
| test/built-ins/Reflect | 90 | 63 | 0 | 0 | 0 | 58.8% |
| test/built-ins/RegExp | 580 | 905 | 0 | 393 | 1 | 30.9% |
| test/built-ins/RegExpStringIteratorPrototype | 0 | 17 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Set | 198 | 183 | 0 | 1 | 1 | 51.8% |
| test/built-ins/SetIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/String | 610 | 610 | 0 | 0 | 3 | 50.0% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 0 | 22 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Symbol | 42 | 54 | 0 | 0 | 2 | 43.8% |
| test/built-ins/Temporal | 1417 | 3186 | 0 | 0 | 0 | 30.8% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 395 | 1043 | 0 | 0 | 8 | 27.5% |
| test/built-ins/TypedArrayConstructors | 264 | 458 | 0 | 0 | 16 | 36.6% |
| test/built-ins/Uint8Array | 6 | 64 | 0 | 0 | 0 | 8.6% |
| test/built-ins/WeakMap | 0 | 141 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakRef | 0 | 29 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakSet | 0 | 85 | 0 | 0 | 0 | 0.0% |
| test/built-ins/decodeURI | 40 | 5 | 0 | 10 | 0 | 72.7% |
| test/built-ins/decodeURIComponent | 41 | 5 | 0 | 10 | 0 | 73.2% |
| test/built-ins/encodeURI | 18 | 12 | 0 | 1 | 0 | 58.1% |
| test/built-ins/encodeURIComponent | 18 | 12 | 0 | 1 | 0 | 58.1% |
| test/built-ins/eval | 7 | 3 | 0 | 0 | 0 | 70.0% |
| test/built-ins/global | 25 | 4 | 0 | 0 | 0 | 86.2% |
| test/built-ins/isFinite | 4 | 11 | 0 | 0 | 0 | 26.7% |
| test/built-ins/isNaN | 4 | 11 | 0 | 0 | 0 | 26.7% |
| test/built-ins/parseFloat | 42 | 11 | 0 | 1 | 0 | 77.8% |
| test/built-ins/parseInt | 39 | 16 | 0 | 0 | 0 | 70.9% |
| test/built-ins/undefined | 2 | 3 | 0 | 0 | 3 | 40.0% |
| test/language/arguments-object | 189 | 15 | 0 | 2 | 57 | 91.7% |
| test/language/asi | 98 | 4 | 0 | 0 | 0 | 96.1% |
| test/language/block-scope | 145 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/comments | 44 | 8 | 0 | 0 | 0 | 84.6% |
| test/language/computed-property-names | 28 | 20 | 0 | 0 | 0 | 58.3% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 95 | 32 | 0 | 0 | 220 | 74.8% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 6413 | 4015 | 0 | 86 | 588 | 61.0% |
| test/language/function-code | 99 | 9 | 0 | 0 | 109 | 91.7% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 19 | 18 | 0 | 0 | 5 | 51.4% |
| test/language/identifier-resolution | 6 | 3 | 0 | 0 | 5 | 66.7% |
| test/language/identifiers | 256 | 12 | 0 | 0 | 0 | 95.5% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 36 | 5 | 0 | 0 | 0 | 87.8% |
| test/language/literals | 497 | 19 | 0 | 4 | 14 | 95.6% |
| test/language/module-code | 217 | 382 | 0 | 0 | 0 | 36.2% |
| test/language/punctuators | 10 | 1 | 0 | 0 | 0 | 90.9% |
| test/language/reserved-words | 27 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/rest-parameters | 9 | 2 | 0 | 0 | 0 | 81.8% |
| test/language/source-text | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/language/statementList | 76 | 4 | 0 | 0 | 0 | 95.0% |
| test/language/statements | 6076 | 2721 | 0 | 68 | 472 | 68.5% |
| test/language/types | 88 | 16 | 0 | 0 | 9 | 84.6% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top causas de FAIL (mensaje normalizado)

- **2193x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/asi/S7.9_A10_T1.js`
- **1178x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/comments/S7.4_A1_T1.js`
- **717x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - ej: `test/language/computed-property-names/class/static/generator-prototype.js`
- **640x** `Uncaught TypeError: expression is not a constructor`
  - ej: `test/built-ins/Temporal/Duration/compare/blank-duration.js`
- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **518x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **472x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - ej: `test/language/expressions/assignment/dstr/array-empty-iter-close-err.js`
- **408x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - ej: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-id-iter-val-array-prototype.js`
- **397x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - ej: `test/language/eval-code/indirect/non-definable-function-with-function.js`
- **372x** `SyntaxError: InvalidUnicodeEscape`
  - ej: `test/language/expressions/class/decorator/syntax/class-valid/decorator-member-expr-private-identifier.js`
- **333x** `Uncaught ReferenceError: Iterator is not defined`
  - ej: `test/built-ins/Iterator/length.js`
- **322x** `Uncaught ReferenceError: $N is not defined`
  - ej: `test/language/eval-code/indirect/realm.js`
- **302x** `SyntaxError: UnexpectedCharacter`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **260x** `Uncaught ReferenceError: SharedArrayBuffer is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-SharedArrayBuffer.js`
- **228x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: TypeError Expected SameValue(«[object Object]`
  - ej: `test/language/expressions/async-generator/named-yield-star-getiter-async-not-callable-boolean-throw.js`
- **220x** `Uncaught { message: length descriptor value should be N; length value should be N }`
  - ej: `test/language/expressions/arrow-function/length-dflt.js`
- **207x** `async incomplete: Uncaught { message: asyncTest called without async flag }`
  - ej: `test/language/expressions/async-function/named-strict-error-reassign-fn-name-in-body-in-arrow.js`
- **196x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **192x** `Uncaught { message: m descriptor should not be enumerable }`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-computed-names.js`
- **191x** `Uncaught RangeError: Invalid length: must be a non-negative safe integer`
  - ej: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **177x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«N», «N») to be true`
  - ej: `test/language/expressions/async-generator/named-yield-star-getiter-async-null-sync-get-abrupt.js`
- **176x** `Uncaught { message: Expected a TestNError but got a TypeError }`
  - ej: `test/language/expressions/assignment/dstr/array-elem-trlg-iter-rest-rtrn-close-err.js`
- **172x** `async incomplete: SyntaxError: InvalidUnicodeEscape`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-static-async-generator-method-privatename-identifier.js`
- **172x** `Uncaught { message: Expected a TypeError but got a ReferenceError }`
  - ej: `test/language/global-code/script-decl-func-err-non-extensible.js`
- **166x** `Uncaught { message: Expected a ReferenceError to be thrown but no exception was thrown at all }`
  - ej: `test/language/expressions/arrow-function/lexical-super-call-from-within-constructor.js`
- **156x** `async incomplete: SyntaxError: UnexpectedCharacter`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-static-async-generator-method-privatename-identifier-alt.js`
- **131x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - ej: `test/language/eval-code/indirect/var-env-func-non-strict.js`
- **130x** `Uncaught TypeError: Object.defineProperty called on non-object`
  - ej: `test/language/eval-code/indirect/var-env-func-init-global-update-configurable.js`
- **113x** `Uncaught { message: isConstructor invoked with a non-function value }`
  - ej: `test/built-ins/Array/fromAsync/not-a-constructor.js`
- **113x** `Uncaught { message: Built-in objects must be extensible. Expected SameValue(«false», «true») to be true }`
  - ej: `test/built-ins/Set/prototype/difference/builtins.js`

## Top features presentes en FAILs

- 3194x Temporal
- 2106x class
- 1800x TypedArray
- 1781x async-iteration
- 1726x generators
- 1560x destructuring-binding
- 1465x class-fields-public
- 1022x Symbol.iterator
- 898x BigInt
- 878x Symbol
- 659x default-parameters
- 645x class-static-methods-private
- 611x class-methods-private
- 604x dynamic-import
- 541x class-fields-private
- 489x Symbol.asyncIterator
- 459x resizable-arraybuffer
- 459x SharedArrayBuffer
- 453x arrow-function
- 386x iterator-helpers
- 382x Atomics
- 364x Proxy
- 356x explicit-resource-management
- 343x Reflect
- 298x class-static-fields-private
