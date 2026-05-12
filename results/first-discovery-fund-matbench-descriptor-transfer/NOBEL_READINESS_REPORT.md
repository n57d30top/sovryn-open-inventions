# Nobel Discovery Readiness Layer v0

## Decision

Final public label: `not_discovery_scored_raw_reproduction_failed`.

The historical Product package recorded `externally_review_ready_candidate`, but the raw scientific reproduction repair found that the Matbench values are runtime-derived deterministic Product scalars rather than independently reproduced raw-data scientific outputs. Public Einstein/Nobel discovery-score eligibility is therefore downgraded to `false`.

## Evidence Summary

- Historical Product readiness score: 72/100.
- Public readiness score after raw-data reproduction repair: 28/100.
- Public outside expert review readiness score for this discovery claim: 0/100.
- Safety score: 100/100.
- Overclaim risk score: 22/100.
- Public Einstein/Nobel discovery-score eligible: false.

## Claim Boundary

This package now claims only that the Product runtime package can be inspected and its scalar values can be replayed from the documented Product runtime formula. It does not claim outside review, prize significance, external validation, or raw-data scientific reproduction.

## Score Impact

- FundClass used for public discovery scoring: `not_discovery_scored_raw_reproduction_failed`.
- Discovery-scored candidate count contributed by this package: 0.
- Externally-review-ready discovery candidate count contributed by this package: 0.
- Reason: exact raw-data descriptor-transfer residual and baseline recomputation failed because the public package lacks the descriptor matrix, model/training config, split/family manifest, residual formula, executable baselines, and holdout/counterexample manifests.
