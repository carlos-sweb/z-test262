# Test262 — reporte de divergencias del motor z-*

Total: 47381 tests | corridos: 45639 | **PASS: 18256 (40.0% de los corridos)** | FAIL: 26656 | CRASH: 2 | TIMEOUT: 725 | SKIP (by design): 1742

> Nota: cubre el 100% de `test/language` + `test/built-ins`, incluyendo
> árboles totalmente fuera de alcance hoy (0% pass): `Temporal`,
> `TypedArray`+`TypedArrayConstructors`, `Atomics`, `DataView`,
> `SharedArrayBuffer`, `Proxy`+`Reflect`, `BigInt`, `WeakMap`/`WeakSet`/
> `WeakRef`/`FinalizationRegistry`, `ArrayBuffer`, etc. El % global no es
> comparable con ningún "subset comparable" más viejo por eso — usar
> `language/statements`/`language/expressions` (estables entre corridas)
> para tendencia real. **Barrido 2026-07-24 (tarde)**: baseline previo
> PASS 18208/45639 (39.9%) CRASH 2 → este barrido PASS 18256/45639
> (40.0%) CRASH 2 — mismos 2 crashes de siempre (`Map`/`Set.prototype.
> forEach` con delete-durante-iteración, bug latente ya documentado, no
> tocado hoy). La ganancia (+48) es casi toda `built-ins/String`+
> `Number`+`Boolean` (471+133+31 = 635 pass), consistente con el fix de
> hoy a `new String()`/`new Number()`/`new Boolean()` — antes esos
> wrappers tiraban TypeError en cualquier método.


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 0 | 25 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Array | 744 | 2275 | 0 | 26 | 36 | 24.4% |
| test/built-ins/ArrayBuffer | 0 | 221 | 0 | 0 | 0 | 0.0% |
| test/built-ins/ArrayIteratorPrototype | 0 | 19 | 0 | 0 | 8 | 0.0% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 3 | 22 | 0 | 13 | 0 | 7.9% |
| test/built-ins/AsyncFunction | 5 | 12 | 0 | 1 | 0 | 27.8% |
| test/built-ins/AsyncGeneratorFunction | 2 | 20 | 0 | 1 | 0 | 8.7% |
| test/built-ins/AsyncGeneratorPrototype | 0 | 47 | 0 | 1 | 0 | 0.0% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 0 | 387 | 0 | 0 | 2 | 0.0% |
| test/built-ins/BigInt | 0 | 77 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Boolean | 31 | 20 | 0 | 0 | 0 | 60.8% |
| test/built-ins/DataView | 0 | 561 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Date | 290 | 304 | 0 | 0 | 0 | 48.8% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 8 | 85 | 0 | 0 | 0 | 8.6% |
| test/built-ins/FinalizationRegistry | 0 | 47 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Function | 111 | 307 | 0 | 3 | 88 | 26.4% |
| test/built-ins/GeneratorFunction | 4 | 18 | 0 | 1 | 0 | 17.4% |
| test/built-ins/GeneratorPrototype | 14 | 46 | 0 | 1 | 0 | 23.0% |
| test/built-ins/Infinity | 2 | 2 | 0 | 0 | 2 | 50.0% |
| test/built-ins/Iterator | 7 | 505 | 0 | 2 | 0 | 1.4% |
| test/built-ins/JSON | 67 | 98 | 0 | 0 | 0 | 40.6% |
| test/built-ins/Map | 92 | 105 | 1 | 5 | 1 | 45.3% |
| test/built-ins/MapIteratorPrototype | 0 | 11 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Math | 78 | 246 | 0 | 3 | 0 | 23.9% |
| test/built-ins/NaN | 2 | 2 | 0 | 0 | 2 | 50.0% |
| test/built-ins/NativeErrors | 12 | 82 | 0 | 0 | 0 | 12.8% |
| test/built-ins/Number | 133 | 207 | 0 | 0 | 0 | 39.1% |
| test/built-ins/Object | 1562 | 1822 | 0 | 16 | 11 | 45.9% |
| test/built-ins/Promise | 154 | 572 | 0 | 0 | 3 | 21.2% |
| test/built-ins/Proxy | 0 | 300 | 0 | 0 | 11 | 0.0% |
| test/built-ins/Reflect | 0 | 153 | 0 | 0 | 0 | 0.0% |
| test/built-ins/RegExp | 467 | 1003 | 0 | 408 | 1 | 24.9% |
| test/built-ins/RegExpStringIteratorPrototype | 0 | 17 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Set | 175 | 205 | 1 | 1 | 1 | 45.8% |
| test/built-ins/SetIteratorPrototype | 0 | 11 | 0 | 0 | 0 | 0.0% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/String | 471 | 748 | 0 | 1 | 3 | 38.6% |
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
| test/built-ins/decodeURI | 0 | 32 | 0 | 23 | 0 | 0.0% |
| test/built-ins/decodeURIComponent | 0 | 36 | 0 | 20 | 0 | 0.0% |
| test/built-ins/encodeURI | 0 | 26 | 0 | 5 | 0 | 0.0% |
| test/built-ins/encodeURIComponent | 0 | 26 | 0 | 5 | 0 | 0.0% |
| test/built-ins/eval | 4 | 6 | 0 | 0 | 0 | 40.0% |
| test/built-ins/global | 22 | 7 | 0 | 0 | 0 | 75.9% |
| test/built-ins/isFinite | 4 | 11 | 0 | 0 | 0 | 26.7% |
| test/built-ins/isNaN | 4 | 11 | 0 | 0 | 0 | 26.7% |
| test/built-ins/parseFloat | 41 | 12 | 0 | 1 | 0 | 75.9% |
| test/built-ins/parseInt | 36 | 16 | 0 | 3 | 0 | 65.5% |
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
| test/language/expressions | 5964 | 4465 | 0 | 85 | 588 | 56.7% |
| test/language/function-code | 99 | 9 | 0 | 0 | 109 | 91.7% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 19 | 18 | 0 | 0 | 5 | 51.4% |
| test/language/identifier-resolution | 6 | 3 | 0 | 0 | 5 | 66.7% |
| test/language/identifiers | 230 | 12 | 0 | 26 | 0 | 85.8% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 36 | 5 | 0 | 0 | 0 | 87.8% |
| test/language/literals | 468 | 48 | 0 | 4 | 14 | 90.0% |
| test/language/module-code | 217 | 382 | 0 | 0 | 0 | 36.2% |
| test/language/punctuators | 10 | 1 | 0 | 0 | 0 | 90.9% |
| test/language/reserved-words | 26 | 0 | 0 | 1 | 0 | 96.3% |
| test/language/rest-parameters | 9 | 2 | 0 | 0 | 0 | 81.8% |
| test/language/source-text | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/language/statementList | 76 | 4 | 0 | 0 | 0 | 95.0% |
| test/language/statements | 5670 | 3127 | 0 | 68 | 472 | 64.0% |
| test/language/types | 88 | 16 | 0 | 0 | 9 | 84.6% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top causas de FAIL (mensaje normalizado)

- **2242x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/asi/S7.9_A10_T1.js`
- **1526x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet
error(DebugAllocator): memory`
  - ej: `test/language/arguments-object/10.6-11-b-1.js`
- **1248x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet
error(Debug`
  - ej: `test/language/expressions/async-generator/expression-await-as-yield-operand.js`
- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/expressions/async-function/named-returns-async-function-returns-newtarget.js`
- **518x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **400x** `Uncaught [object]`
  - ej: `test/language/arguments-object/S10.6_A3_T1.js`
- **392x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')
error(DebugAllocator): memory address Nx`
  - ej: `test/language/arguments-object/10.6-13-c-3-s.js`
- **372x** `SyntaxError: InvalidUnicodeEscape`
  - ej: `test/language/expressions/class/decorator/syntax/class-valid/decorator-member-expr-private-identifier.js`
- **302x** `SyntaxError: UnexpectedCharacter`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **211x** `Uncaught [object]
error(DebugAllocator): memory address NxNfNcN leaked: 
/home/sweb/.local/share/mise/installs`
  - ej: `test/language/computed-property-names/class/static/getter-prototype.js`
- **200x** `async incomplete: Uncaught [object]`
  - ej: `test/language/expressions/async-function/named-strict-error-reassign-fn-name-in-body-in-arrow.js`
- **196x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **191x** `Uncaught ReferenceError: Temporal is not defined
error(DebugAllocator): memory address NxNfNcN leaked: 
/home/`
  - ej: `test/built-ins/Temporal/getOwnPropertyNames.js`
- **172x** `async incomplete: SyntaxError: InvalidUnicodeEscape`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-static-async-generator-method-privatename-identifier.js`
- **156x** `async incomplete: SyntaxError: UnexpectedCharacter`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-static-async-generator-method-privatename-identifier-alt.js`
- **113x** `Uncaught ReferenceError: FloatNArray is not defined
error(DebugAllocator): memory address NxNfNcN leaked: 
/ho`
  - ej: `test/built-ins/Array/prototype/reduce/callbackfn-resize-arraybuffer.js`
- **110x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-function/nameless-dflt-params-ref-self.js`
- **109x** `Uncaught TypeError: Array.prototype.reduceRight called on a non-array
error(DebugAllocator): memory address Nx`
  - ej: `test/built-ins/Array/prototype/reduceRight/15.4.4.22-8-b-ii-1.js`
- **108x** `Uncaught [object]
error(DebugAllocator): memory address NxNfNcNcN leaked: 
/home/sweb/.local/share/mise/instal`
  - ej: `test/language/expressions/arrow-function/dstr/dflt-obj-ptrn-id-init-fn-name-cover.js`
- **108x** `Uncaught [object]
error(DebugAllocator): memory address NxNfNaNcN leaked: 
/home/sweb/.local/share/mise/instal`
  - ej: `test/language/expressions/assignment/dstr/array-elem-trlg-iter-elision-iter-nrml-close-null.js`
- **105x** `Uncaught [object]
error(DebugAllocator): memory address NxNfNeNcN leaked: 
/home/sweb/.local/share/mise/instal`
  - ej: `test/language/expressions/arrow-function/dstr/dflt-ary-ptrn-elem-id-init-fn-name-arrow.js`
- **103x** `Uncaught ReferenceError: Temporal is not defined
error(DebugAllocator): memory address NxNfNcNcN leaked: 
/hom`
  - ej: `test/built-ins/Temporal/Duration/years-undefined.js`
- **90x** `Uncaught ReferenceError: Temporal is not defined
error(DebugAllocator): memory address NxNfNaNcN leaked: 
/hom`
  - ej: `test/built-ins/Temporal/Duration/prototype/round/branding.js`
- **88x** `Uncaught ReferenceError: Temporal is not defined
error(DebugAllocator): memory address NxNfN leaked: 
/home/sw`
  - ej: `test/built-ins/Temporal/Duration/months-undefined.js`
- **86x** `Uncaught ReferenceError: FloatNArray is not defined
error(DebugAllocator): memory address NxNfNeNcN leaked: 
/`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-Float64Array.js`
- **83x** `Uncaught ReferenceError: Temporal is not defined
error(DebugAllocator): memory address NxNfNeNcN leaked: 
/hom`
  - ej: `test/built-ins/Temporal/Duration/compare/relativeto-propertybag-invalid.js`
- **81x** `Uncaught TypeError: Array.prototype.lastIndexOf called on a non-array
error(DebugAllocator): memory address Nx`
  - ej: `test/built-ins/Array/prototype/lastIndexOf/15.4.4.15-1-6.js`
- **79x** `Uncaught ReferenceError: Temporal is not defined
error(DebugAllocator): memory address NxNfNbNcN leaked: 
/hom`
  - ej: `test/built-ins/Temporal/Duration/subclass.js`
- **76x** `Uncaught [object]
error(DebugAllocator): memory address NxNfNdNcN leaked: 
/home/sweb/.local/share/mise/instal`
  - ej: `test/language/expressions/async-generator/named-dflt-params-abrupt.js`
- **76x** `Uncaught ReferenceError: FloatNArray is not defined
error(DebugAllocator): memory address NxNfNaNcN leaked: 
/`
  - ej: `test/built-ins/Atomics/and/non-shared-bufferdata.js`

## Top features presentes en FAILs

- 4611x Temporal
- 2489x TypedArray
- 2239x class
- 2079x async-iteration
- 1938x destructuring-binding
- 1861x generators
- 1525x class-fields-public
- 1419x BigInt
- 1223x Symbol
- 1081x Symbol.iterator
- 714x default-parameters
- 675x class-static-methods-private
- 639x class-methods-private
- 604x dynamic-import
- 548x class-fields-private
- 531x arrow-function
- 490x Symbol.asyncIterator
- 462x resizable-arraybuffer
- 459x SharedArrayBuffer
- 455x Proxy
- 447x Reflect
- 446x Reflect.construct
- 386x iterator-helpers
- 382x Atomics
- 356x explicit-resource-management

## CRASHES (los más graves)

- **2x** `exit -N: thread N panic: switch on corrupt value
/home/sweb/z-value/src/zvalue.zig:N:N: NxNcN in retain (zvalu`
  - ej: `test/built-ins/Map/prototype/forEach/deleted-values-during-foreach.js`
