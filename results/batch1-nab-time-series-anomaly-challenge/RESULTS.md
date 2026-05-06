# Results

| Metric | Value |
| --- | --- |
| rows evaluated | 4032 |
| label windows | 1 |
| labeled points | 403 |
| global z-score precision | 1 |
| global z-score recall | 0.179 |
| rolling MAD precision | 0.105 |
| rolling MAD recall | 0.154 |
| derivative challenger precision | 0.324 |
| candidate rejected | 1 |

## Baseline Matrix

| Baseline | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| global_zscore_3sigma | 72 detections | precision=1 | recall=0.179, fp=0 |
| rolling_mad_4sigma_candidate | 593 detections | precision=0.105 | recall=0.154, fp=531 |
| derivative_zscore_challenger | 37 detections | precision=0.324 | recall=0.03, fp=25 |
