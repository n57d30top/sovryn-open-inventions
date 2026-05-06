# Baseline Reproduction

| Baseline | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| light_threshold_train_selected | threshold=364.5 | f1=0.984, balAcc=0.994 | fp=55, fn=12 |
| co2_threshold_train_selected | threshold=614 | f1=0.448, balAcc=0.665 | fp=3612, fn=413 |
| temperature_threshold_train_selected | threshold=21.26 | f1=0.736, balAcc=0.881 | fp=1153, fn=183 |
| humidity_threshold_train_selected | threshold=19.525 | f1=0.347, balAcc=0.5 | fp=7703, fn=0 |

Baseline reproduction is bounded to public-safe source or dataset evidence. Missing full-scale reproduction is recorded as a limitation, not hidden.
