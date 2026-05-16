# Rival Closure Evidence

Source:

- `standalone_replay_results.json`
- `BENCHMARK_TRIAGE_FORMAL_RULES.json`
- `COMPARATIVE_ABLATION_RESULTS.md`
- `NEGATIVE_CONTROL_RESULTS.md`

## Per-Row Rival Decisions

| Claim                     | Baseline rival               | Holdout rival         | Negative-control rival | Overall V2 rival decision             |
| ------------------------- | ---------------------------- | --------------------- | ---------------------- | ------------------------------------- |
| SA-PLAUS-003-OPENML-32    | weakened: delta 0.093        | weakened: delta 0.187 | weakened: margin 0.081 | scoped_or_weakened                    |
| SECOND-SURV-001-OPENML-59 | weakened: delta 0.289        | weakened: delta 0.511 | weakened: margin 0.289 | scoped_or_weakened                    |
| SECOND-SURV-003-OPENML-7  | weakened: delta 0.250        | weakened: delta 0.500 | weakened: margin 0.441 | scoped_or_weakened                    |
| SECOND-SURV-005-OPENML-53 | weakened: delta 0.165        | weakened: delta 0.221 | weakened: margin 0.170 | scoped_or_weakened                    |
| SECOND-SURV-006-OPENML-36 | weakened: delta 0.082        | weakened: delta 0.209 | weakened: margin 0.056 | scoped_or_weakened with margin caveat |
| SECOND-SURV-007-OPENML-43 | still_plausible: delta 0.043 | weakened: delta 0.653 | stronger: margin 0.001 | major_revision_caveat_retain          |
| SECOND-SURV-008-OPENML-15 | weakened: delta 0.119        | weakened: delta 0.790 | weakened: margin 0.190 | scoped_or_weakened                    |

## Prose Decision

The V2 evidence does not support a blanket claim that all seven rows weaken the
same rival set. Six rows remain reviewable under V2. One row is explicitly
demoted because a negative-control rival remains stronger than the candidate
mechanism.

This is a meaningful improvement over V1 labeling, but not a full methodology
acceptance. The larger blocker remains comparative method value against
baseline-only and real group/time/entity holdouts.
