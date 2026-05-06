# Baseline Sanity Checks

| target | model | source accuracy | source macro-F1 | random accuracy | random macro-F1 |
| --- | --- | --- | --- | --- | --- |
| UCI HAR Smartphones | dummy_most_frequent | 0.182219 | 0.051378 | 0.188666 | 0.052907 |
| UCI HAR Smartphones | linear_logistic_sgd | 0.935188 | 0.935249 | 0.97455 | 0.975267 |
| UCI HAR Smartphones | random_forest | 0.922973 | 0.921539 | 0.977604 | 0.977832 |
| UCI Statlog Shuttle | dummy_most_frequent | 0.791586 | 0.126239 | 0.785931 | 0.125734 |
| UCI Statlog Shuttle | linear_logistic_sgd | 0.92869 | 0.382773 | 0.925517 | 0.453021 |
| UCI Statlog Shuttle | random_forest | 0.999379 | 0.6982 | 0.99931 | 0.796026 |
| UCI Letter Recognition | dummy_most_frequent | 0.036 | 0.002673 | 0.04075 | 0.003012 |
| UCI Letter Recognition | linear_logistic_sgd | 0.69375 | 0.692537 | 0.69525 | 0.689473 |
| UCI Letter Recognition | random_forest | 0.95175 | 0.951615 | 0.95725 | 0.957113 |

These are sanity checks only. They are not benchmark-win claims.
