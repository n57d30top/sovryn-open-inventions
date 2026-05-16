# Candidate One-Page Summary

Candidate ID: `DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001`

Status: `pipeline_fund_candidate`, not discovery-scored.

## Bounded Claim

A receipt-first benchmark triage method can identify OpenML benchmark claims whose random-split performance survives public raw replay as a bounded protocol-fragility signal across OpenML-32 and at least one independent task, with nonfatal baseline, holdout, rival, and negative-control checks.

## Why Receipt-First Matters

Earlier benchmark/data candidates failed when evidence used source-family URLs instead of concrete task receipts, raw-data access, split definitions, or replayable manifests. This candidate only uses concrete OpenML task/data receipts and public raw replay rows.

## Seven Survivor Tasks

| Claim                       | Task | Dataset   | Split feature       |
| --------------------------- | ---: | --------- | ------------------- |
| `SA-PLAUS-003-OPENML-32`    |   32 | pendigits | input1              |
| `SECOND-SURV-001-OPENML-59` |   59 | iris      | sepallength         |
| `SECOND-SURV-003-OPENML-7`  |    7 | audiology | age_gt_60           |
| `SECOND-SURV-005-OPENML-53` |   53 | vehicle   | COMPACTNESS         |
| `SECOND-SURV-006-OPENML-36` |   36 | segment   | region-centroid-col |
| `SECOND-SURV-007-OPENML-43` |   43 | spambase  | word_freq_make      |
| `SECOND-SURV-008-OPENML-15` |   15 | breast-w  | Clump_Thickness     |

## Reproducer Status

The public reproducer fetches OpenML ARFF files, recomputes replay metrics, and emits machine-readable JSON.

Current dry-run status:

`public_raw_replay_reproduced_with_rounding_caveat`

The rounding caveat is limited to displayed Product metrics; all task rows are within rounding tolerance.

## Limitations

- No external validation exists.
- No supportive external methodology review exists.
- No independent third-party reproduction has been ingested.
- The method is bounded to the listed OpenML replay tasks.
- The package is inspectable methodology evidence, not a discovery-scored Fund.
- `FUND_FOUND=false` and `notificationAllowed=false`.
