# Baseline Reproduction

| Baseline | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| global_zscore_3sigma | 72 detections | precision=1 | recall=0.179, fp=0 |
| rolling_mad_4sigma_candidate | 593 detections | precision=0.105 | recall=0.154, fp=531 |
| derivative_zscore_challenger | 37 detections | precision=0.324 | recall=0.03, fp=25 |

Baseline reproduction is bounded to public-safe data or source-card evidence. Missing full-scale reproduction is recorded as a limitation, not hidden.
