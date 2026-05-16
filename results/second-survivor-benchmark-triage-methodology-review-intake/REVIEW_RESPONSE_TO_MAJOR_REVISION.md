# Response To Major-Revision Review

Decision received: `major_revision`

The review is treated as revision guidance only because no public review URL or
source receipt exists.

## Reviewer Concern: Checklist vs Real Methodology

Response:

- Added `BENCHMARK_TRIAGE_METHOD_V2.md`.
- Added `BENCHMARK_TRIAGE_FORMAL_RULES.json`.
- Defined formal inputs, scoring formula, output classes, blockers, falsifiers,
  and limitations.

Status: partially addressed.

## Reviewer Concern: Reject-All Comparison Too Weak

Response:

- Added `COMPARATIVE_ABLATION_PLAN.md`.
- Added `COMPARATIVE_ABLATION_RESULTS.md`.
- Compared V2 against reject-all, accept-all, task-size, holdout-only, and
  baseline-only.

Result:

- V2 beats reject-all on review yield.
- V2 beats accept-all and holdout-only by demoting a weak negative-control row.
- V2 does not beat baseline-only on the current seven-row package.

Status: not fully closed.

## Reviewer Concern: Holdout Policy Underjustified

Response:

- Added `HOLDOUT_POLICY_JUSTIFICATION.md`.
- Added `HOLDOUT_POLICY_RESULTS.md`.
- Separated first-feature bucket holdouts from real group/time/entity holdouts.

Status: partially addressed, but current evidence remains proxy-only.

## Reviewer Concern: Negative Controls Too Weak

Response:

- Added `NEGATIVE_CONTROL_UPGRADE.md`.
- Added `NEGATIVE_CONTROL_RESULTS.md`.
- Added negative-control margin rule.
- Demoted `SECOND-SURV-007-OPENML-43` because negative-control margin is 0.001.

Status: improved for available controls; full closure requires additional
controls.

## Reviewer Concern: Rival Closure Too Shallow

Response:

- Added `RIVAL_CLOSURE_UPGRADE.md`.
- Added `RIVAL_CLOSURE_EVIDENCE.md`.
- Replaced blanket labels with per-row rival prose.

Status: improved, not fully closed.

## Reviewer Concern: Comparative Ablations Missing

Response:

- Added initial comparator table.
- Explicitly records that V2 ties baseline-only on current rows.

Status: partially addressed; larger mixed benchmark required.

## Final Response

The revision makes the package suitable for another methodology review pass, but
does not warrant discovery scoring. The candidate remains
`pipeline_fund_candidate_major_revision_revised_awaiting_re_review`.
