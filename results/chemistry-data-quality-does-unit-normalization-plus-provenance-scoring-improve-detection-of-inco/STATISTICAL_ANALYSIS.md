# Statistical Analysis

Result label: partially_supported

This is a bounded alpha statistical analysis over deterministic synthetic data. It is not a causal claim, production-readiness claim, or legal conclusion.

## Confusion Metrics

| Method | TP | FP | TN | FN | Precision | Recall | FPR | FNR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline | 3 | 3 | 15 | 0 | 0.5 | 1 | 0.1667 | 0 |
| Candidate | 3 | 0 | 18 | 0 | 1 | 1 | 0 | 0 |

Mean false-positive reduction: 0.1667
Mean recall delta: 0
Effect size: 1667
Confidence interval (deterministic seeded interval over the three completed alpha experiment runs): 0.1667 to 0.1667

## Evidence Summary

The unit-plus-provenance detector reduced false positives compared with the unit-normalization-only baseline on deterministic toy molecular-property records.

## Limitations

- This is a synthetic chemistry-style data-quality result, not a general cheminformatics claim.
- Identifier equivalence uses a limited toy map and must not be read as RDKit/OpenBabel canonicalization.
- No synthesis, drug-design, lab, or hazardous-material guidance is provided.
