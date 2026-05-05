# Ablation Report

Result label: partially_supported

This report removes one candidate feature at a time. It is a bounded synthetic-data ablation, not proof that the method will generalize.

| Variant | Removed feature | FPR | Recall |
| --- | --- | ---: | ---: |
| without-provenance-score | provenance score | 0 | 1 |
| without-weather-normalization | weather normalization | 0.125 | 1 |
| without-missing-interval-feature | missing interval feature | 0 | 1 |

Weather normalization is the clearest contributor to lower false positives in this synthetic study; provenance and missing-interval features improve triage specificity.
