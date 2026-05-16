# Holdout Policy Results

Source: `standalone_replay_results.json`

## Current Holdout Results

| Claim                     | Task | Holdout policy       | Split feature       | Holdout metric | Random-holdout delta | V2 holdout interpretation                              |
| ------------------------- | ---: | -------------------- | ------------------- | -------------: | -------------------: | ------------------------------------------------------ |
| SA-PLAUS-003-OPENML-32    |   32 | first-feature bucket | input1              |          0.000 |                0.187 | supports proxy holdout caveat                          |
| SECOND-SURV-001-OPENML-59 |   59 | first-feature bucket | sepallength         |          0.000 |                0.511 | supports proxy holdout caveat                          |
| SECOND-SURV-003-OPENML-7  |    7 | first-feature bucket | age_gt_60           |          0.000 |                0.500 | supports proxy holdout caveat                          |
| SECOND-SURV-005-OPENML-53 |   53 | first-feature bucket | COMPACTNESS         |          0.176 |                0.221 | supports proxy holdout caveat                          |
| SECOND-SURV-006-OPENML-36 |   36 | first-feature bucket | region-centroid-col |          0.000 |                0.209 | supports proxy holdout caveat                          |
| SECOND-SURV-007-OPENML-43 |   43 | first-feature bucket | word_freq_make      |          0.000 |                0.653 | holdout supports, negative control blocks stronger use |
| SECOND-SURV-008-OPENML-15 |   15 | first-feature bucket | Clump_Thickness     |          0.000 |                0.790 | supports proxy holdout caveat                          |

## What Is Justified

The current evidence justifies saying:

> Under the package's deterministic first-feature bucket holdout, random-split
> metrics are higher than holdout metrics for all seven rows.

## What Is Not Justified

The current evidence does not justify saying:

- real group leakage has been closed,
- real entity leakage has been closed,
- temporal leakage has been closed,
- GroupKFold or StratifiedKFold validation has passed,
- the method is externally accepted.

Holdout status: `policy_documented_proxy_only_not_full_closure`.
