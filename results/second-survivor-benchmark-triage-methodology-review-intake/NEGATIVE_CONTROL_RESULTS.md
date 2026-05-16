# Negative Control Results

Source: `standalone_replay_results.json`

## Shuffled-Target Control With V2 Margin

| Claim                     | Task | Dataset   | Random metric | Negative metric | Margin | V1 behaved | V2 result   |
| ------------------------- | ---: | --------- | ------------: | --------------: | -----: | ---------- | ----------- |
| SA-PLAUS-003-OPENML-32    |   32 | pendigits |         0.187 |           0.106 |  0.081 | yes        | pass        |
| SECOND-SURV-001-OPENML-59 |   59 | iris      |         0.511 |           0.222 |  0.289 | yes        | pass        |
| SECOND-SURV-003-OPENML-7  |    7 | audiology |         0.500 |           0.059 |  0.441 | yes        | pass        |
| SECOND-SURV-005-OPENML-53 |   53 | vehicle   |         0.398 |           0.228 |  0.170 | yes        | pass        |
| SECOND-SURV-006-OPENML-36 |   36 | segment   |         0.209 |           0.153 |  0.056 | yes        | pass        |
| SECOND-SURV-007-OPENML-43 |   43 | spambase  |         0.653 |           0.652 |  0.001 | yes        | fail_margin |
| SECOND-SURV-008-OPENML-15 |   15 | breast-w  |         0.790 |           0.600 |  0.190 | yes        | pass        |

## Decision

Negative controls strengthened: yes, for the executed shuffled-target control.

Full negative-control closure: no. Random-feature, source-identity,
duplicate/entity-overlap, metric-sensitivity, and threshold-sensitivity controls
must still be executed on a larger re-review benchmark.
