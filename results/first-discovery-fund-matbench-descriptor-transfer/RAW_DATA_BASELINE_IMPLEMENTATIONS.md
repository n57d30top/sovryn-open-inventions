# Raw-Data Baseline Implementations

The executable implementations are in `reproduce_matbench_candidate.py`. This document summarizes the exact public-data baselines used by the standalone raw-data proxy experiment.

| Baseline | Implementation |
| --- | --- |
| `null_or_trivial_rule` | Predict the train-target mean for every deterministic holdout row. |
| `composition_formula_size` | Fit OLS with intercept on train-standardized `element_count` and `total_atoms`; score on deterministic holdout. |
| `matched_negative_shuffled_target` | Fit the same all-feature OLS after deterministic train-target shuffle with seed `1729`; score on deterministic holdout. |
| `candidate_formula_descriptor_proxy` | Fit OLS with intercept on all seven formula descriptors; score on deterministic holdout. |

All baselines are intentionally simple and dependency-free so an external reviewer can rerun them with only Python standard library.
