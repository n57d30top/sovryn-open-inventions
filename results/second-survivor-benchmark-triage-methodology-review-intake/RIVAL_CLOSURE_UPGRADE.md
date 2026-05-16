# Rival Closure Upgrade

V1 reported rival status mostly as labels. V2 requires a prose decision and a
measurable closure condition per rival.

## Rival Closure Policy

| Rival                                | Closing Evidence                                   | Status Values                         |
| ------------------------------------ | -------------------------------------------------- | ------------------------------------- |
| Simple baseline explains signal      | Model-baseline delta remains above threshold       | closed / still_plausible / stronger   |
| Holdout policy artifact              | Stronger split preserves candidate-relevant delta  | weakened / still_plausible            |
| Negative-control artifact            | Negative control margin remains above threshold    | closed / still_plausible / stronger   |
| Task-size artifact                   | Size heuristic does not select cleaner set than V2 | weakened / still_plausible            |
| Metric artifact                      | Metric sensitivity does not reverse result         | closed / still_plausible              |
| Source identity or duplicate leakage | Source/duplicate probes fail to explain result     | closed / still_plausible              |
| Checklist-only method                | V2 decision rule beats simple comparators          | weakened / still_plausible / stronger |

## Current Closure Boundary

The current package weakens some rivals but does not close all of them:

- Simple baseline is weakened for six rows.
- Negative-control artifact remains strong for spambase.
- Baseline-only ties V2 on the current package.
- Real group/time/entity rivals remain untested.

Rival closure status: `improved_but_not_fully_closed`.
