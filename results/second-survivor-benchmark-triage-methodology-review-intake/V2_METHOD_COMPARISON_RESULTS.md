# V2 Method Comparison Results

| Method                | Selected plausible claims | Survivor count | Survivor yield | Cost saved | False acceptance | False rejection |
| --------------------- | ------------------------: | -------------: | -------------: | ---------: | ---------------: | --------------: |
| V2 formal rule        |                        17 |             17 |          1.000 |      0.575 |            0.000 |           0.000 |
| baseline-only         |                        25 |             17 |          0.680 |      0.375 |            0.320 |           0.000 |
| reject-all            |                         0 |              0 |          0.000 |      1.000 |            0.000 |           1.000 |
| accept-all            |                        40 |             17 |          0.425 |      0.000 |              n/a |             n/a |
| random                |                       n/a |            n/a |          0.400 |        n/a |              n/a |             n/a |
| holdout-only          |                       n/a |            n/a |          0.607 |        n/a |              n/a |             n/a |
| receipt-only          |                       n/a |            n/a |          0.425 |        n/a |              n/a |             n/a |
| negative-control-only |                       n/a |            n/a |          0.436 |        n/a |              n/a |             n/a |

V2 beats baseline-only on survivor yield: yes

This comparison is still internal/public-package evidence only. It is not external validation and not FUND_FOUND.
