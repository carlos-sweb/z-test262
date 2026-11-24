# Test262 — z-* engine divergence report

Total: 47381 tests | ran: 45639 | **PASS: 42820 (93.8% of those ran)** | FAIL: 2819 | CRASH: 0 | TIMEOUT: 0 | SKIP (by design): 1742


## Pass rate by area

| area | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 23 | 2 | 0 | 0 | 0 | 92.0% |
| test/built-ins/Array | 2899 | 146 | 0 | 0 | 36 | 95.2% |
| test/built-ins/ArrayBuffer | 154 | 67 | 0 | 0 | 0 | 69.7% |
| test/built-ins/ArrayIteratorPrototype | 19 | 0 | 0 | 0 | 8 | 100.0% |
| test/built-ins/AsyncDisposableStack | 103 | 1 | 0 | 0 | 0 | 99.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 38 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/AsyncFunction | 14 | 4 | 0 | 0 | 0 | 77.8% |
| test/built-ins/AsyncGeneratorFunction | 20 | 3 | 0 | 0 | 0 | 87.0% |
| test/built-ins/AsyncGeneratorPrototype | 42 | 6 | 0 | 0 | 0 | 87.5% |
| test/built-ins/AsyncIteratorPrototype | 13 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/Atomics | 210 | 177 | 0 | 0 | 2 | 54.3% |
| test/built-ins/BigInt | 70 | 7 | 0 | 0 | 0 | 90.9% |
| test/built-ins/Boolean | 50 | 1 | 0 | 0 | 0 | 98.0% |
| test/built-ins/DataView | 514 | 47 | 0 | 0 | 0 | 91.6% |
| test/built-ins/Date | 579 | 15 | 0 | 0 | 0 | 97.5% |
| test/built-ins/DisposableStack | 92 | 1 | 0 | 0 | 0 | 98.9% |
| test/built-ins/Error | 84 | 9 | 0 | 0 | 0 | 90.3% |
| test/built-ins/FinalizationRegistry | 46 | 1 | 0 | 0 | 0 | 97.9% |
| test/built-ins/Function | 386 | 35 | 0 | 0 | 88 | 91.7% |
| test/built-ins/GeneratorFunction | 20 | 3 | 0 | 0 | 0 | 87.0% |
| test/built-ins/GeneratorPrototype | 60 | 1 | 0 | 0 | 0 | 98.4% |
| test/built-ins/Infinity | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/Iterator | 510 | 4 | 0 | 0 | 0 | 99.2% |
| test/built-ins/JSON | 160 | 5 | 0 | 0 | 0 | 97.0% |
| test/built-ins/Map | 199 | 4 | 0 | 0 | 1 | 98.0% |
| test/built-ins/MapIteratorPrototype | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/Math | 327 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/NaN | 4 | 0 | 0 | 0 | 2 | 100.0% |
| test/built-ins/NativeErrors | 82 | 12 | 0 | 0 | 0 | 87.2% |
| test/built-ins/Number | 336 | 4 | 0 | 0 | 0 | 98.8% |
| test/built-ins/Object | 3341 | 59 | 0 | 0 | 11 | 98.3% |
| test/built-ins/Promise | 707 | 19 | 0 | 0 | 3 | 97.4% |
| test/built-ins/Proxy | 240 | 60 | 0 | 0 | 11 | 80.0% |
| test/built-ins/Reflect | 147 | 6 | 0 | 0 | 0 | 96.1% |
| test/built-ins/RegExp | 1777 | 101 | 0 | 0 | 1 | 94.6% |
| test/built-ins/RegExpStringIteratorPrototype | 17 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/Set | 377 | 5 | 0 | 0 | 1 | 98.7% |
| test/built-ins/SetIteratorPrototype | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 75 | 29 | 0 | 0 | 0 | 72.1% |
| test/built-ins/String | 1208 | 12 | 0 | 0 | 3 | 99.0% |
| test/built-ins/StringIteratorPrototype | 7 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/SuppressedError | 20 | 2 | 0 | 0 | 0 | 90.9% |
| test/built-ins/Symbol | 71 | 25 | 0 | 0 | 2 | 74.0% |
| test/built-ins/Temporal | 4579 | 24 | 0 | 0 | 0 | 99.5% |
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
| test/language/arguments-object | 201 | 5 | 0 | 0 | 57 | 97.6% |
| test/language/asi | 101 | 1 | 0 | 0 | 0 | 99.0% |
| test/language/block-scope | 145 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/comments | 46 | 6 | 0 | 0 | 0 | 88.5% |
| test/language/computed-property-names | 47 | 1 | 0 | 0 | 0 | 97.9% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 115 | 12 | 0 | 0 | 220 | 90.6% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 9758 | 756 | 0 | 0 | 588 | 92.8% |
| test/language/function-code | 106 | 2 | 0 | 0 | 109 | 98.1% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 24 | 13 | 0 | 0 | 5 | 64.9% |
| test/language/identifier-resolution | 8 | 1 | 0 | 0 | 5 | 88.9% |
| test/language/identifiers | 264 | 4 | 0 | 0 | 0 | 98.5% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 39 | 2 | 0 | 0 | 0 | 95.1% |
| test/language/literals | 519 | 1 | 0 | 0 | 14 | 99.8% |
| test/language/module-code | 229 | 370 | 0 | 0 | 0 | 38.2% |
| test/language/punctuators | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/reserved-words | 27 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/rest-parameters | 11 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/source-text | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/statementList | 76 | 4 | 0 | 0 | 0 | 95.0% |
| test/language/statements | 8566 | 299 | 0 | 0 | 472 | 96.6% |
| test/language/types | 101 | 3 | 0 | 0 | 9 | 97.1% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top FAIL causes (normalized message)

- **467x** `async incomplete: SyntaxError: UnexpectedToken`
  - e.g.: `test/language/expressions/class/cpn-class-expr-accessors-computed-property-name-from-await-expression.js`
- **324x** `SyntaxError: UnexpectedToken`
  - e.g.: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **175x** `Uncaught TypeError: createRealm is not a function`
  - e.g.: `test/language/eval-code/indirect/realm.js`
- **145x** `SyntaxError: MissingSemicolon`
  - e.g.: `test/language/asi/do-while-same-line.js`
- **107x** `Uncaught TypeError: resize is not a function`
  - e.g.: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **76x** `Uncaught TypeError: undefined is not a function`
  - e.g.: `test/built-ins/Array/prototype/at/coerced-index-resize.js`
- **76x** `Uncaught { message: implements ArrayBuffer.prototype.resize Expected SameValue(«"undefined"», «"function"») to`
  - e.g.: `test/built-ins/DataView/prototype/getBigInt64/resizable-buffer.js`
- **70x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/language/expressions/optional-chaining/optional-call-preserves-this.js`
- **69x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - e.g.: `test/language/global-code/decl-lex-configurable-global.js`
- **57x** `Uncaught ReferenceError: ShadowRealm is not defined`
  - e.g.: `test/built-ins/ShadowRealm/extensibility.js`
- **54x** `async incomplete: SyntaxError: MissingSemicolon`
  - e.g.: `test/language/import/import-attributes/json-idempotency.js`
- **53x** `async incomplete: Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/built-ins/Atomics/waitAsync/false-for-timeout-agent.js`
- **38x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/expressions/assignment/target-super-computed-reference-null.js`
- **32x** `Uncaught { message: Expected SameValue(«undefined», «N») to be true }`
  - e.g.: `test/language/statementList/eval-block-with-statment-block.js`
- **32x** `Uncaught { message: The value of `typeof Atomics.waitAsync` is "function" Expected SameValue(«"undefined"», «"`
  - e.g.: `test/built-ins/Atomics/waitAsync/bad-range.js`
- **22x** `Engine error: StackOverflow`
  - e.g.: `test/language/expressions/tco-pos.js`
- **21x** `Uncaught { message: Expected SameValue(«"inside"», «"outside"») to be true }`
  - e.g.: `test/language/expressions/arrow-function/scope-paramsbody-var-open.js`
- **18x** `Uncaught TypeError: transferToImmutable is not a function`
  - e.g.: `test/built-ins/ArrayBuffer/prototype/resize/this-is-immutable-arraybuffer-object.js`
- **18x** `Uncaught { message: no arg factories match include immutable and exclude undefined }`
  - e.g.: `test/built-ins/Atomics/add/immutable-buffer.js`
- **16x** `SyntaxError: UnexpectedCharacter`
  - e.g.: `test/language/expressions/class/decorator/syntax/class-valid/decorator-member-expr-private-identifier.js`
- **16x** `Uncaught ReferenceError: await is not defined`
  - e.g.: `test/language/module-code/top-level-await/syntax/block-await-expr-template-literal.js`
- **16x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - e.g.: `test/language/statements/let/syntax/let-closure-inside-condition.js`
- **15x** `Uncaught { message: Expected a SyntaxError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/arguments-object/10.5-7-b-1-s.js`
- **12x** `async incomplete: Uncaught { message: The value of `typeof Atomics.waitAsync` is "function" Expected SameValue`
  - e.g.: `test/built-ins/Atomics/waitAsync/false-for-timeout.js`
- **11x** `Uncaught { message: Expected a TypeError but got a TestNError }`
  - e.g.: `test/language/expressions/member-expression/computed-reference-null-or-undefined.js`
- **11x** `Uncaught { message: Expected true but got false }`
  - e.g.: `test/language/expressions/postfix-decrement/S11.3.2_A6_T3.js`
- **11x** `Uncaught { message: Expected a RangeError but got a TypeError }`
  - e.g.: `test/built-ins/Array/prototype/toSpliced/length-exceeding-array-length-limit.js`
- **11x** `async incomplete: Uncaught TypeError: Promise.prototype.then called on a non-promise`
  - e.g.: `test/built-ins/Promise/all/invoke-resolve-on-promises-every-iteration-of-custom.js`
- **10x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - e.g.: `test/language/statements/class/elements/public-class-field-initialization-is-visible-to-proxy.js`
- **10x** `Uncaught RangeError: Invalid or out-of-range Temporal value`
  - e.g.: `test/built-ins/Temporal/Duration/compare/relativeto-string-limits.js`

## Top features present in FAILs

- 604x dynamic-import
- 388x resizable-arraybuffer
- 321x TypedArray
- 258x top-level-await
- 182x SharedArrayBuffer
- 177x Atomics
- 175x cross-realm
- 154x import-defer
- 149x BigInt
- 133x class
- 120x explicit-resource-management
- 117x Symbol
- 117x arrow-function
- 116x Reflect
- 101x Atomics.waitAsync
- 98x source-phase-imports
- 90x Proxy
- 84x ArrayBuffer
- 81x import-attributes
- 74x async-iteration
- 70x regexp-modifiers
- 64x immutable-arraybuffer
- 64x ShadowRealm
- 52x async-functions
- 47x Symbol.toPrimitive
