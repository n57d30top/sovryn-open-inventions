# Baseline Comparison

Baseline: unit-normalization-only conflict detector
Candidate: unit-normalization plus provenance scoring detector
Result label: partially_supported

This comparison is evidence-bound to the generated synthetic experiment runs.

| Seed | Baseline FPR | Candidate FPR | Reduction |
| --- | ---: | ---: | ---: |
| 1 | 0.1667 | 0 | 0.1667 |
| 2 | 0.1667 | 0 | 0.1667 |
| 3 | 0.1667 | 0 | 0.1667 |

- Candidate better on false positives: true
- Recall preserved: true
