# Ablation Report

Result label: partially_supported

This report removes one candidate feature at a time. It is a bounded synthetic-data ablation, not proof that the method will generalize.

| Variant | Removed feature | FPR | Recall |
| --- | --- | ---: | ---: |
| without-provenance-score | provenance score | 0.2 | 1 |
| without-equivalence-confidence | limited identifier-equivalence confidence | 0.2 | 1 |
| without-outlier-residual-threshold | outlier residual threshold | 0 | 0.5 |

Provenance scoring and residual thresholds are the clearest contributors in this bounded toy chemistry study.
