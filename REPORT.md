# Test262 — reporte de divergencias del motor z-*

Total: 36894 tests | corridos: 35204 | **PASS: 13100 (37.2% de los corridos)** | FAIL: 21797 | CRASH: 1 | TIMEOUT: 306 | SKIP (by design): 1690


## Pass-rate por área

| área | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/built-ins/Array | 714 | 2310 | 0 | 21 | 36 | 23.2% |
| test/built-ins/Boolean | 29 | 22 | 0 | 0 | 0 | 56.9% |
| test/built-ins/Date | 290 | 304 | 0 | 0 | 0 | 48.8% |
| test/built-ins/Error | 4 | 89 | 0 | 0 | 0 | 4.3% |
| test/built-ins/Function | 79 | 342 | 0 | 0 | 88 | 18.8% |
| test/built-ins/JSON | 65 | 100 | 0 | 0 | 0 | 39.4% |
| test/built-ins/Map | 80 | 120 | 0 | 3 | 1 | 39.4% |
| test/built-ins/Math | 81 | 246 | 0 | 0 | 0 | 24.8% |
| test/built-ins/NativeErrors | 12 | 82 | 0 | 0 | 0 | 12.8% |
| test/built-ins/Number | 131 | 209 | 0 | 0 | 0 | 38.5% |
| test/built-ins/Object | 1562 | 1838 | 0 | 0 | 11 | 45.8% |
| test/built-ins/Promise | 42 | 684 | 0 | 0 | 3 | 5.8% |
| test/built-ins/RegExp | 640 | 1031 | 1 | 206 | 1 | 34.1% |
| test/built-ins/Set | 166 | 215 | 0 | 1 | 1 | 43.5% |
| test/built-ins/String | 387 | 833 | 0 | 0 | 3 | 31.6% |
| test/built-ins/Symbol | 19 | 77 | 0 | 0 | 2 | 19.8% |
| test/language/arguments-object | 89 | 117 | 0 | 0 | 57 | 43.2% |
| test/language/asi | 98 | 4 | 0 | 0 | 0 | 96.1% |
| test/language/block-scope | 144 | 1 | 0 | 0 | 0 | 99.3% |
| test/language/comments | 38 | 14 | 0 | 0 | 0 | 73.1% |
| test/language/computed-property-names | 12 | 36 | 0 | 0 | 0 | 25.0% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 10 | 117 | 0 | 0 | 220 | 7.9% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 4481 | 5985 | 0 | 48 | 588 | 40.4% |
| test/language/function-code | 90 | 18 | 0 | 0 | 109 | 83.3% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 19 | 18 | 0 | 0 | 5 | 51.4% |
| test/language/identifier-resolution | 6 | 3 | 0 | 0 | 5 | 66.7% |
| test/language/identifiers | 200 | 68 | 0 | 0 | 0 | 74.6% |
| test/language/import | 13 | 115 | 0 | 0 | 0 | 10.2% |
| test/language/keywords | 25 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/line-terminators | 27 | 14 | 0 | 0 | 0 | 65.9% |
| test/language/literals | 462 | 58 | 0 | 0 | 14 | 88.8% |
| test/language/module-code | 217 | 382 | 0 | 0 | 0 | 36.2% |
| test/language/punctuators | 10 | 1 | 0 | 0 | 0 | 90.9% |
| test/language/reserved-words | 27 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/rest-parameters | 8 | 3 | 0 | 0 | 0 | 72.7% |
| test/language/source-text | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/language/statementList | 40 | 40 | 0 | 0 | 0 | 50.0% |
| test/language/statements | 3594 | 5244 | 0 | 27 | 472 | 40.5% |
| test/language/types | 80 | 24 | 0 | 0 | 9 | 76.9% |
| test/language/white-space | 51 | 16 | 0 | 0 | 0 | 76.1% |

## Top causas de FAIL (mensaje normalizado)

- **4039x** `Uncaught [object]`
  - ej: `test/language/arguments-object/S10.6_A3_T1.js`
- **3573x** `SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/cls-expr-private-gen-meth-args-trailing-comma-multiple.js`
- **2854x** `async incomplete: SyntaxError: UnexpectedToken`
  - ej: `test/language/arguments-object/cls-decl-async-private-gen-meth-args-trailing-comma-multiple.js`
- **2806x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/arguments-object/10.6-14-c-4-s.js`
- **1572x** `async incomplete: Uncaught TypeError: async generators are not supported yet`
  - ej: `test/language/arguments-object/async-gen-meth-args-trailing-comma-multiple.js`
- **1547x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - ej: `test/language/comments/S7.4_A1_T1.js`
- **841x** `Uncaught TypeError: Object.getOwnPropertyDescriptor called on non-object`
  - ej: `test/language/arguments-object/arguments-caller.js`
- **658x** `Uncaught TypeError: Object.defineProperty called on non-object`
  - ej: `test/language/eval-code/indirect/var-env-func-init-global-update-configurable.js`
- **353x** `Uncaught ReferenceError: eval is not defined`
  - ej: `test/language/comments/mongolian-vowel-separator-single-eval.js`
- **257x** `async incomplete: `
  - ej: `test/language/expressions/async-arrow-function/dflt-params-abrupt.js`
- **196x** `SyntaxError: MissingSemicolon`
  - ej: `test/language/asi/do-while-same-line.js`
- **147x** `async incomplete: Uncaught ReferenceError: globalThis is not defined`
  - ej: `test/language/expressions/async-function/named-strict-error-reassign-fn-name-in-body-in-arrow.js`
- **145x** `Uncaught TypeError: hasOwnProperty is not a function`
  - ej: `test/language/expressions/array/11.1.4_4-5-1.js`
- **135x** `Uncaught TypeError: getPrototypeOf is not a function`
  - ej: `test/language/arguments-object/10.6-5-1.js`
- **121x** `Uncaught ReferenceError: Proxy is not defined`
  - ej: `test/language/expressions/object/object-spread-proxy-get-not-called-on-dontenum-keys.js`
- **102x** `Uncaught ReferenceError: UintNArray is not defined`
  - ej: `test/language/destructuring/binding/typedarray-backed-by-resizable-buffer.js`
- **87x** `Uncaught ReferenceError: $N is not defined`
  - ej: `test/language/eval-code/indirect/realm.js`
- **81x** `Uncaught TypeError: Property description must be an object`
  - ej: `test/built-ins/Object/create/15.2.3.5-4-10.js`
- **78x** `async incomplete: Uncaught ReferenceError: print is not defined`
  - ej: `test/built-ins/Promise/all/iter-arg-is-false-reject.js`
- **76x** `Uncaught TypeError: Object.defineProperties called on non-object`
  - ej: `test/language/expressions/typeof/get-value.js`
- **76x** `Uncaught TypeError: split is not a function`
  - ej: `test/built-ins/String/prototype/split/argument-is-new-reg-exp-and-instance-is-string-hello.js`
- **71x** `Uncaught TypeError: expression is not a function`
  - ej: `test/language/statements/for-of/Array.prototype.Symbol.iterator.js`
- **62x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - ej: `test/language/expressions/async-arrow-function/dflt-params-ref-self.js`
- **53x** `Uncaught TypeError: hasOwn is not a function`
  - ej: `test/built-ins/Object/hasOwn/hasown_inherited_exists.js`
- **51x** `async incomplete: SyntaxError: MissingSemicolon`
  - ej: `test/language/import/import-attributes/json-idempotency.js`
- **50x** `Uncaught TypeError: Cannot set properties of undefined (setting '…')`
  - ej: `test/language/expressions/postfix-decrement/S11.3.2_A2.1_T1.js`
- **47x** `Uncaught TypeError: Cannot redefine property: foo`
  - ej: `test/built-ins/Object/defineProperties/15.2.3.7-6-a-42.js`
- **33x** `async incomplete: Uncaught TypeError: any is not a function`
  - ej: `test/built-ins/Promise/any/invoke-resolve-error-close.js`
- **31x** `Uncaught TypeError: Cannot assign to read only property '…' of object`
  - ej: `test/built-ins/Object/create/15.2.3.5-4-181.js`
- **29x** `async incomplete: Uncaught TypeError: allSettled is not a function`
  - ej: `test/built-ins/Promise/allSettled/does-not-invoke-array-setters.js`

## Top features presentes en FAILs

- 4027x async-iteration
- 3733x class
- 3422x destructuring-binding
- 2390x generators
- 1757x class-fields-public
- 1361x Symbol.iterator
- 1356x class-methods-private
- 1342x class-static-methods-private
- 1119x default-parameters
- 743x class-fields-private
- 604x dynamic-import
- 534x Symbol.asyncIterator
- 400x Symbol
- 399x computed-property-names
- 351x async-functions
- 339x object-rest
- 325x class-static-fields-private
- 275x arrow-function
- 258x top-level-await
- 247x Reflect.construct
- 208x BigInt
- 185x class-static-fields-public
- 154x import-defer
- 151x set-methods
- 145x Symbol.toPrimitive

## CRASHES (los más graves)

- **0** crashes conocidos (2026-07-19). Los 3 crashes de la fase regex ya
  están arreglados — ver "Delta 2026-07-19 (post-fixes)" abajo. El "CRASH: 1"
  del encabezado es del último barrido completo previo a los fixes.

---

## Análisis (actualizado 2026-07-19, post regex)

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
