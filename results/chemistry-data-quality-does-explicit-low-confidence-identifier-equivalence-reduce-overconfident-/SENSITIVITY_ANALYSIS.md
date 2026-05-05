# Sensitivity Analysis

Result label: partially_supported

This deterministic sweep checks whether the result depends heavily on selected alpha parameters.

| Parameter | Value | FPR | Recall |
| --- | ---: | ---: | ---: |
| residualThresholdC | 5 | 0.2 | 1 |
| residualThresholdC | 20 | 0 | 1 |
| residualThresholdC | 100 | 0 | 0.5 |
| provenanceWeight | 0 | 0.2 | 1 |
| provenanceWeight | 0.5 | 0 | 1 |
| equivalenceConfidencePenalty | 1 | 0 | 1 |

The candidate is stable under moderate residual and provenance weights, but high thresholds can miss a conflict.
