# Standalone Replay Results

This replay fetches public OpenML ARFF files and recomputes the receipt-first second-survivor metrics without reading Product `.sovryn` state.

| Claim                     | Task |  Rows | Features | Baseline | Random | Holdout | Model-baseline delta | Random-holdout delta | Negative | Exact Product metrics | Within rounding tolerance |
| ------------------------- | ---: | ----: | -------: | -------: | -----: | ------: | -------------------: | -------------------: | -------: | --------------------- | ------------------------- |
| SA-PLAUS-003-OPENML-32    |   32 | 10992 |       16 |    0.094 |  0.187 |   0.000 |                0.093 |                0.187 |    0.106 | no                    | yes                       |
| SECOND-SURV-001-OPENML-59 |   59 |   150 |        4 |    0.222 |  0.511 |   0.000 |                0.289 |                0.511 |    0.222 | yes                   | yes                       |
| SECOND-SURV-003-OPENML-7  |    7 |   226 |       69 |    0.250 |  0.500 |   0.000 |                0.250 |                0.500 |    0.059 | yes                   | yes                       |
| SECOND-SURV-005-OPENML-53 |   53 |   846 |       18 |    0.232 |  0.398 |   0.176 |                0.165 |                0.221 |    0.228 | yes                   | yes                       |
| SECOND-SURV-006-OPENML-36 |   36 |  2310 |       19 |    0.127 |  0.209 |   0.000 |                0.082 |                0.209 |    0.153 | yes                   | yes                       |
| SECOND-SURV-007-OPENML-43 |   43 |  4601 |       57 |    0.610 |  0.653 |   0.000 |                0.043 |                0.653 |    0.652 | yes                   | yes                       |
| SECOND-SURV-008-OPENML-15 |   15 |   699 |        9 |    0.671 |  0.790 |   0.000 |                0.119 |                0.790 |    0.600 | yes                   | yes                       |

OpenML-32 differs from the Product rounded table by 0.001 on two displayed metrics; all other displayed Product metrics reproduce exactly. This package therefore treats standalone replay as supportive inspectability evidence with a rounding caveat, not as external validation.

This is public-data replay, not external validation. External review remains required before any discovery-scored promotion.
