# Test262 — z-* engine divergence report

Total: 53414 tests | ran: 50882 | **PASS: 29398 (57.8% of those ran)** | FAIL: 21459 | CRASH: 1 | TIMEOUT: 24 | SKIP (by design): 2532


## Pass rate by area

| area | pass | fail | crash | timeout | skip | % pass |
|---|---|---|---|---|---|---|
| test/annexB/built-ins | 44 | 195 | 0 | 2 | 0 | 18.3% |
| test/annexB/language | 24 | 31 | 0 | 0 | 790 | 43.6% |
| test/built-ins/AbstractModuleSource | 0 | 8 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AggregateError | 0 | 25 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Array | 1778 | 1264 | 0 | 3 | 36 | 58.4% |
| test/built-ins/ArrayBuffer | 30 | 191 | 0 | 0 | 0 | 13.6% |
| test/built-ins/ArrayIteratorPrototype | 10 | 9 | 0 | 0 | 8 | 52.6% |
| test/built-ins/AsyncDisposableStack | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/AsyncFromSyncIteratorPrototype | 6 | 32 | 0 | 0 | 0 | 15.8% |
| test/built-ins/AsyncFunction | 9 | 9 | 0 | 0 | 0 | 50.0% |
| test/built-ins/AsyncGeneratorFunction | 8 | 15 | 0 | 0 | 0 | 34.8% |
| test/built-ins/AsyncGeneratorPrototype | 2 | 45 | 0 | 1 | 0 | 4.2% |
| test/built-ins/AsyncIteratorPrototype | 0 | 13 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Atomics | 0 | 387 | 0 | 0 | 2 | 0.0% |
| test/built-ins/BigInt | 63 | 14 | 0 | 0 | 0 | 81.8% |
| test/built-ins/Boolean | 46 | 5 | 0 | 0 | 0 | 90.2% |
| test/built-ins/DataView | 343 | 218 | 0 | 0 | 0 | 61.1% |
| test/built-ins/Date | 521 | 73 | 0 | 0 | 0 | 87.7% |
| test/built-ins/DisposableStack | 0 | 93 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Error | 28 | 65 | 0 | 0 | 0 | 30.1% |
| test/built-ins/FinalizationRegistry | 0 | 47 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Function | 202 | 219 | 0 | 0 | 88 | 48.0% |
| test/built-ins/GeneratorFunction | 8 | 15 | 0 | 0 | 0 | 34.8% |
| test/built-ins/GeneratorPrototype | 15 | 45 | 0 | 1 | 0 | 24.6% |
| test/built-ins/Infinity | 3 | 1 | 0 | 0 | 2 | 75.0% |
| test/built-ins/Iterator | 7 | 507 | 0 | 0 | 0 | 1.4% |
| test/built-ins/JSON | 82 | 83 | 0 | 0 | 0 | 49.7% |
| test/built-ins/Map | 129 | 74 | 0 | 0 | 1 | 63.5% |
| test/built-ins/MapIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/Math | 326 | 1 | 0 | 0 | 0 | 99.7% |
| test/built-ins/NaN | 3 | 1 | 0 | 0 | 2 | 75.0% |
| test/built-ins/NativeErrors | 44 | 50 | 0 | 0 | 0 | 46.8% |
| test/built-ins/Number | 262 | 78 | 0 | 0 | 0 | 77.1% |
| test/built-ins/Object | 2273 | 1127 | 0 | 0 | 11 | 66.9% |
| test/built-ins/Promise | 201 | 525 | 0 | 0 | 3 | 27.7% |
| test/built-ins/Proxy | 82 | 218 | 0 | 0 | 11 | 27.3% |
| test/built-ins/Reflect | 109 | 44 | 0 | 0 | 0 | 71.2% |
| test/built-ins/RegExp | 1219 | 652 | 0 | 7 | 1 | 64.9% |
| test/built-ins/RegExpStringIteratorPrototype | 0 | 17 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Set | 205 | 177 | 0 | 0 | 1 | 53.7% |
| test/built-ins/SetIteratorPrototype | 1 | 10 | 0 | 0 | 0 | 9.1% |
| test/built-ins/ShadowRealm | 0 | 64 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SharedArrayBuffer | 0 | 104 | 0 | 0 | 0 | 0.0% |
| test/built-ins/String | 956 | 264 | 0 | 0 | 3 | 78.4% |
| test/built-ins/StringIteratorPrototype | 0 | 7 | 0 | 0 | 0 | 0.0% |
| test/built-ins/SuppressedError | 0 | 22 | 0 | 0 | 0 | 0.0% |
| test/built-ins/Symbol | 63 | 33 | 0 | 0 | 2 | 65.6% |
| test/built-ins/Temporal | 1570 | 3033 | 0 | 0 | 0 | 34.1% |
| test/built-ins/ThrowTypeError | 0 | 14 | 0 | 0 | 0 | 0.0% |
| test/built-ins/TypedArray | 469 | 969 | 0 | 0 | 8 | 32.6% |
| test/built-ins/TypedArrayConstructors | 296 | 426 | 0 | 0 | 16 | 41.0% |
| test/built-ins/Uint8Array | 6 | 64 | 0 | 0 | 0 | 8.6% |
| test/built-ins/WeakMap | 0 | 141 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakRef | 0 | 29 | 0 | 0 | 0 | 0.0% |
| test/built-ins/WeakSet | 0 | 85 | 0 | 0 | 0 | 0.0% |
| test/built-ins/decodeURI | 54 | 0 | 0 | 1 | 0 | 98.2% |
| test/built-ins/decodeURIComponent | 55 | 0 | 0 | 1 | 0 | 98.2% |
| test/built-ins/encodeURI | 25 | 5 | 0 | 1 | 0 | 80.6% |
| test/built-ins/encodeURIComponent | 25 | 5 | 0 | 1 | 0 | 80.6% |
| test/built-ins/eval | 10 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/global | 27 | 2 | 0 | 0 | 0 | 93.1% |
| test/built-ins/isFinite | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/isNaN | 15 | 0 | 0 | 0 | 0 | 100.0% |
| test/built-ins/parseFloat | 50 | 4 | 0 | 0 | 0 | 92.6% |
| test/built-ins/parseInt | 49 | 6 | 0 | 0 | 0 | 89.1% |
| test/built-ins/undefined | 3 | 2 | 0 | 0 | 3 | 60.0% |
| test/harness/assert-false.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-notsamevalue-nan.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-notsamevalue-notsame.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-notsamevalue-objects.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-notsamevalue-tostring.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-notsamevalue-zeros.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-obj.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-samevalue-nan.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-samevalue-objects.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-samevalue-same.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-samevalue-tostring.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-samevalue-zeros.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-throws-custom-typeerror.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-throws-custom.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-throws-incorrect-ctor.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-throws-native.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-throws-no-arg.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-throws-no-error.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-throws-null-fn.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-throws-null.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-throws-primitive.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-throws-same-realm.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/assert-throws-single-arg.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-tostring.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assert-true.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/assertRelativeDateMs.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-asyncTest-func-throws-sync.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-asyncTest-rejects-non-callable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-asyncTest-return-not-thenable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-asyncTest-returns-undefined.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/asyncHelpers-asyncTest-then-rejects.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-asyncTest-then-resolves.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-asyncTest-without-async-flag.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-custom-typeerror.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-custom.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-func-never-settles.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-func-throws-sync.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-incorrect-ctor.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-invalid-func.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-native.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-no-arg.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-no-error.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-null.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-primitive.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-resolved-error.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/asyncHelpers-throwsAsync-same-realm.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/asyncHelpers-throwsAsync-single-arg.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/byteConversionValues.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-arguments.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-arraylike.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-different-elements.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-different-length.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-empty.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-falsy-arguments.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-message.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-same-elements-different-order.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-same-elements-same-order.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-samevalue.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-sparse.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/compare-array-symbol.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/dateConstants.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/decimalToHexString.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/deepEqual-array.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/deepEqual-circular.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/deepEqual-deep.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/deepEqual-mapset.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/deepEqual-object.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/deepEqual-primitives-bigint.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/deepEqual-primitives.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/detachArrayBuffer-host-detachArrayBuffer.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/detachArrayBuffer.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/fnGlobalObject.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/isConstructor.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/nans.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/nativeFunctionMatcher.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/promiseHelper.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifyconfigurable-configurable-object.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/propertyhelper-verifyconfigurable-configurable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifyconfigurable-not-configurable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifyenumerable-enumerable-symbol.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifyenumerable-enumerable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifyenumerable-not-enumerable-symbol.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifyenumerable-not-enumerable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifynotconfigurable-configurable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifynotconfigurable-not-configurable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifynotenumerable-enumerable-symbol.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifynotenumerable-enumerable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifynotenumerable-not-enumerable-symbol.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifynotenumerable-not-enumerable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifynotwritable-not-writable-strict.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifynotwritable-writable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifywritable-array-length.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/propertyhelper-verifywritable-not-writable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/propertyhelper-verifywritable-writable.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/proxytrapshelper-default.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/proxytrapshelper-overrides.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/sta.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/tcoHelper.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/testTypedArray-conversions-call-error.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/testTypedArray-conversions.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/testTypedArray.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/verifyProperty-arguments.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-configurable-object.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/harness/verifyProperty-desc-is-not-object.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-noproperty.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-restore-accessor-symbol.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-restore-accessor.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-restore-symbol.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-restore.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-same-value.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-string-prop.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-symbol-prop.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-undefined-desc.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-value-error.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/verifyProperty-value.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/harness/wellKnownIntrinsicObjects.js | 1 | 0 | 0 | 0 | 0 | 100.0% |
| test/intl402/Array | 0 | 2 | 0 | 0 | 0 | 0.0% |
| test/intl402/BigInt | 5 | 6 | 0 | 0 | 0 | 45.5% |
| test/intl402/Collator | 0 | 65 | 0 | 0 | 0 | 0.0% |
| test/intl402/Date | 8 | 4 | 0 | 0 | 0 | 66.7% |
| test/intl402/DateTimeFormat | 0 | 244 | 0 | 0 | 0 | 0.0% |
| test/intl402/DisplayNames | 0 | 57 | 0 | 0 | 0 | 0.0% |
| test/intl402/DurationFormat | 0 | 110 | 0 | 0 | 0 | 0.0% |
| test/intl402/FallbackSymbol | 0 | 2 | 0 | 0 | 0 | 0.0% |
| test/intl402/Intl | 0 | 66 | 0 | 0 | 0 | 0.0% |
| test/intl402/ListFormat | 0 | 81 | 0 | 0 | 0 | 0.0% |
| test/intl402/Locale | 0 | 160 | 0 | 0 | 0 | 0.0% |
| test/intl402/Number | 3 | 4 | 0 | 0 | 0 | 42.9% |
| test/intl402/NumberFormat | 0 | 249 | 0 | 0 | 0 | 0.0% |
| test/intl402/PluralRules | 0 | 53 | 0 | 0 | 0 | 0.0% |
| test/intl402/RelativeTimeFormat | 0 | 80 | 0 | 0 | 0 | 0.0% |
| test/intl402/Segmenter | 0 | 79 | 0 | 0 | 0 | 0.0% |
| test/intl402/String | 4 | 15 | 0 | 0 | 0 | 21.1% |
| test/intl402/Temporal | 66 | 1963 | 0 | 0 | 0 | 3.3% |
| test/intl402/TypedArray | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/constructors-string-and-single-element-array.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/constructors-taint-Object-prototype-2.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/constructors-taint-Object-prototype.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/default-locale-is-canonicalized.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/default-locale-is-supported.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/fallback-locales-are-supported.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/language-tags-canonicalized.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/language-tags-invalid.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/language-tags-valid.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/language-tags-with-underscore.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-consistent-with-resolvedOptions.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-default-locale-and-zxx-locale.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-duplicate-elements-removed.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-empty-and-undefined.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-locales-arg-coered-to-object.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-locales-arg-empty-array.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-returned-array-elements-are-not-frozen.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-taint-Array-2.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-taint-Array.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-test-option-localeMatcher.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-throws-if-element-not-string-or-object.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/intl402/supportedLocalesOf-unicode-extensions-ignored.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/language/arguments-object | 189 | 17 | 0 | 0 | 57 | 91.7% |
| test/language/asi | 101 | 1 | 0 | 0 | 0 | 99.0% |
| test/language/block-scope | 145 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/comments | 46 | 6 | 0 | 0 | 0 | 88.5% |
| test/language/computed-property-names | 46 | 2 | 0 | 0 | 0 | 95.8% |
| test/language/destructuring | 17 | 1 | 0 | 0 | 1 | 94.4% |
| test/language/directive-prologue | 5 | 0 | 0 | 0 | 57 | 100.0% |
| test/language/eval-code | 96 | 31 | 0 | 0 | 220 | 75.6% |
| test/language/export | 3 | 0 | 0 | 0 | 0 | 100.0% |
| test/language/expressions | 7894 | 2620 | 0 | 0 | 588 | 75.1% |
| test/language/function-code | 100 | 8 | 0 | 0 | 109 | 92.6% |
| test/language/future-reserved-words | 48 | 0 | 0 | 0 | 7 | 100.0% |
| test/language/global-code | 21 | 16 | 0 | 0 | 5 | 56.8% |
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
| test/language/statements | 6946 | 1919 | 0 | 0 | 472 | 78.4% |
| test/language/types | 101 | 3 | 0 | 0 | 9 | 97.1% |
| test/language/white-space | 67 | 0 | 0 | 0 | 0 | 100.0% |
| test/staging/Temporal | 1 | 1 | 0 | 0 | 0 | 50.0% |
| test/staging/Uint8Array | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/staging/built-ins | 2 | 6 | 0 | 0 | 0 | 25.0% |
| test/staging/decorators | 1 | 2 | 0 | 0 | 0 | 33.3% |
| test/staging/explicit-resource-management | 6 | 47 | 0 | 0 | 0 | 11.3% |
| test/staging/set-is-subset-of-empty-index.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/staging/set-is-subset-on-set-like.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/staging/set-is-subset-table-receiver-cleared.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/staging/set-is-subset-table-transition.js | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/staging/set-methods | 0 | 3 | 0 | 0 | 0 | 0.0% |
| test/staging/sm | 418 | 985 | 1 | 2 | 0 | 29.7% |
| test/staging/source-phase-imports | 0 | 1 | 0 | 0 | 0 | 0.0% |
| test/staging/top-level-await | 0 | 1 | 0 | 0 | 0 | 0.0% |

## Top FAIL causes (normalized message)

- **1647x** `Uncaught TypeError: Cannot read properties of undefined (reading '…')`
  - e.g.: `test/annexB/built-ins/RegExp/legacy-accessors/rightContext/this-not-regexp-constructor.js`
- **1195x** `Uncaught ReferenceError: Intl is not defined`
  - e.g.: `test/intl402/BigInt/prototype/toLocaleString/returns-same-results-as-NumberFormat.js`
- **743x** `Uncaught TypeError: month is required`
  - e.g.: `test/built-ins/Temporal/PlainDate/from/argument-object-valid.js`
- **740x** `Uncaught TypeError: expression is not a constructor`
  - e.g.: `test/built-ins/Temporal/Duration/compare/blank-duration.js`
- **721x** `Uncaught { message: Expected a TypeError to be thrown but no exception was thrown at all }`
  - e.g.: `test/built-ins/Array/prototype/filter/target-array-non-extensible.js`
- **651x** `z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - e.g.: `test/built-ins/Array/isArray/15.4.3.2-2-1.js`
- **600x** `SyntaxError: UnexpectedToken`
  - e.g.: `test/annexB/language/expressions/assignment/dstr/object-pattern-emulates-undefined.js`
- **561x** `async incomplete: SyntaxError: UnexpectedToken`
  - e.g.: `test/language/expressions/async-function/named-returns-async-arrow-returns-newtarget.js`
- **485x** `Uncaught { message: Expected a TestNError to be thrown but no exception was thrown at all }`
  - e.g.: `test/built-ins/Array/prototype/filter/create-ctor-poisoned.js`
- **469x** `Uncaught { message: Expected SameValue(«N», «N») to be true }`
  - e.g.: `test/built-ins/Array/prototype/lastIndexOf/coerced-position-grow.js`
- **449x** `Uncaught ReferenceError: Iterator is not defined`
  - e.g.: `test/built-ins/Iterator/length.js`
- **426x** `Uncaught ReferenceError: $N is not defined`
  - e.g.: `test/annexB/built-ins/Array/from/iterator-method-emulates-undefined.js`
- **308x** `Uncaught TypeError: Cannot convert undefined or null to object`
  - e.g.: `test/annexB/built-ins/RegExp/prototype/compile/length.js`
- **287x** `async incomplete: z-run: NotImplemented: the script uses a feature this engine doesn't support yet`
  - e.g.: `test/built-ins/Array/fromAsync/async-iterable-async-mapped-awaits-once.js`
- **260x** `Uncaught ReferenceError: SharedArrayBuffer is not defined`
  - e.g.: `test/built-ins/ArrayBuffer/prototype/resize/this-is-sharedarraybuffer.js`
- **228x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: TypeError Expected SameValue(«[object Functio`
  - e.g.: `test/language/expressions/async-generator/named-yield-star-getiter-async-not-callable-boolean-throw.js`
- **200x** `Uncaught { message: Expected a TypeError but got a ReferenceError }`
  - e.g.: `test/annexB/built-ins/unescape/to-primitive-err.js`
- **200x** `SyntaxError: MissingSemicolon`
  - e.g.: `test/language/asi/do-while-same-line.js`
- **183x** `Uncaught { message: Expected SameValue(«[object Function]», «N») to be true }`
  - e.g.: `test/language/expressions/class/elements/after-same-line-gen-rs-private-getter-alt.js`
- **182x** `async incomplete: TestN:AsyncTestFailure:TestNError: TestNError: Expected SameValue(«N», «N») to be true`
  - e.g.: `test/built-ins/Array/fromAsync/sync-iterable-with-rejecting-thenable-closes.js`
- **176x** `Uncaught { message: Expected a ReferenceError to be thrown but no exception was thrown at all }`
  - e.g.: `test/built-ins/Function/internals/Construct/derived-this-uninitialized.js`
- **167x** `SyntaxError: OutOfMemory`
  - e.g.: `test/built-ins/Array/property-cast-number.js`
- **147x** `Uncaught { message: Expected a TestNError but got a TypeError }`
  - e.g.: `test/annexB/built-ins/RegExp/prototype/compile/flags-to-string-err.js`
- **143x** `Uncaught { message: Expected SameValue(«undefined», «N») to be true }`
  - e.g.: `test/built-ins/Array/prototype/exotic-array.js`
- **138x** `Uncaught { message: Expected SameValue(«"undefined"», «"function"») to be true }`
  - e.g.: `test/annexB/built-ins/unescape/prop-desc.js`
- **134x** `Uncaught TypeError: Object.defineProperty called on non-object`
  - e.g.: `test/annexB/built-ins/RegExp/prototype/Symbol.split/Symbol.match-getter-recompiles-source.js`
- **132x** `Uncaught RangeError: Maximum call stack size exceeded`
  - e.g.: `test/language/expressions/tco-pos.js`
- **129x** `Uncaught TypeError: year is required`
  - e.g.: `test/built-ins/Temporal/PlainMonthDay/prototype/toPlainDate/order-of-operations.js`
- **121x** `Uncaught TypeError: Property description must be an object`
  - e.g.: `test/built-ins/Object/create/15.2.3.5-4-10.js`
- **118x** `Uncaught TypeError: resize is not a function`
  - e.g.: `test/built-ins/Array/prototype/at/coerced-index-resize.js`

## Top features present in FAILs

- 5076x Temporal
- 1702x TypedArray
- 1513x Intl.Era-monthcode
- 1503x async-iteration
- 1230x generators
- 1179x Symbol.iterator
- 1093x class
- 1073x destructuring-binding
- 786x Symbol
- 786x BigInt
- 687x class-fields-public
- 604x dynamic-import
- 501x Symbol.asyncIterator
- 463x SharedArrayBuffer
- 456x resizable-arraybuffer
- 449x class-methods-private
- 437x arrow-function
- 437x default-parameters
- 397x explicit-resource-management
- 397x class-fields-private
- 386x iterator-helpers
- 384x Atomics
- 364x Proxy
- 348x Reflect
- 347x class-static-methods-private

## CRASHES (the most severe)

- **1x** `exit -N: `
  - e.g.: `test/staging/sm/JSON/parse-syntax-errors-02.js`
