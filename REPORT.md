# Test262 — reporte de divergencias del motor z-*

Total: 47381 tests | corridos: 45639 | **PASS: 21309 (46.7% de los corridos)** | FAIL: 23703 | CRASH: 0 | TIMEOUT: 627 | SKIP (by design): 1742


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 0 | 25 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Array | 762 | 2259 | 0 | 24 | 36 | 25.0% |
| test/built-ins/ArrayBuffer | 17 | 204 | 0 | 0 | 0 | 7.7% |
| test/built-ins/ArrayIteratorPrototype | 10 | 9 | 0 | 0 | 8 | 52.6% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 4 | 21 | 0 | 13 | 0 | 10.5% |
| test/built-ins/AsyncFunction | 6 | 12 | 0 | 0 | 0 | 33.3% |
| test/built-ins/AsyncGeneratorFunction | 4 | 19 | 0 | 0 | 0 | 17.4% |
| test/built-ins/AsyncGeneratorPrototype | 1 | 46 | 0 | 1 | 0 | 2.1% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 0 | 387 | 0 | 0 | 2 | 0.0% |
| test/built-ins/BigInt | 27 | 50 | 0 | 0 | 0 | 35.1% |
| test/built-ins/Boolean | 32 | 19 | 0 | 0 | 0 | 62.7% |
| test/built-ins/DataView | 229 | 332 | 0 | 0 | 0 | 40.8% |
| test/built-ins/Date | 291 | 303 | 0 | 0 | 0 | 49.0% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 10 | 83 | 0 | 0 | 0 | 10.8% |
| test/built-ins/FinalizationRegistry | 0 | 47 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Function | 132 | 289 | 0 | 0 | 88 | 31.4% |
| test/built-ins/GeneratorFunction | 6 | 17 | 0 | 0 | 0 | 26.1% |
| test/built-ins/GeneratorPrototype | 14 | 46 | 0 | 1 | 0 | 23.0% |
| test/built-ins/Infinity | 2 | 2 | 0 | 0 | 2 | 50.0% |
| test/built-ins/Iterator | 7 | 507 | 0 | 0 | 0 | 1.4% |
| test/built-ins/JSON | 71 | 94 | 0 | 0 | 0 | 43.0% |
| test/built-ins/Map | 96 | 102 | 0 | 5 | 1 | 47.3% |
| test/built-ins/MapIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/Math | 81 | 246 | 0 | 0 | 0 | 24.8% |
| test/built-ins/NaN | 2 | 2 | 0 | 0 | 2 | 50.0% |
| test/built-ins/NativeErrors | 18 | 76 | 0 | 0 | 0 | 19.1% |
| test/built-ins/Number | 149 | 191 | 0 | 0 | 0 | 43.8% |
| test/built-ins/Object | 1609 | 1775 | 0 | 16 | 11 | 47.3% |
| test/built-ins/Promise | 171 | 555 | 0 | 0 | 3 | 23.6% |
| test/built-ins/Proxy | 77 | 223 | 0 | 0 | 11 | 25.7% |
| test/built-ins/Reflect | 70 | 83 | 0 | 0 | 0 | 45.8% |
| test/built-ins/RegExp | 564 | 924 | 0 | 390 | 1 | 30.0% |
| test/built-ins/RegExpStringIteratorPrototype | 0 | 17 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Set | 177 | 204 | 0 | 1 | 1 | 46.3% |
| test/built-ins/SetIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/String | 500 | 720 | 0 | 0 | 3 | 41.0% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 0 | 22 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Symbol | 19 | 77 | 0 | 0 | 2 | 19.8% |
| test/built-ins/Temporal | 1233 | 3370 | 0 | 0 | 0 | 26.8% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 381 | 1057 | 0 | 0 | 8 | 26.5% |
| test/built-ins/TypedArrayConstructors | 249 | 473 | 0 | 0 | 16 | 34.5% |
| test/built-ins/Uint8Array | 6 | 64 | 0 | 0 | 0 | 8.6% |
| test/built-ins/WeakMap | 0 | 141 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakRef | 0 | 29 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakSet | 0 | 85 | 0 | 0 | 0 | 0.0% |
| test/built-ins/decodeURI | 40 | 7 | 0 | 8 | 0 | 72.7% |
| test/built-ins/decodeURIComponent | 41 | 7 | 0 | 8 | 0 | 73.2% |
| test/built-ins/encodeURI | 16 | 14 | 0 | 1 | 0 | 51.6% |
| test/built-ins/encodeURIComponent | 16 | 14 | 0 | 1 | 0 | 51.6% |
| test/built-ins/eval | 5 | 5 | 0 | 0 | 0 | 50.0% |
| test/built-ins/global | 25 | 4 | 0 | 0 | 0 | 86.2% |
| test/built-ins/isFinite | 4 | 11 | 0 | 0 | 0 | 26.7% |
| test/built-ins/isNaN | 4 | 11 | 0 | 0 | 0 | 26.7% |
| test/built-ins/parseFloat | 43 | 11 | 0 | 0 | 0 | 79.6% |
| test/built-ins/parseInt | 39 | 16 | 0 | 0 | 0 | 70.9% |
| test/built-ins/undefined | 2 | 3 | 0 | 0 | 3 | 40.0% |
| test/language/arguments-object | 189 | 17 | 0 | 0 | 57 | 91.7% |
| test/language/asi | 98 | 4 | 0 | 0 | 0 | 96.1% |
| test/language/block-scope | 145 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/comments | 44 | 8 | 0 | 0 | 0 | 84.6% |
| test/language/computed-property-names | 28 | 20 | 0 | 0 | 0 | 58.3% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 95 | 32 | 0 | 0 | 220 | 74.8% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 6233 | 4195 | 0 | 86 | 588 | 59.3% |
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
| test/language/statements | 5695 | 3102 | 0 | 68 | 472 | 64.2% |
| test/language/types | 88 | 16 | 0 | 0 | 9 | 84.6% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top causas de FAIL (mensaje normalizado)

- **3782x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/arguments-object/10.6-11-b-1.js`
- **1352x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-arrow-function/dflt-params-ref-self.js`
- **1144x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/arguments-object/10.6-13-c-3-s.js`
- **715x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - ej: `test/language/arguments-object/10.6-13-c-1-s.js`
- **640x** `Uncaught TypeError: expression is not a constructor`
  - ej: `test/built-ins/Temporal/Duration/compare/blank-duration.js`
- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **518x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **472x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - ej: `test/language/expressions/assignment/dstr/array-empty-iter-close-err.js`
- **432x** `Uncaught { message: name should be an own property }`
  - ej: `test/language/expressions/arrow-function/name.js`
- **408x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - ej: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-id-iter-val-array-prototype.js`
- **397x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - ej: `test/language/eval-code/indirect/non-definable-function-with-function.js`
- **372x** `SyntaxError: InvalidUnicodeEscape`
  - ej: `test/language/expressions/class/decorator/syntax/class-valid/decorator-member-expr-private-identifier.js`
- **336x** `Uncaught { message: length should be an own property }`
  - ej: `test/language/expressions/arrow-function/length-dflt.js`
- **333x** `Uncaught ReferenceError: Iterator is not defined`
  - ej: `test/built-ins/Iterator/length.js`
- **322x** `Uncaught ReferenceError: $N is not defined`
  - ej: `test/language/eval-code/indirect/realm.js`
- **302x** `SyntaxError: UnexpectedCharacter`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **260x** `Uncaught ReferenceError: SharedArrayBuffer is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-SharedArrayBuffer.js`
- **207x** `async incomplete: Uncaught { message: asyncTest called without async flag }`
  - ej: `test/language/expressions/async-function/named-strict-error-reassign-fn-name-in-body-in-arrow.js`
- **196x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **191x** `Uncaught RangeError: Invalid length: must be a non-negative safe integer`
  - ej: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
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
- **112x** `Uncaught { message: Expected SameValue(«""», «"arrow"») to be true }`
  - ej: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-id-init-fn-name-arrow.js`

## Top features presentes en FAILs

- 3378x Temporal
- 2232x class
- 2076x async-iteration
- 1938x destructuring-binding
- 1856x generators
- 1823x TypedArray
- 1525x class-fields-public
- 1032x Symbol.iterator
- 930x BigInt
- 905x Symbol
- 714x default-parameters
- 673x class-static-methods-private
- 639x class-methods-private
- 604x dynamic-import
- 545x class-fields-private
- 490x Symbol.asyncIterator
- 459x resizable-arraybuffer
- 459x SharedArrayBuffer
- 454x arrow-function
- 386x iterator-helpers
- 382x Atomics
- 368x Proxy
- 364x Reflect
- 356x explicit-resource-management
- 325x object-rest
