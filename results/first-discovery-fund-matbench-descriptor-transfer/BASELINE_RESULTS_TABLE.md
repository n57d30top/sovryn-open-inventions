# Baseline Results Table

The table below exposes the Product-recorded baseline comparator values for the public runtime evidence. It does not add new computation.

| Baseline/control | Recorded value | Explains signal | Evidence ref | Reviewer note |
| --- | ---: | --- | --- | --- |
| composition_formula_size_target_family_baseline | 0.34 | false | `copied-product-evidence/runtime-evidence-output-01.json` | Strongest named simple baseline; reviewer should independently define and rerun it. |
| matched_negative_control | 0.29 | false | `copied-product-evidence/runtime-evidence-output-01.json` | Product-recorded negative/control comparator. |
| null_or_trivial_rule | 0.23 | false | `copied-product-evidence/runtime-evidence-output-01.json` | Product-recorded null/simple-rule comparator. |
| second-stage residual floor | 0.1 | not applicable | `copied-product-evidence/runtime-evidence-output-01.json#birthEvaluation` | Birth gate says the residual magnitude must exceed this floor. |

Reviewer caveat: these are Product-recorded scalar results. The public package still needs a standalone script that recomputes these baselines from raw Matbench data.

