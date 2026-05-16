# Holdout Policy Justification

The first package used first-feature bucket holdouts as a public-safe proxy.
The major-revision review correctly identified this as underjustified.

## V2 Holdout Policy

| Claim type             | Required holdout                                        | Reason                                                        | Falsifier                                 |
| ---------------------- | ------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------- |
| Random split inflation | Stronger split than random; group/entity/time preferred | Random split can overstate performance                        | Delta disappears under stronger split     |
| Entity leakage         | Entity split                                            | Same entity across train/test can inflate metric              | Entity holdout performs like random split |
| Temporal drift         | Time split                                              | Temporal claim requires time ordering                         | Time holdout does not differ from random  |
| Source-family leakage  | Source/family split                                     | Same source family can explain recurrence                     | Family holdout collapses                  |
| Metric fragility       | Metric swap plus repeated split                         | Metric-only effect should not be source claim                 | Ranking stable across metrics             |
| No explicit key        | First-feature bucket only as proxy                      | Public package can test sensitivity but not real independence | Must remain major-caveat only             |

## Current Package Boundary

Current seven-row evidence has:

- random split,
- first-feature bucket holdout,
- public raw-data replay,
- no explicit group/entity/time keys.

Therefore the current holdout policy is documented but not fully validated. The
package may be re-reviewed as a pipeline methodology revision, not as a
discovery-scored benchmark claim.
