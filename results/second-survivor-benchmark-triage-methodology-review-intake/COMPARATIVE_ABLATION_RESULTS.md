# Comparative Ablation Results

Source:

- `standalone_replay_results.json`
- `BENCHMARK_TRIAGE_FORMAL_RULES.json`

## Result Summary

| Method              | Selected | Robust selected | Weak selected | Current interpretation                                           |
| ------------------- | -------: | --------------: | ------------: | ---------------------------------------------------------------- |
| Reject-all          |        0 |               0 |             0 | Avoids false positives but has zero review yield                 |
| Accept-all          |        7 |               6 |             1 | Fails to demote weak negative-control case                       |
| Task-size largest 4 |        4 |               3 |             1 | Size does not explain selection cleanly                          |
| Holdout-only        |        6 |               5 |             1 | Holdout delta alone keeps a weak negative-control case           |
| Baseline-only       |        6 |               6 |             0 | Ties V2 on current rows                                          |
| V2 formal rule      |        6 |               6 |             0 | Improves over accept-all and holdout-only, but not baseline-only |

## Per-Claim V2 Outcome

| Claim                     | Task | Dataset   | Model-baseline delta | Random-holdout delta | Negative-control margin | V2 score | V2 output                     |
| ------------------------- | ---: | --------- | -------------------: | -------------------: | ----------------------: | -------: | ----------------------------- |
| SA-PLAUS-003-OPENML-32    |   32 | pendigits |                0.093 |                0.187 |                   0.081 |    0.871 | retain_for_external_re_review |
| SECOND-SURV-001-OPENML-59 |   59 | iris      |                0.289 |                0.511 |                   0.289 |    0.960 | retain_for_external_re_review |
| SECOND-SURV-003-OPENML-7  |    7 | audiology |                0.250 |                0.500 |                   0.441 |    0.960 | retain_for_external_re_review |
| SECOND-SURV-005-OPENML-53 |   53 | vehicle   |                0.165 |                0.221 |                   0.170 |    0.960 | retain_for_external_re_review |
| SECOND-SURV-006-OPENML-36 |   36 | segment   |                0.082 |                0.209 |                   0.056 |    0.869 | retain_for_external_re_review |
| SECOND-SURV-007-OPENML-43 |   43 | spambase  |                0.043 |                0.653 |                   0.001 |    0.667 | major_revision_caveat_retain  |
| SECOND-SURV-008-OPENML-15 |   15 | breast-w  |                0.119 |                0.790 |                   0.190 |    0.919 | retain_for_external_re_review |

## Decision

Ablation status: `partial_not_closed`.

V2 is a real decision rule and it catches one weak replayable row that accept-all
and holdout-only keep. However, on this seven-row package, baseline-only ties V2.
That means the major-revision concern is not fully closed.

The next re-review must use a larger mixed benchmark with weak, plausible, and
known-good claims so V2 can be judged against baseline-only and reject-all on
survivor yield.
