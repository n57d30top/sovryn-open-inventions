# Public Review Package Audit

Result slug: `second-survivor-benchmark-triage-methodology-review-intake`

Candidate: `DISCOVERY-BENCH-TRIAGE-SECOND-INDEPENDENT-SURVIVOR-001`

Audit status: ready for external methodology review intake with major caveats.

This audit checks public inspectability only. It does not upgrade the
candidate to discovery-scored status, does not claim external validation, and
does not create `FUND_FOUND`.

## Required Review Contents

| Requirement             | Public file(s)                                                                             | Status  |
| ----------------------- | ------------------------------------------------------------------------------------------ | ------- |
| Bounded claim           | `EXACT_CLAIM.md`, `METHODOLOGY_EXACT_CLAIM.md`, `REVIEWER_SUMMARY.md`                      | present |
| Method description      | `METHOD.md`, `METHODOLOGY_VALUE_TESTS.md`                                                  | present |
| Task list               | `DATASETS_AND_TASKS.md`, `INDEPENDENT_REPRODUCER_PACKAGE.md`                               | present |
| Raw-data receipts       | `DATASETS_AND_TASKS.md`, `PUBLIC_REVIEW_URLS.md`, `reproduce_second_survivor_benchmark.js` | present |
| Replay commands         | `REPRODUCE.md`, `INDEPENDENT_REPRODUCER_README.md`, `REVIEWER_REPLAY_QUICKCHECK.md`        | present |
| Baselines               | `BASELINES.md`, `STANDALONE_REPLAY_RESULTS.md`                                             | present |
| Holdout/split checks    | `HOLDOUT_REPLAY.md`, `STANDALONE_REPLAY_RESULTS.md`                                        | present |
| Rival explanations      | `RIVAL_EXPLANATIONS.md`, `REVIEWER_SUMMARY.md`                                             | present |
| Negative controls       | `NEGATIVE_CONTROLS.md`, `STANDALONE_REPLAY_RESULTS.md`                                     | present |
| Limitations             | `LIMITATIONS.md`, `SUMMARY.json`                                                           | present |
| Claim/evidence bindings | `CLAIM_EVIDENCE_BINDINGS.json`, `EXTERNAL_REVIEW_EVIDENCE_REF_INDEX.md`                    | present |
| Expected outputs        | `EXPECTED_REPRODUCER_OUTPUTS.json`, `STANDALONE_REPLAY_RESULTS.md`                         | present |

## Public Reproducer Check

The public reproducer is `reproduce_second_survivor_benchmark.js`. It fetches
OpenML ARFF files from public URLs, recomputes the bounded replay table, writes
`standalone_replay_results.json`, and does not read Product `.sovryn` state.

The reviewer quickcheck is `reviewer_replay_quickcheck.js`. It reruns the
public reproducer and checks that:

- seven public replay rows are present,
- all survivor rows remain within recorded Product rounding tolerance,
- `fundFound` remains false,
- `countsForDiscoveryScore` remains false,
- no external-validation claim is recorded.

Latest public quickcheck status: passed.

## Remaining Caveat

The package is suitable for a real external methodology reviewer to inspect and
rerun. It is not itself independent external review. Readiness can increase only
after a real external public review URL or independent reproduction record is
ingested with a valid source receipt.
