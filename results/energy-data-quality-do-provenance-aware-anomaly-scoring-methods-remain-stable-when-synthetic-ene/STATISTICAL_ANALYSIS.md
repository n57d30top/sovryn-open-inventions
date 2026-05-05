# Statistical Analysis

Result label: partially_supported

This is a bounded alpha statistical analysis over deterministic synthetic data. It is not a causal claim, production-readiness claim, or legal conclusion.

## Confusion Metrics

| Method | TP | FP | TN | FN | Precision | Recall | FPR | FNR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline | 3 | 3 | 21 | 0 | 0.5 | 1 | 0.125 | 0 |
| Candidate | 3 | 0 | 24 | 0 | 1 | 1 | 0 | 0 |

Mean false-positive reduction: 0.125
Mean recall delta: 0
Effect size: 1250
Confidence interval (deterministic seeded interval over the three completed alpha experiment runs): 0.125 to 0.125

## Evidence Summary

The candidate detector reduced false positives on seeded synthetic energy datasets while preserving recall in this bounded alpha runtime.

## Limitations

- This is a synthetic-data result, not a real-world energy claim.
- Alpha.3 analysis does not yet include independent replication or falsification.
- The result label is evidence-bound and must not be read as a causal or production-readiness conclusion.
