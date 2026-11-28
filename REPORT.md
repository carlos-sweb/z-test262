# Test262 — z-* engine divergence report

Total: 47381 tests | ran: 45639 | **PASS: 43187 (94.6% of those ran)** | FAIL: 2452 | CRASH: 0 | TIMEOUT: 0 | SKIP (by design): 1742


## Pass rate by area

| area | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 24 | 1 | 0 | 0 | 0 | 96.0% |
| test/built-ins/Array | 2899 | 146 | 0 | 0 | 36 | 95.2% |
| test/built-ins/ArrayBuffer | 154 | 67 | 0 | 0 | 0 | 69.7% |
| test/built-ins/ArrayIteratorPrototype | 19 | 0 | 0 | 0 | 8 | 100.0% |
| test/built-ins/AsyncDisposableStack | 103 | 1 | 0 | 0 | 0 | 99.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 38 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/AsyncFunction | 17 | 1 | 0 | 0 | 0 | 94.4% |
| test/built-ins/AsyncGeneratorFunction | 21 | 2 | 0 | 0 | 0 | 91.3% |
| test/built-ins/AsyncGeneratorPrototype | 48 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/AsyncIteratorPrototype | 13 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/Atomics | 210 | 177 | 0 | 0 | 2 | 54.3% |
| test/built-ins/BigInt | 76 | 1 | 0 | 0 | 0 | 98.7% |
| test/built-ins/Boolean | 50 | 1 | 0 | 0 | 0 | 98.0% |
| test/built-ins/DataView | 514 | 47 | 0 | 0 | 0 | 91.6% |
| test/built-ins/Date | 591 | 3 | 0 | 0 | 0 | 99.5% |
| test/built-ins/DisposableStack | 92 | 1 | 0 | 0 | 0 | 98.9% |
| test/built-ins/Error | 88 | 5 | 0 | 0 | 0 | 94.6% |
| test/built-ins/FinalizationRegistry | 46 | 1 | 0 | 0 | 0 | 97.9% |
| test/built-ins/Function | 405 | 16 | 0 | 0 | 88 | 96.2% |
| test/built-ins/GeneratorFunction | 21 | 2 | 0 | 0 | 0 | 91.3% |
| test/built-ins/GeneratorPrototype | 61 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/Infinity | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/Iterator | 513 | 1 | 0 | 0 | 0 | 99.8% |
| test/built-ins/JSON | 163 | 2 | 0 | 0 | 0 | 98.8% |
| test/built-ins/Map | 202 | 1 | 0 | 0 | 1 | 99.5% |
| test/built-ins/MapIteratorPrototype | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/Math | 327 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/NaN | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/NativeErrors | 88 | 6 | 0 | 0 | 0 | 93.6% |
| test/built-ins/Number | 339 | 1 | 0 | 0 | 0 | 99.7% |
| test/built-ins/Object | 3353 | 47 | 0 | 0 | 11 | 98.6% |
| test/built-ins/Promise | 725 | 1 | 0 | 0 | 3 | 99.9% |
| test/built-ins/Proxy | 244 | 56 | 0 | 0 | 11 | 81.3% |
| test/built-ins/Reflect | 151 | 2 | 0 | 0 | 0 | 98.7% |
| test/built-ins/RegExp | 1779 | 99 | 0 | 0 | 1 | 94.7% |
| test/built-ins/RegExpStringIteratorPrototype | 17 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/Set | 381 | 1 | 0 | 0 | 1 | 99.7% |
| test/built-ins/SetIteratorPrototype | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 75 | 29 | 0 | 0 | 0 | 72.1% |
| test/built-ins/String | 1216 | 4 | 0 | 0 | 3 | 99.7% |
| test/built-ins/StringIteratorPrototype | 7 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/SuppressedError | 21 | 1 | 0 | 0 | 0 | 95.5% |
| test/built-ins/Symbol | 77 | 19 | 0 | 0 | 2 | 80.2% |
| test/built-ins/Temporal | 4603 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/ThrowTypeError | 13 | 1 | 0 | 0 | 0 | 92.9% |
| test/built-ins/TypedArray | 1229 | 209 | 0 | 0 | 8 | 85.5% |
| test/built-ins/TypedArrayConstructors | 683 | 39 | 0 | 0 | 16 | 94.6% |
| test/built-ins/Uint8Array | 68 | 2 | 0 | 0 | 0 | 97.1% |
| test/built-ins/WeakMap | 140 | 1 | 0 | 0 | 0 | 99.3% |
| test/built-ins/WeakRef | 28 | 1 | 0 | 0 | 0 | 96.6% |
| test/built-ins/WeakSet | 84 | 1 | 0 | 0 | 0 | 98.8% |
| test/built-ins/decodeURI | 55 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/decodeURIComponent | 56 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/encodeURI | 31 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/encodeURIComponent | 31 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/eval | 10 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/global | 29 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/isFinite | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/isNaN | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/parseFloat | 54 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/parseInt | 55 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/undefined | 5 | 0 | 0 | 0 | 3 | 100.0% |
| test/language/arguments-object | 206 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/asi | 102 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/block-scope | 145 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/comments | 51 | 1 | 0 | 0 | 0 | 98.1% |
| test/language/computed-property-names | 48 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 126 | 1 | 0 | 0 | 220 | 99.2% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 9827 | 687 | 0 | 0 | 588 | 93.5% |
| test/language/function-code | 108 | 0 | 0 | 0 | 109 | 100.0% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 36 | 1 | 0 | 0 | 5 | 97.3% |
| test/language/identifier-resolution | 9 | 0 | 0 | 0 | 5 | 100.0% |
| test/language/identifiers | 264 | 4 | 0 | 0 | 0 | 98.5% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 41 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/literals | 520 | 0 | 0 | 0 | 14 | 100.0% |
| test/language/module-code | 229 | 370 | 0 | 0 | 0 | 38.2% |
| test/language/punctuators | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/reserved-words | 27 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/rest-parameters | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/source-text | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/statementList | 80 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/statements | 8663 | 202 | 0 | 0 | 472 | 97.7% |
| test/language/types | 102 | 2 | 0 | 0 | 9 | 98.1% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top FAIL causes (normalized message)

- **467x** `async incomplete: SyntaxError: UnexpectedToken`
  - e.g.: `test/language/expressions/class/cpn-class-expr-computed-property-name-from-await-expression.js`
- **322x** `SyntaxError: UnexpectedToken`
  - e.g.: `test/language/expressions/dynamic-import/returns-promise.js`
- **172x** `Uncaught TypeError: createRealm is not a function`
  - e.g.: `test/language/eval-code/indirect/realm.js`
- **142x** `SyntaxError: MissingSemicolon`
  - e.g.: `test/language/import/import-attributes/json-extensibility-array.js`
- **107x** `Uncaught TypeError: resize is not a function`
  - e.g.: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **79x** `Uncaught TypeError: undefined is not a function`
  - e.g.: `test/language/expressions/class/private-getter-brand-check-multiple-evaluations-of-class-realm-function-ctor.js`
- **76x** `Uncaught { message: implements ArrayBuffer.prototype.resize Expected SameValue(«"undefined"», «"function"») to`
  - e.g.: `test/built-ins/DataView/prototype/getBigInt64/resizable-buffer.js`
- **67x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/language/expressions/optional-chaining/optional-call-preserves-this.js`
- **67x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - e.g.: `test/built-ins/AbstractModuleSource/length.js`
- **57x** `Uncaught ReferenceError: ShadowRealm is not defined`
  - e.g.: `test/built-ins/ShadowRealm/extensibility.js`
- **54x** `async incomplete: SyntaxError: MissingSemicolon`
  - e.g.: `test/language/import/import-attributes/json-idempotency.js`
- **53x** `async incomplete: Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/built-ins/Atomics/waitAsync/false-for-timeout-agent.js`
- **32x** `Uncaught { message: The value of `typeof Atomics.waitAsync` is "function" Expected SameValue(«"undefined"», «"`
  - e.g.: `test/built-ins/Atomics/waitAsync/bad-range.js`
- **22x** `Engine error: StackOverflow`
  - e.g.: `test/language/expressions/tco-pos.js`
- **19x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/expressions/assignment/target-super-computed-reference-null.js`
- **18x** `Uncaught TypeError: transferToImmutable is not a function`
  - e.g.: `test/built-ins/ArrayBuffer/prototype/resize/this-is-immutable-arraybuffer-object.js`
- **18x** `Uncaught { message: no arg factories match include immutable and exclude undefined }`
  - e.g.: `test/built-ins/Atomics/add/immutable-buffer.js`
- **16x** `SyntaxError: UnexpectedCharacter`
  - e.g.: `test/language/expressions/class/decorator/syntax/class-valid/decorator-member-expr-private-identifier.js`
- **16x** `Uncaught ReferenceError: await is not defined`
  - e.g.: `test/language/module-code/top-level-await/syntax/block-await-expr-template-literal.js`
- **12x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - e.g.: `test/language/statements/let/syntax/let-closure-inside-condition.js`
- **12x** `async incomplete: Uncaught { message: The value of `typeof Atomics.waitAsync` is "function" Expected SameValue`
  - e.g.: `test/built-ins/Atomics/waitAsync/false-for-timeout.js`
- **11x** `Uncaught { message: Expected a RangeError but got a TypeError }`
  - e.g.: `test/built-ins/Array/prototype/toSpliced/length-exceeding-array-length-limit.js`
- **8x** `Uncaught RangeError: Maximum call stack size exceeded`
  - e.g.: `test/language/expressions/tagged-template/tco-call.js`
- **8x** `Uncaught { message: Expected SameValue(«[object Object]», «undefined») to be true }`
  - e.g.: `test/language/module-code/eval-this.js`
- **8x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/statements/class/elements/public-class-field-initialization-is-visible-to-proxy.js`
- **7x** `Uncaught { message: Expected true but got false }`
  - e.g.: `test/built-ins/ArrayBuffer/prototype/resize/coerced-new-length-detach.js`
- **7x** `Uncaught { message: Method must exist. Expected SameValue(«"undefined"», «"function"») to be true }`
  - e.g.: `test/built-ins/ArrayBuffer/prototype/sliceToImmutable/this-becomes-detached.js`
- **6x** `Uncaught TypeError: iterator.next is not a function`
  - e.g.: `test/language/expressions/assignment/dstr/array-elem-iter-rtrn-close-err.js`
- **6x** `Uncaught TypeError: This operation is not supported by this engine yet`
  - e.g.: `test/language/expressions/does-not-equals/bigint-and-incomparable-primitive.js`
- **6x** `Uncaught { message: Expected a RangeError to be thrown but no exception was thrown at all }`
  - e.g.: `test/built-ins/ArrayBuffer/options-maxbytelength-diminuitive.js`

## Top features present in FAILs

- 604x dynamic-import
- 388x resizable-arraybuffer
- 321x TypedArray
- 258x top-level-await
- 182x SharedArrayBuffer
- 177x Atomics
- 175x cross-realm
- 154x import-defer
- 141x BigInt
- 119x explicit-resource-management
- 111x Symbol
- 110x arrow-function
- 107x Reflect
- 101x Atomics.waitAsync
- 98x source-phase-imports
- 90x class
- 84x ArrayBuffer
- 81x import-attributes
- 80x Proxy
- 70x regexp-modifiers
- 65x async-iteration
- 64x immutable-arraybuffer
- 64x ShadowRealm
- 51x async-functions
- 41x source-phase-imports-module-source
