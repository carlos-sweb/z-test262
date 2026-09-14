# Test262 — z-* engine divergence report

Total: 47381 tests | ran: 45639 | **PASS: 29572 (64.8% of those ran)** | FAIL: 16051 | CRASH: 0 | TIMEOUT: 16 | SKIP (by design): 1742


## Pass rate by area

| area | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 0 | 25 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Array | 1778 | 1264 | 0 | 3 | 36 | 58.4% |
| test/built-ins/ArrayBuffer | 34 | 187 | 0 | 0 | 0 | 15.4% |
| test/built-ins/ArrayIteratorPrototype | 10 | 9 | 0 | 0 | 8 | 52.6% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 6 | 32 | 0 | 0 | 0 | 15.8% |
| test/built-ins/AsyncFunction | 9 | 9 | 0 | 0 | 0 | 50.0% |
| test/built-ins/AsyncGeneratorFunction | 8 | 15 | 0 | 0 | 0 | 34.8% |
| test/built-ins/AsyncGeneratorPrototype | 2 | 45 | 0 | 1 | 0 | 4.2% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 207 | 180 | 0 | 0 | 2 | 53.5% |
| test/built-ins/BigInt | 63 | 14 | 0 | 0 | 0 | 81.8% |
| test/built-ins/Boolean | 46 | 5 | 0 | 0 | 0 | 90.2% |
| test/built-ins/DataView | 374 | 187 | 0 | 0 | 0 | 66.7% |
| test/built-ins/Date | 521 | 73 | 0 | 0 | 0 | 87.7% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 28 | 65 | 0 | 0 | 0 | 30.1% |
| test/built-ins/FinalizationRegistry | 0 | 47 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Function | 202 | 219 | 0 | 0 | 88 | 48.0% |
| test/built-ins/GeneratorFunction | 8 | 15 | 0 | 0 | 0 | 34.8% |
| test/built-ins/GeneratorPrototype | 15 | 45 | 0 | 1 | 0 | 24.6% |
| test/built-ins/Infinity | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/Iterator | 7 | 507 | 0 | 0 | 0 | 1.4% |
| test/built-ins/JSON | 82 | 83 | 0 | 0 | 0 | 49.7% |
| test/built-ins/Map | 129 | 74 | 0 | 0 | 1 | 63.5% |
| test/built-ins/MapIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/Math | 326 | 1 | 0 | 0 | 0 | 99.7% |
| test/built-ins/NaN | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/NativeErrors | 44 | 50 | 0 | 0 | 0 | 46.8% |
| test/built-ins/Number | 262 | 78 | 0 | 0 | 0 | 77.1% |
| test/built-ins/Object | 2274 | 1126 | 0 | 0 | 11 | 66.9% |
| test/built-ins/Promise | 201 | 525 | 0 | 0 | 3 | 27.7% |
| test/built-ins/Proxy | 82 | 218 | 0 | 0 | 11 | 27.3% |
| test/built-ins/Reflect | 109 | 44 | 0 | 0 | 0 | 71.2% |
| test/built-ins/RegExp | 1229 | 646 | 0 | 3 | 1 | 65.4% |
| test/built-ins/RegExpStringIteratorPrototype | 0 | 17 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Set | 205 | 177 | 0 | 0 | 1 | 53.7% |
| test/built-ins/SetIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 30 | 74 | 0 | 0 | 0 | 28.8% |
| test/built-ins/String | 956 | 264 | 0 | 0 | 3 | 78.4% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 0 | 22 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Symbol | 63 | 33 | 0 | 0 | 2 | 65.6% |
| test/built-ins/Temporal | 2074 | 2529 | 0 | 0 | 0 | 45.1% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 476 | 962 | 0 | 0 | 8 | 33.1% |
| test/built-ins/TypedArrayConstructors | 336 | 386 | 0 | 0 | 16 | 46.5% |
| test/built-ins/Uint8Array | 6 | 64 | 0 | 0 | 0 | 8.6% |
| test/built-ins/WeakMap | 0 | 141 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakRef | 0 | 29 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakSet | 0 | 85 | 0 | 0 | 0 | 0.0% |
| test/built-ins/decodeURI | 54 | 0 | 0 | 1 | 0 | 98.2% |
| test/built-ins/decodeURIComponent | 55 | 0 | 0 | 1 | 0 | 98.2% |
| test/built-ins/encodeURI | 25 | 5 | 0 | 1 | 0 | 80.6% |
| test/built-ins/encodeURIComponent | 25 | 5 | 0 | 1 | 0 | 80.6% |
| test/built-ins/eval | 10 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/global | 29 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/isFinite | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/isNaN | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/parseFloat | 50 | 4 | 0 | 0 | 0 | 92.6% |
| test/built-ins/parseInt | 49 | 6 | 0 | 0 | 0 | 89.1% |
| test/built-ins/undefined | 5 | 0 | 0 | 0 | 3 | 100.0% |
| test/language/arguments-object | 189 | 17 | 0 | 0 | 57 | 91.7% |
| test/language/asi | 101 | 1 | 0 | 0 | 0 | 99.0% |
| test/language/block-scope | 145 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/comments | 46 | 6 | 0 | 0 | 0 | 88.5% |
| test/language/computed-property-names | 46 | 2 | 0 | 0 | 0 | 95.8% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 96 | 31 | 0 | 0 | 220 | 75.6% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 7897 | 2617 | 0 | 0 | 588 | 75.1% |
| test/language/function-code | 100 | 8 | 0 | 0 | 109 | 92.6% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 21 | 16 | 0 | 0 | 5 | 56.8% |
| test/language/identifier-resolution | 8 | 1 | 0 | 0 | 5 | 88.9% |
| test/language/identifiers | 264 | 4 | 0 | 0 | 0 | 98.5% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 39 | 2 | 0 | 0 | 0 | 95.1% |
| test/language/literals | 508 | 8 | 0 | 4 | 14 | 97.7% |
| test/language/module-code | 216 | 383 | 0 | 0 | 0 | 36.1% |
| test/language/punctuators | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/reserved-words | 27 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/rest-parameters | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/source-text | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/statementList | 76 | 4 | 0 | 0 | 0 | 95.0% |
| test/language/statements | 6947 | 1918 | 0 | 0 | 472 | 78.4% |
| test/language/types | 101 | 3 | 0 | 0 | 9 | 97.1% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top FAIL causes (normalized message)

- **809x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/language/arguments-object/10.6-13-c-3-s.js`
- **686x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/eval-code/indirect/non-definable-global-function.js`
- **605x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - e.g.: `test/language/comments/hashbang/use-strict.js`
- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - e.g.: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **516x** `SyntaxError: UnexpectedToken`
  - e.g.: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **486x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/expressions/assignment/dstr/array-empty-iter-close-err.js`
- **412x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - e.g.: `test/language/expressions/arrow-function/dstr/ary-ptrn-elem-id-iter-val-array-prototype.js`
- **333x** `Uncaught ReferenceError: Iterator is not defined`
  - e.g.: `test/built-ins/Iterator/length.js`
- **324x** `Uncaught ReferenceError: $N is not defined`
  - e.g.: `test/language/eval-code/indirect/realm.js`
- **294x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - e.g.: `test/language/expressions/object/method-definition/generator-prototype-prop.js`
- **278x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - e.g.: `test/language/expressions/async-generator/expression-yield-star-before-newline.js`
- **228x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: TypeError Expected SameValue(«[object Functio`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-not-callable-boolean-throw.js`
- **196x** `SyntaxError: MissingSemicolon`
  - e.g.: `test/language/asi/do-while-same-line.js`
- **182x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«N», «N») to be true`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-null-sync-get-abrupt.js`
- **182x** `Uncaught { message: Expected SameValue(«[object Function]», «N») to be true }`
  - e.g.: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **171x** `Uncaught RangeError: Invalid time zone`
  - e.g.: `test/built-ins/Temporal/Duration/prototype/round/relativeto-days-24-hours-relative-to-zoned-date-time.js`
- **166x** `Uncaught { message: Expected a ReferenceError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/expressions/arrow-function/dflt-params-ref-self.js`
- **160x** `Uncaught { message: Expected a TypeError but got a ReferenceError }`
  - e.g.: `test/language/global-code/script-decl-func-err-non-extensible.js`
- **157x** `Uncaught TypeError: Object.defineProperty called on non-object`
  - e.g.: `test/built-ins/Array/prototype/methods-called-as-functions.js`
- **151x** `SyntaxError: OutOfMemory`
  - e.g.: `test/language/arguments-object/10.6-6-2.js`
- **143x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - e.g.: `test/language/eval-code/indirect/var-env-func-non-strict.js`
- **132x** `Uncaught RangeError: Maximum call stack size exceeded`
  - e.g.: `test/language/expressions/tco-pos.js`
- **131x** `Uncaught { message: Expected a TestNError but got a TypeError }`
  - e.g.: `test/language/expressions/assignment/dstr/array-elem-trlg-iter-rest-rtrn-close-err.js`
- **128x** `Uncaught RangeError: Invalid Temporal string`
  - e.g.: `test/built-ins/Temporal/Duration/prototype/round/relativeto-date-limits.js`
- **127x** `Uncaught { message: Expected a RangeError but got a TypeError }`
  - e.g.: `test/built-ins/Array/prototype/splice/create-non-array-invalid-len.js`
- **120x** `Uncaught TypeError: month is required`
  - e.g.: `test/built-ins/Temporal/PlainDate/compare/argument-propertybag-calendar-case-insensitive.js`
- **119x** `Uncaught TypeError: resize is not a function`
  - e.g.: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **119x** `Uncaught TypeError: Property description must be an object`
  - e.g.: `test/built-ins/Object/create/15.2.3.5-4-10.js`
- **116x** `async incomplete: SyntaxError: OutOfMemory`
  - e.g.: `test/language/expressions/async-generator/dstr/ary-init-iter-close.js`
- **111x** `Uncaught { message: Expected SameValue(«undefined», «N») to be true }`
  - e.g.: `test/language/expressions/array/spread-obj-mult-spread-getter.js`

## Top features present in FAILs

- 2537x Temporal
- 1502x async-iteration
- 1495x TypedArray
- 1224x generators
- 1177x Symbol.iterator
- 1084x class
- 1069x destructuring-binding
- 687x class-fields-public
- 655x BigInt
- 604x dynamic-import
- 599x Symbol
- 501x Symbol.asyncIterator
- 451x resizable-arraybuffer
- 449x class-methods-private
- 436x default-parameters
- 397x class-fields-private
- 386x iterator-helpers
- 383x arrow-function
- 361x Proxy
- 350x explicit-resource-management
- 347x class-static-methods-private
- 324x Reflect
- 271x Symbol.species
- 258x top-level-await
- 251x SharedArrayBuffer
