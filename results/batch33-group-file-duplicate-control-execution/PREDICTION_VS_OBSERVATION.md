# Prediction vs Observation

| Prediction | Observation | Finding |
| --- | --- | --- |
| m32-har-subject-overlap | passed | Source HAR subject overlap was zero while random split mixed subjects; source-vs-random linear macro-F1 delta remained material. |
| m32-har-duplicate-transfer | weak | Exact feature-vector duplicate transfer did not explain the HAR delta; group/protocol structure was more plausible. |
| m32-shuttle-rare-class-metric | passed | Shuttle showed large accuracy/weighted-vs-macro differences and rare-class weakness, supporting class/metric explanation. |
| m32-shuttle-duplicate-transfer | weak | Duplicate checks did not provide enough direct evidence to explain Shuttle split delta. |
| m32-landsat-protocol-difficulty | partial | Landsat retained a modest random-minus-source delta without direct group/duplicate evidence; ordinary protocol difficulty remains plausible. |
| m32-letter-low-risk-control | passed | Letter behaved as a low-risk protocol-absent control with small seed-level variation. |
| m32-vehicle-ambiguity-barrier | inconclusive | Vehicle variants were executable, but file/fold semantics remain ambiguous and block strong protocol-first claims. |
| m32-optical-model-family | partial | Optical source-vs-random delta persisted but varied by model family, narrowing the mechanism to model-sensitive protocol effect. |
| m32-digits-control | passed | Bundled digits control remained low-risk under repeated random splits. |
| m32-image-ambiguous-protocol | not_executed | Deferred because Batch 33 already met execution requirements and Vehicle supplied the ambiguous deep-study target. |
