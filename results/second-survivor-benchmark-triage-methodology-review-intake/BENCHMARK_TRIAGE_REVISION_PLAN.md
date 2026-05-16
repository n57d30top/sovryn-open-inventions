# Benchmark-Triage Revision Plan

Objective: revise the package without strengthening the claim or treating the
major-revision review as acceptance.

## 1. Convert Checklist Into Method

Define a small, executable method specification:

- input schema for benchmark claims,
- required receipts,
- feature extraction from replay, baselines, holdouts, rivals, and controls,
- deterministic scoring rule,
- retention/rejection threshold,
- calibrated abstain state,
- explicit failure modes.

Deliverable: `RECEIPT_FIRST_TRIAGE_METHOD_V2.md`

## 2. Strengthen Reject-All Comparison

Evaluate against:

- reject-all,
- accept-all,
- random selection,
- baseline-only heuristic,
- replay-only heuristic,
- source-family-only heuristic,
- prior V2/V3/V4 methods.

Required success condition: the method must beat reject-all on useful retained
claims or remain a non-scoring pipeline package.

Deliverable: `REJECT_ALL_AND_BASELINE_COMPARISON.md`

## 3. Justify Holdout Policy

Create a policy table:

| Claim type       | Required holdout           | Why                                 | Falsifier                  |
| ---------------- | -------------------------- | ----------------------------------- | -------------------------- |
| leakage          | group/entity/time holdout  | leakage requires independence test  | holdout delta disappears   |
| temporal drift   | time split                 | drift requires temporal ordering    | random-only result fails   |
| metric fragility | metric swap/repeated split | metric sensitivity must be isolated | rank stable across metrics |
| recurrence       | independent task/family    | recurrence cannot be single-task    | no second support          |

Deliverable: `HOLDOUT_POLICY_JUSTIFICATION.md`

## 4. Upgrade Negative Controls

Add controls that can falsify the method:

- shuffled target,
- permuted group key,
- duplicate-row injection/removal,
- metric-swap control,
- label-frequency-only model,
- split-key ablation,
- task-receipt removal control.

Deliverable: `NEGATIVE_CONTROL_UPGRADE.md`

## 5. Deepen Rival Closure

For every retained claim, require measurable rival tests:

- class imbalance,
- dataset size,
- source family,
- model instability,
- metric artifact,
- duplicate leakage,
- preprocessing artifact,
- group/time/entity split artifact.

Deliverable: `RIVAL_CLOSURE_MATRIX.md`

## 6. Add Comparative Ablations

Run ablations:

- no receipts,
- no replay,
- no holdout policy,
- no negative controls,
- no rival closure,
- no recurrence requirement,
- full method.

Measure:

- weak-claim rejection,
- useful-claim retention,
- false rejection,
- survivor yield,
- cost saved,
- review burden.

Deliverable: `TRIAGE_METHOD_ABLATION_RESULTS.md`

## Promotion Boundary

After revision, the candidate may only improve if:

- a public review URL exists,
- source receipt passes,
- reviewer independence is public and verifiable,
- major-revision blockers are addressed,
- reject-all is beaten on survivor yield,
- the claim remains bounded,
- Product Fund Gate remains honest.
