# Sensitivity Analysis

Result label: partially_supported

This deterministic sweep checks whether the result depends heavily on selected alpha parameters.

| Parameter | Value | FPR | Recall |
| --- | ---: | ---: | ---: |
| threshold | 7 | 0 | 1 |
| threshold | 8 | 0 | 1 |
| threshold | 10 | 0 | 1 |
| threshold | 12 | 0 | 1 |
| provenanceWeight | 0 | 0 | 1 |
| provenanceWeight | 0.5 | 0 | 1 |
| provenanceWeight | 1 | 0 | 1 |
| weatherWeight | 0 | 0.125 | 1 |
| weatherWeight | 0.5 | 0 | 1 |
| weatherWeight | 1 | 0 | 1 |

The candidate remains strongest when weather normalization is enabled; threshold sweeps expose the expected false-positive tradeoff.
