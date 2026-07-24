# Test262 — reporte de divergencias del motor z-*

Total: 47381 tests | corridos: 45639 | **PASS: 18208 (39.9% de los corridos)** | FAIL: 26808 | CRASH: 2 | TIMEOUT: 621 | SKIP (by design): 1742

> Nota: este es el primer barrido que cubre el **100%** de `test/language` +
> `test/built-ins` (47381 archivos vs. 36894 en el barrido anterior). El total
> sube porque ahora se incluyen árboles previamente no barridos y totalmente
> fuera de alcance hoy (0% pass): `Temporal` (4603), `TypedArray`+
> `TypedArrayConstructors` (2160), `Atomics` (389), `DataView` (561),
> `SharedArrayBuffer`+`Uint8Array` (174), `Proxy`+`Reflect` (464), `BigInt`
> (77), `WeakMap`/`WeakSet`/`WeakRef`/`FinalizationRegistry` (302),
> `AggregateError`/`SuppressedError`/`Disposable*Stack`/`ShadowRealm`,
> `ArrayBuffer` (221). El % global de esta corrida **no es comparable
> directamente** con el histórico "subset comparable" de abajo por eso — usar
> las áreas `language/statements`/`language/expressions` (estables entre
> corridas) o esa tabla para tendencia real.


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 0 | 25 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Array | 745 | 2275 | 0 | 25 | 36 | 24.5% |
| test/built-ins/ArrayBuffer | 0 | 221 | 0 | 0 | 0 | 0.0% |
| test/built-ins/ArrayIteratorPrototype | 0 | 19 | 0 | 0 | 8 | 0.0% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 3 | 22 | 0 | 13 | 0 | 7.9% |
| test/built-ins/AsyncFunction | 5 | 13 | 0 | 0 | 0 | 27.8% |
| test/built-ins/AsyncGeneratorFunction | 2 | 21 | 0 | 0 | 0 | 8.7% |
| test/built-ins/AsyncGeneratorPrototype | 0 | 47 | 0 | 1 | 0 | 0.0% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 0 | 387 | 0 | 0 | 2 | 0.0% |
| test/built-ins/BigInt | 0 | 77 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Boolean | 30 | 21 | 0 | 0 | 0 | 58.8% |
| test/built-ins/DataView | 0 | 561 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Date | 290 | 304 | 0 | 0 | 0 | 48.8% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 8 | 85 | 0 | 0 | 0 | 8.6% |
| test/built-ins/FinalizationRegistry | 0 | 47 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Function | 111 | 310 | 0 | 0 | 88 | 26.4% |
| test/built-ins/GeneratorFunction | 4 | 19 | 0 | 0 | 0 | 17.4% |
| test/built-ins/GeneratorPrototype | 14 | 46 | 0 | 1 | 0 | 23.0% |
| test/built-ins/Infinity | 2 | 2 | 0 | 0 | 2 | 50.0% |
| test/built-ins/Iterator | 7 | 507 | 0 | 0 | 0 | 1.4% |
| test/built-ins/JSON | 67 | 98 | 0 | 0 | 0 | 40.6% |
| test/built-ins/Map | 92 | 105 | 1 | 5 | 1 | 45.3% |
| test/built-ins/MapIteratorPrototype | 0 | 11 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Math | 81 | 246 | 0 | 0 | 0 | 24.8% |
| test/built-ins/NaN | 2 | 2 | 0 | 0 | 2 | 50.0% |
| test/built-ins/NativeErrors | 12 | 82 | 0 | 0 | 0 | 12.8% |
| test/built-ins/Number | 131 | 209 | 0 | 0 | 0 | 38.5% |
| test/built-ins/Object | 1562 | 1822 | 0 | 16 | 11 | 45.9% |
| test/built-ins/Promise | 154 | 572 | 0 | 0 | 3 | 21.2% |
| test/built-ins/Proxy | 0 | 300 | 0 | 0 | 11 | 0.0% |
| test/built-ins/Reflect | 0 | 153 | 0 | 0 | 0 | 0.0% |
| test/built-ins/RegExp | 468 | 1009 | 0 | 401 | 1 | 24.9% |
| test/built-ins/RegExpStringIteratorPrototype | 0 | 17 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Set | 175 | 205 | 1 | 1 | 1 | 45.8% |
| test/built-ins/SetIteratorPrototype | 0 | 11 | 0 | 0 | 0 | 0.0% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/String | 393 | 827 | 0 | 0 | 3 | 32.2% |
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
| test/built-ins/decodeURI | 0 | 54 | 0 | 1 | 0 | 0.0% |
| test/built-ins/decodeURIComponent | 0 | 55 | 0 | 1 | 0 | 0.0% |
| test/built-ins/encodeURI | 0 | 31 | 0 | 0 | 0 | 0.0% |
| test/built-ins/encodeURIComponent | 0 | 31 | 0 | 0 | 0 | 0.0% |
| test/built-ins/eval | 4 | 6 | 0 | 0 | 0 | 40.0% |
| test/built-ins/global | 22 | 7 | 0 | 0 | 0 | 75.9% |
| test/built-ins/isFinite | 4 | 11 | 0 | 0 | 0 | 26.7% |
| test/built-ins/isNaN | 4 | 11 | 0 | 0 | 0 | 26.7% |
| test/built-ins/parseFloat | 42 | 12 | 0 | 0 | 0 | 77.8% |
| test/built-ins/parseInt | 39 | 16 | 0 | 0 | 0 | 70.9% |
| test/built-ins/undefined | 2 | 3 | 0 | 0 | 3 | 40.0% |
| test/language/arguments-object | 189 | 17 | 0 | 0 | 57 | 91.7% |
| test/language/asi | 98 | 4 | 0 | 0 | 0 | 96.1% |
| test/language/block-scope | 144 | 1 | 0 | 0 | 0 | 99.3% |
| test/language/comments | 44 | 8 | 0 | 0 | 0 | 84.6% |
| test/language/computed-property-names | 28 | 20 | 0 | 0 | 0 | 58.3% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 92 | 35 | 0 | 0 | 220 | 72.4% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 5963 | 4467 | 0 | 84 | 588 | 56.7% |
| test/language/function-code | 99 | 9 | 0 | 0 | 109 | 91.7% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 19 | 18 | 0 | 0 | 5 | 51.4% |
| test/language/identifier-resolution | 6 | 3 | 0 | 0 | 5 | 66.7% |
| test/language/identifiers | 256 | 12 | 0 | 0 | 0 | 95.5% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 36 | 5 | 0 | 0 | 0 | 87.8% |
| test/language/literals | 468 | 48 | 0 | 4 | 14 | 90.0% |
| test/language/module-code | 217 | 382 | 0 | 0 | 0 | 36.2% |
| test/language/punctuators | 10 | 1 | 0 | 0 | 0 | 90.9% |
| test/language/reserved-words | 27 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/rest-parameters | 9 | 2 | 0 | 0 | 0 | 81.8% |
| test/language/source-text | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/language/statementList | 76 | 4 | 0 | 0 | 0 | 95.0% |
| test/language/statements | 5667 | 3130 | 0 | 68 | 472 | 63.9% |
| test/language/types | 88 | 16 | 0 | 0 | 9 | 84.6% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |

## Top causas de FAIL (mensaje normalizado)

- **6062x** `Uncaught [object]`
  - ej: `test/language/arguments-object/10.5-1-s.js`
- **4016x** `Uncaught ReferenceError: Temporal is not defined`
  - ej: `test/built-ins/Temporal/getOwnPropertyNames.js`
- **3768x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/arguments-object/10.6-11-b-1.js`
- **2076x** `Uncaught ReferenceError: FloatNArray is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-Float32Array.js`
- **1358x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-arrow-function/dflt-params-ref-self.js`
- **576x** `Uncaught ReferenceError: ArrayBuffer is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-ArrayBuffer.js`
- **560x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **518x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/comments/hashbang/line-terminator-line-separator.js`
- **467x** `Uncaught ReferenceError: Proxy is not defined`
  - ej: `test/language/expressions/class/elements/fields-multiple-definitions-static-private-methods-proxy.js`
- **392x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/arguments-object/10.6-13-c-3-s.js`
- **372x** `SyntaxError: InvalidUnicodeEscape`
  - ej: `test/language/expressions/class/decorator/syntax/class-valid/decorator-member-expr-private-identifier.js`
- **322x** `Uncaught ReferenceError: Iterator is not defined`
  - ej: `test/built-ins/Iterator/length.js`
- **302x** `SyntaxError: UnexpectedCharacter`
  - ej: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **280x** `Uncaught ReferenceError: UintNArray is not defined`
  - ej: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **265x** `async incomplete: Uncaught [object]`
  - ej: `test/language/expressions/async-arrow-function/dflt-params-trailing-comma.js`
- **232x** `Uncaught TypeError: Cannot convert undefined or null to object`
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
- **136x** `Uncaught TypeError: expression is not a function`
  - ej: `test/language/statements/for-of/Array.prototype.Symbol.iterator.js`
- **123x** `Uncaught ReferenceError: SharedArrayBuffer is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-SharedArrayBuffer.js`
- **122x** `Uncaught ReferenceError: Reflect is not defined`
  - ej: `test/language/expressions/class/elements/private-methods/prod-private-generator.js`
- **111x** `Uncaught TypeError: Array.prototype.reduce called on a non-array`
  - ej: `test/built-ins/Array/prototype/reduce/15.4.4.21-1-10.js`
- **109x** `Uncaught TypeError: Array.prototype.reduceRight called on a non-array`
  - ej: `test/built-ins/Array/prototype/reduceRight/15.4.4.22-1-10.js`
- **91x** `Uncaught ReferenceError: WeakMap is not defined`
  - ej: `test/language/expressions/class/subclass-builtins/subclass-WeakMap.js`
- **89x** `Uncaught ReferenceError: Atomics is not defined`
  - ej: `test/built-ins/Atomics/add/name.js`
- **88x** `Uncaught TypeError: Array.prototype.filter called on a non-array`
  - ej: `test/built-ins/Array/prototype/filter/15.4.4.20-3-19.js`
- **86x** `Uncaught TypeError: Array.prototype.some called on a non-array`
  - ej: `test/built-ins/Array/prototype/some/15.4.4.17-1-4.js`

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
- 532x arrow-function
- 490x Symbol.asyncIterator
- 462x resizable-arraybuffer
- 459x SharedArrayBuffer
- 455x Proxy
- 449x Reflect.construct
- 448x Reflect
- 386x iterator-helpers
- 382x Atomics
- 356x explicit-resource-management

## CRASHES (los más graves)

- **2** crashes conocidos (2026-07-24): `test/built-ins/Map/prototype/forEach/deleted-values-during-foreach.js`
  y `test/built-ins/Set/prototype/forEach/iterates-values-revisits-after-delete-re-add.js`,
  ambos `switch on corrupt value` en `z-value/src/zvalue.zig:207` (`retain`).
  **Pre-existentes, no regresión de esta fase** — verificado con git stash:
  crashean igual con los cambios de async generators revertidos. Clase de bug
  ya vista antes (colgante durante mutación mid-iteración); esta vez en
  `Map`/`Set.prototype.forEach` con delete+re-add, no en `for-of`. Sin tocar
  todavía.
---

## Análisis (actualizado 2026-07-24, async generators)

### Delta 2026-07-24: ASYNC GENERATORS / `for await` / `Symbol.asyncIterator` (segundo bucket más grande)

Runtime completo para `async function*`/`async *método(){}` (la gramática ya
parseaba desde la fase de generators/async; solo faltaba la evaluación) y
gramática+evaluación de `for await (... of ...)`. Cambios: z-statements
(`ForHead.for_of.is_await`, contextual `await` tras `for` gateado por el
mismo `await_allowed` que ya gatea el operador `await`), z-interpreter
(`FiberState.kind` enum → `is_generator`/`is_async` bools ortogonales;
`resumeFiber` gana un post-check que liquida `pending_result_promise` cuando
el fiber yieldea/completa/lanza; `awaitValue` extraído y reusado por
`.await_expr` y por `.yield_expr` de un generador async — AsyncGeneratorYield
hace un Await implícito del valor antes de exponerlo; `makeAsyncGeneratorObject`
+ `asyncGeneratorNext`; `evalForOf` awaitea cada valor producido, de
cualquier forma de iterable, cuando `is_await`; `resolveAsyncIterator` prueba
`Symbol.asyncIterator` y cae a `Symbol.iterator`/duck-typing si no existe).
También se encontró y arregló un gap preexistente no relacionado que
enmascaraba la medición: faltaba el global `print()` que usa el harness
estándar de Test262 para tests async (`doneprintHandle.js`/`$DONE`) — sin él,
NINGÚN test async-harness terminaba de reportar su resultado, en cualquier
área, no solo async generators. Ya arreglado (`builtins.zig`).

Deltas (comparando con/sin los cambios vía git stash, mismo barrido):
- **Dirs específicos de async-generator** (`language/{statements,expressions}/async-generator`,
  `language/statements/for-await-of`, `built-ins/{AsyncGeneratorFunction,
  AsyncGeneratorPrototype,AsyncIteratorPrototype,AsyncFromSyncIteratorPrototype}`,
  2280 tests): **11.7% → 58.8%** (+1074).
- **language/statements: 4334 → 5667 (+1333, 48.9% → 63.9%)**
- **language/expressions: 5228 → 5963 (+735, 49.7% → 56.7%)**
- **0 regresiones**: los 2 CRASH que aparecen en el barrido completo
  (`Map`/`Set.prototype.forEach` con delete-durante-iteración) son
  **pre-existentes**, verificado con el mismo git stash — nada que ver con
  esta fase (bug latente en `zvalue.zig:207` `retain`, ver sección CRASHES).
- Feature `async-iteration` en FAILs: 4027x → 2079x. `Symbol.asyncIterator`:
  534x → 490x.

Node-verificado exhaustivamente: yield síncrono y `await` intercalados dentro
del mismo generador async (orden confirmado con log de efectos secundarios
en múltiples `.next()`), `for await` sobre async-generator/array-de-promesas/
objeto con solo `Symbol.iterator` (fallback), método `async *` de clase con
`this`/campos privados, propagación de excepción a través de `for await`.
Suites: z-statements (3 tests nuevos de gramática `for await`) y
z-interpreter (`tests/async_generator_test.zig` nuevo, 7 tests) en verde.

**Fuera de alcance (documentado, mismo narrowing que generators/async
síncronos)**: `yield*` delegado async-aware (sigue la delegación síncrona
actual), `AsyncGenerator.prototype.return()`/`.throw()` (el generator
síncrono tampoco los tiene), overlapping `.next()` sin esperar el anterior
(un solo request en vuelo — el patrón que usa `for await`, que nunca
solapa), top-level await. Esto explica buena parte del `NotImplemented`
restante en los dirs `yield-star*`/`yield-spread*` de async-generator.

### Delta 2026-07-20 (10): CLASES MODERNAS — el bucket #1 (+1461)

Gramática y runtime completos para clases modernas: **class fields**
(públicos/privados/estáticos, con/sin init), **`#private`** (fields, métodos,
accessors, estáticos, `#x in obj` brand checks), **computed keys** (evaluadas
una vez en orden, con soporte de Symbol keys → `*[Symbol.iterator]()` hace
clases iterables), **numeric keys**, y **static blocks**. Cambios coordinados:
z-functions (AST ClassKey/ClassElement + gramática con lookahead de
modificadores ampliado), z-parser (`.#x` member + `#x in`), z-interpreter
(PrivateEnvironment como identidad ClassCtx + claves reservadas `\x00P`,
orden spec de field-init base/derivada vía pending-super, intercepción de
get/set/call/in/delete privados; fibers transportan private_ctx para métodos
async/gen privados). Trailing commas ya funcionaban (los tests así nombrados
fallaban por las features de clase).

Deltas (mismo run): **statements 3612→4334 (+722, 40.8→48.9%)**,
**expressions 4489→5228 (+739, 40.4→49.7%)** = **+1461, 0 crashes**. Los dirs
class/: 2506→3760 (+1254). Node-verificado exhaustivamente (orden de fields,
brand errors, getters/setters privados, static blocks, frozen-this).
Narrowing documentado: `delete this.#x` es SyntaxError en runtime (no early),
async generators siguen fuera (siguiente palanca, ~4500).

### Delta 2026-07-20 (9): eval (Fase A) — eval-code 10 -> 92 (+82)

`eval` cableado reusando `zfunctions.Parser` + `evalBody`: el global `eval`
(indirecto) corre en scope global; `evalCall` detecta el `eval(...)` literal
(intrínseco no shadow-eado) como eval DIRECTO y corre en un hijo del scope del
llamador (always-strict ⇒ scope propio). Arg no-string se devuelve tal cual;
error de parse ⇒ SyntaxError atrapable; excepciones propagan. language/eval-code
10→92 (+82), 0 crashes (220 SKIP = noStrict por diseño). Node-verificado. Fuera
de alcance: realm/$262, var-leaking sloppy. (Falta Fase B: Proxy.)

### Delta 2026-07-20 (8): for-of iteración viva (crashes -> 0)

El bucle `for-of` sobre array/set/map cacheaba el slice/entries, así que un
cuerpo que mutaba el contenedor (`array.pop()`, `set.delete()`) dejaba una
lectura colgante ("switch on corrupt value"). Ahora los tres iteran en vivo
(re-leen longitud/keys cada paso y retienen el elemento), observando la
mutación como ArrayIterator/SetIterator/MapIterator del spec. language/
statements 3606→3612, CRASH 2→0. Node-verificado (array/set/map-contract y
variantes expand/contract).

### Delta 2026-07-20 (7): globalThis (+20 en el subset medido)

`globalThis` cableado como objeto respaldado por el entorno global: sus lecturas
resuelven bindings globales (`globalThis.Object`, `globalThis.parseInt`) y las
escrituras crean globales (`globalThis.x = 1` -> `x` global); `globalThis.globalThis
=== globalThis`. Delta medido: expressions 4481→4489, statements 3594→3606.
Node-verificado (salvo el prototipo host-específico de globalThis, que no es
spec). Los 2 crashes de statements/for-of (array/set-contract) son PRE-EXISTENTES
(verificado con git stash) -- misma clase iteración+mutación que ya se limpió en
los métodos de Array; el bucle `for-of` cachea el slice. Follow-up.

### Delta 2026-07-20 (6): reflexión sobre más tipos (+128)

`Object.defineProperty`/`defineProperties`/`getOwnPropertyNames` aceptan ahora
funciones (vía el statics bag, con descriptores completos) y arrays
(index/length por valor -- best-effort, sin descriptores por-elemento; named
keys vía el array_props object). Añadidos los estáticos faltantes `Object.is`
(SameValue), `Object.hasOwn`, `Object.fromEntries` (arrays de pares).
built-ins/Object 1437→1562, arguments-object 86→89 (+128, 0 crashes).
Node-verificado. Gap restante: descriptores por-elemento de arrays.

### Delta 2026-07-20 (5): métodos de instancia Number/Boolean (+63)

Number.prototype (toString(radix)/toFixed/toExponential/toPrecision/valueOf/
toLocaleString) y Boolean.prototype (toString/valueOf) cableados sobre el
receptor primitivo (delegando a z-number FormattingMethods; RangeErrors
correctos). Number 76→131, Boolean 21→29 (+63, 0 crashes). Narrowing: los
wrappers `new Number()`/`new Boolean()` (objeto hueco sin [[NumberData]]) no
soportan estos métodos. Node-verificado.

### Delta 2026-07-20 (4): estáticos/constantes builtin non-enumerable (+89)

Los estáticos builtin (Object.keys, Date.now, Array.isArray, Math.floor,
Promise.resolve, …) y las constantes (Number.MAX_SAFE_INTEGER, Math.PI, los
well-known Symbols) se registraban con `.set` (enumerable) en vez de con los
atributos spec. Ahora: métodos → non-enumerable/writable/configurable
(`dneMethod`), constantes → non-enumerable/non-writable/non-configurable
(`dneConst`). `Object.keys`/`values`/`entries` aceptan funciones (devuelven los
estáticos enumerables del bag, ahora ninguno) → `Object.keys(Date)` === []. Con
esto `verifyProperty` sobre constructores/namespaces pasa. Deltas: Object
1383→1437, Number 58→76, Promise 34→42, Boolean 17→21, Math 78→81, Symbol
17→19 (**+89**, 0 crashes). Node-verificado.

### Delta 2026-07-20 (3): limpieza de crashes latentes de Array/String (29 → 0)

Los 29 crashes que la capa de descriptores dejó alcanzables (18 Array, 11
String) están arreglados: **Array CRASH 18→0** (PASS 699→714), **String
CRASH 11→0** (PASS 374→387). Dos clases:
- **`@intFromFloat` sobre NaN/Infinity/huge** en repeat/padStart/padEnd/
  codePointAt/fromCharCode/fromCodePoint/splice/flat/copyWithin/at/from y
  `normIndex`: helper `toIntSat` (ToIntegerOrInfinity saturado, NaN→0) + los
  RangeError correctos (repeat Inf/neg, fromCodePoint fuera de rango).
- **Slice cacheado colgante** cuando el callback muta el array mid-loop
  (map/filter/forEach/reduce/some/every/find/findIndex/findLast/reduceRight/
  flatMap): ahora iteran por índice contra el array vivo con `liveElem`
  (retiene el elemento durante el callback; captura `len` una vez, salta
  índices removidos). Node-verificado.

### Delta 2026-07-20 (2): prototipos builtin reales + capa de descriptores (+590)

Fundación completa: los métodos builtin ahora viven en **objetos prototipo
reales** (`Object.prototype`, `Array.prototype`, `Date.prototype`, …) como
own-props con atributos spec (writable, non-enumerable, configurable), en vez
de despacharse por `StaticStringMap`. Los objetos ordinarios encadenan a
`Object.prototype`; el lookup por tipo camina el prototipo real; y la reflexión
(`getOwnPropertyDescriptor` sobre objetos **y funciones**, `getPrototypeOf`,
`hasOwnProperty` sobre arrays/strings) opera sobre ellos. Identidad
`[].push === Array.prototype.push` y `Object.create(null)` (no hereda nada)
correctas.

Deltas (mismo run):
- **built-ins/Object 1183 → 1383** (+200, 34.8% → 40.5%)
- **built-ins/Date 148 → 290** (+142, 24.9% → 48.8%)
- **built-ins/String 292 → 374** (+82, 23.9% → 30.6%)
- **built-ins/Array 616 → 699** (+83, 20.2% → 22.7%)
- **language/expressions 4398 → 4481** (+83)
- **Total +590 tests.**

Los 18 crashes de Array y 11 de String son **pre-existentes** (verificado con
git stash: crashean igual en la versión previa) — bugs latentes de
`@intFromFloat` (splice/repeat/padStart/copyWithin/…) y un "switch on corrupt
value" en tests con accessors/mutación-durante-loop, que ahora se **alcanzan**
porque los tests progresan más lejos. No son regresión de este cambio.
Follow-up: aplicar el mismo saturado NaN/rango que ya se usó en Date/lastIndex.

Follow-ups de esta capa: estáticos builtin non-enumerable (hoy enumerable via
el property bag); métodos de instancia de Number/Boolean; `typeof
Function.prototype` === 'function' (exótico); objetos de JSON.parse encadenados.

### Delta 2026-07-20: Date completado (5.2% → 24.9%)

Se completó la API de `Date` en el intérprete (z-interpreter, sin tocar
z-date/z-value que ya estaban listos): todos los getters local+UTC, todos los
setters local+UTC (con guardas NaN/rango → Invalid Date, sin panics), formatters
(`toString`/`toDateString`/`toTimeString`/`toUTCString`/`toGMTString`/`toJSON`/
`toLocale*`/`valueOf`), estáticos (`now`/`parse`/`UTC`), constructor multi-arg y
`new Date(dateValue)`. `ToString(date)` ahora usa `toString()` (no ISO).
Barrido `test/built-ins/Date`: **PASS 31 → 148 (5.2% → 24.9%)**, 0 crashes.

Los FAIL restantes NO son de la lógica de Date sino de la **capa de reflexión
compartida**: ~208 `verifyProperty`, ~100 `Object.getOwnPropertyDescriptor`
sobre `Date.prototype` (los métodos se despachan por un StaticStringMap, no son
own-props reales), ~104 features no implementadas. Es la misma palanca que
subiría Object/Array/String: **hacer que los prototipos builtin sean objetos
reales con descriptores**.

### Delta 2026-07-19 (post-fixes): CRASH → 0

Barrido de `test/built-ins/RegExp` (1879 tests): **CRASH 2 → 0**, PASS
456 → 458, FAIL/TIMEOUT sin cambios. Tres crashes arreglados:

1. **Cuantificador anulable** (`/(a?b??)*/`, `(a?)+`, `(a*)*` …) —
   desbordaba la pila por recursión infinita. Fix en z-regex
   `recursive_matcher.zig`: guarda de progreso-cero (`matchBackEdge`) que
   descarta la iteración vacía (regla ECMA-262), cubriendo ambas formas de
   back-edge (GOTO del star, rama SPLIT del plus). `[0]` siempre correcto;
   queda una divergencia documentada en el *valor de captura* de una
   iteración vacía descartada (fix pleno = RepeatMatcher con contador).
2. **Cuantificador enorme** (`b{9007199254740991}`) — panic por overflow
   u32 al desenrollar `min`. Fix en z-regex `lexer.zig`: acumulación
   saturada + `MAX_REPEAT_UNROLL = 2**16` (max→∞, min acotado; estilo RE2).
3. **`lastIndex` fuera de rango** (Infinity/MAX_VALUE/2**53) — panic
   float→int en `exec`. Fix en z-interpreter: conversión saturada + se
   agregaron `Number.MAX_VALUE/MIN_VALUE/POSITIVE_INFINITY/NEGATIVE_INFINITY`.

### Delta de esta fase

z-regex cableado: regex literals, RegExp, y String match/matchAll/search/
replace/replaceAll/split con regex. Subconjunto comparable: **37.0% →
37.4% (+130 tests)**. built-ins/RegExp 0→30.1%, built-ins/String
20.2→23.9%, language/literals →88.8% (los regex literals ya evalúan).

**REGRESIÓN: CRASH 0 → 1.** El patrón `/(a?b??)*/` (cuantificador
anulable bajo `*`) SIGSEGVea el RecursiveMatcher de z-regex — NO respeta
la regla del spec "una iteración opcional que matchea vacío se descarta",
y recursiona sin fondo. Es un **bug del motor z-regex** que el cableado
expuso (el wiring en sí es correcto: 342/342 en z-interpreter, idéntico a
Node en todo lo probado). **Prioridad #1: arreglar los cuantificadores
anulables en z-regex** (su propia fase). Es el único input conocido que
vuelve a crashear el motor desde JS.

### Historial (subset comparable)

| corrida | PASS |
|---|---|
| baseline 2026-07-18 | 23.7% |
| descriptors + constructores | 31.9% |
| gramática gen/async | 33.6% |
| arguments | 34.2% |
| Symbol + iterator | 35.9% |
| Array/String coverage | 36.9% |
| Map/Set | 37.0% |
| regex (z-regex wired) | **37.4%** (RegExp dir 0→30%) |

### Prioridades restantes

1. ~~z-regex: cuantificadores anulables~~ ✅ ARREGLADO (2026-07-19) junto
   con los otros 2 crashes de la fase regex. Ver "Delta post-fixes".
2. Well-known symbols cableados (toPrimitive/hasInstance/toStringTag).
3. Class fields (`x = 1`, `#private`), computed method keys.
4. Exotic semantics (sparse arrays, length/prop descriptors, this-coercion
   genérico) para subir built-ins/Array/String/Object/RegExp.
5. Bug ASI do-while.
