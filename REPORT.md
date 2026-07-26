# Test262 — reporte de divergencias del motor z-*

Total: 47381 tests | corridos: 45639 | **PASS: 18576 (40.7% de los corridos)** | FAIL: 26385 | CRASH: 0 | TIMEOUT: 678 | SKIP (by design): 1742


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 0 | 25 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Array | 745 | 2274 | 0 | 26 | 36 | 24.5% |
| test/built-ins/ArrayBuffer | 0 | 221 | 0 | 0 | 0 | 0.0% |
| test/built-ins/ArrayIteratorPrototype | 0 | 19 | 0 | 0 | 8 | 0.0% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 3 | 22 | 0 | 13 | 0 | 7.9% |
| test/built-ins/AsyncFunction | 5 | 12 | 0 | 1 | 0 | 27.8% |
| test/built-ins/AsyncGeneratorFunction | 2 | 20 | 0 | 1 | 0 | 8.7% |
| test/built-ins/AsyncGeneratorPrototype | 0 | 47 | 0 | 1 | 0 | 0.0% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 0 | 387 | 0 | 0 | 2 | 0.0% |
| test/built-ins/BigInt | 27 | 50 | 0 | 0 | 0 | 35.1% |
| test/built-ins/Boolean | 32 | 19 | 0 | 0 | 0 | 62.7% |
| test/built-ins/DataView | 0 | 561 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Date | 291 | 303 | 0 | 0 | 0 | 49.0% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 9 | 84 | 0 | 0 | 0 | 9.7% |
| test/built-ins/FinalizationRegistry | 0 | 47 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Function | 112 | 306 | 0 | 3 | 88 | 26.6% |
| test/built-ins/GeneratorFunction | 4 | 18 | 0 | 1 | 0 | 17.4% |
| test/built-ins/GeneratorPrototype | 14 | 46 | 0 | 1 | 0 | 23.0% |
| test/built-ins/Infinity | 2 | 2 | 0 | 0 | 2 | 50.0% |
| test/built-ins/Iterator | 7 | 505 | 0 | 2 | 0 | 1.4% |
| test/built-ins/JSON | 68 | 97 | 0 | 0 | 0 | 41.2% |
| test/built-ins/Map | 94 | 104 | 0 | 5 | 1 | 46.3% |
| test/built-ins/MapIteratorPrototype | 0 | 11 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Math | 80 | 246 | 0 | 1 | 0 | 24.5% |
| test/built-ins/NaN | 2 | 2 | 0 | 0 | 2 | 50.0% |
| test/built-ins/NativeErrors | 18 | 76 | 0 | 0 | 0 | 19.1% |
| test/built-ins/Number | 134 | 206 | 0 | 0 | 0 | 39.4% |
| test/built-ins/Object | 1576 | 1808 | 0 | 16 | 11 | 46.4% |
| test/built-ins/Promise | 156 | 570 | 0 | 0 | 3 | 21.5% |
| test/built-ins/Proxy | 77 | 223 | 0 | 0 | 11 | 25.7% |
| test/built-ins/Reflect | 64 | 89 | 0 | 0 | 0 | 41.8% |
| test/built-ins/RegExp | 469 | 1007 | 0 | 402 | 1 | 25.0% |
| test/built-ins/RegExpStringIteratorPrototype | 0 | 17 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Set | 176 | 205 | 0 | 1 | 1 | 46.1% |
| test/built-ins/SetIteratorPrototype | 0 | 11 | 0 | 0 | 0 | 0.0% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/String | 474 | 746 | 0 | 0 | 3 | 38.9% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 0 | 22 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Symbol | 19 | 77 | 0 | 0 | 2 | 19.8% |
| test/built-ins/Temporal | 0 | 4603 | 0 | 0 | 0 | 0.0% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 0 | 1438 | 0 | 0 | 8 | 0.0% |
| test/built-ins/TypedArrayConstructors | 0 | 722 | 0 | 0 | 16 | 0.0% |
| test/built-ins/Uint8Array | 0 | 70 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakMap | 0 | 141 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakRef | 0 | 29 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakSet | 0 | 85 | 0 | 0 | 0 | 0.0% |
| test/built-ins/decodeURI | 0 | 47 | 0 | 8 | 0 | 0.0% |
| test/built-ins/decodeURIComponent | 0 | 48 | 0 | 8 | 0 | 0.0% |
| test/built-ins/encodeURI | 0 | 31 | 0 | 0 | 0 | 0.0% |
| test/built-ins/encodeURIComponent | 0 | 31 | 0 | 0 | 0 | 0.0% |
| test/built-ins/eval | 4 | 6 | 0 | 0 | 0 | 40.0% |
| test/built-ins/global | 22 | 7 | 0 | 0 | 0 | 75.9% |
| test/built-ins/isFinite | 4 | 11 | 0 | 0 | 0 | 26.7% |
| test/built-ins/isNaN | 4 | 11 | 0 | 0 | 0 | 26.7% |
| test/built-ins/parseFloat | 41 | 12 | 0 | 1 | 0 | 75.9% |
| test/built-ins/parseInt | 38 | 16 | 0 | 1 | 0 | 69.1% |
| test/built-ins/undefined | 2 | 3 | 0 | 0 | 3 | 40.0% |
| test/language/arguments-object | 189 | 17 | 0 | 0 | 57 | 91.7% |
| test/language/asi | 98 | 4 | 0 | 0 | 0 | 96.1% |
| test/language/block-scope | 144 | 1 | 0 | 0 | 0 | 99.3% |
| test/language/comments | 43 | 8 | 0 | 1 | 0 | 82.7% |
| test/language/computed-property-names | 28 | 20 | 0 | 0 | 0 | 58.3% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 92 | 35 | 0 | 0 | 220 | 72.4% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 6053 | 4374 | 0 | 87 | 588 | 57.6% |
| test/language/function-code | 99 | 9 | 0 | 0 | 109 | 91.7% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 19 | 18 | 0 | 0 | 5 | 51.4% |
| test/language/identifier-resolution | 6 | 3 | 0 | 0 | 5 | 66.7% |
| test/language/identifiers | 230 | 12 | 0 | 26 | 0 | 85.8% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 36 | 5 | 0 | 0 | 0 | 87.8% |
| test/language/literals | 488 | 28 | 0 | 4 | 14 | 93.8% |
| test/language/module-code | 217 | 382 | 0 | 0 | 0 | 36.2% |
| test/language/punctuators | 10 | 1 | 0 | 0 | 0 | 90.9% |
| test/language/reserved-words | 27 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/rest-parameters | 9 | 2 | 0 | 0 | 0 | 81.8% |
| test/language/source-text | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/language/statementList | 76 | 4 | 0 | 0 | 0 | 95.0% |
| test/language/statements | 5671 | 3126 | 0 | 68 | 472 | 64.0% |
| test/language/types | 88 | 16 | 0 | 0 | 9 | 84.6% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top causas de FAIL (mensaje normalizado)

- **5818x** `Uncaught [object]`
  - ej: `test/language/arguments-object/S10.6_A3_T1.js`
- **4151x** `Uncaught ReferenceError: Temporal is not defined`
  - ej: `test/built-ins/Temporal/getOwnPropertyNames.js`
- **2508x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/asi/S7.9_A10_T1.js`
- **2076x** `Uncaught ReferenceError: FloatNArray is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-Float32Array.js`
- **1057x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet
error(DebugAllocator): memory`
  - ej: `test/language/arguments-object/10.6-11-b-1.js`
- **820x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-function/named-dflt-params-ref-self.js`
- **577x** `Uncaught ReferenceError: ArrayBuffer is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-ArrayBuffer.js`
- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **542x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet
error(Debug`
  - ej: `test/language/expressions/async-generator/named-yield-promise-reject-next-yield-star-sync-iterator.js`
- **518x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/expressions/arrow-function/lexical-new.target-closure-returned.js`
- **385x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/arguments-object/10.6-13-c-3-s.js`
- **372x** `SyntaxError: InvalidUnicodeEscape`
  - ej: `test/language/expressions/class/decorator/syntax/class-valid/decorator-member-expr-private-identifier.js`
- **328x** `Uncaught ReferenceError: Iterator is not defined`
  - ej: `test/built-ins/Iterator/length.js`
- **302x** `SyntaxError: UnexpectedCharacter`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **235x** `async incomplete: Uncaught [object]`
  - ej: `test/language/expressions/async-generator/dflt-params-trailing-comma.js`
- **227x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - ej: `test/language/eval-code/indirect/non-definable-function-with-function.js`
- **212x** `Uncaught ReferenceError: $N is not defined`
  - ej: `test/language/eval-code/indirect/realm.js`
- **196x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **175x** `Uncaught ReferenceError: DataView is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-DataView.js`
- **172x** `async incomplete: SyntaxError: InvalidUnicodeEscape`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-static-async-generator-method-privatename-identifier.js`
- **156x** `async incomplete: SyntaxError: UnexpectedCharacter`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-static-async-generator-method-privatename-identifier-alt.js`
- **137x** `Uncaught TypeError: expression is not a function`
  - ej: `test/language/statements/for-of/Array.prototype.Symbol.iterator.js`
- **124x** `Uncaught ReferenceError: SharedArrayBuffer is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-SharedArrayBuffer.js`
- **111x** `Uncaught TypeError: Array.prototype.reduce called on a non-array`
  - ej: `test/built-ins/Array/prototype/reduce/15.4.4.21-1-10.js`
- **109x** `Uncaught TypeError: Array.prototype.reduceRight called on a non-array`
  - ej: `test/built-ins/Array/prototype/reduceRight/15.4.4.22-2-12.js`
- **95x** `Uncaught ReferenceError: UintNArray is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-Uint16Array.js`
- **91x** `Uncaught ReferenceError: WeakMap is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-WeakMap.js`
- **89x** `Uncaught ReferenceError: Atomics is not defined`
  - ej: `test/built-ins/Atomics/Symbol.toStringTag.js`
- **88x** `Uncaught TypeError: Array.prototype.filter called on a non-array`
  - ej: `test/built-ins/Array/prototype/filter/15.4.4.20-1-9.js`
- **86x** `Uncaught TypeError: Array.prototype.some called on a non-array`
  - ej: `test/built-ins/Array/prototype/some/15.4.4.17-1-4.js`

## Top features presentes en FAILs

- 4611x Temporal
- 2489x TypedArray
- 2234x class
- 2079x async-iteration
- 1938x destructuring-binding
- 1860x generators
- 1525x class-fields-public
- 1285x BigInt
- 1192x Symbol
- 1081x Symbol.iterator
- 714x default-parameters
- 673x class-static-methods-private
- 639x class-methods-private
- 604x dynamic-import
- 547x class-fields-private
- 514x arrow-function
- 490x Symbol.asyncIterator
- 462x resizable-arraybuffer
- 459x SharedArrayBuffer
- 407x Reflect.construct
- 386x iterator-helpers
- 382x Atomics
- 372x Reflect
- 368x Proxy
- 356x explicit-resource-management
