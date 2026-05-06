# Execution Depth Matrix

| Result | Target type | Highest level | Execution performed | Negative or partial |
| --- | --- | ---: | --- | --- |
| batch6-scikit-learn-iris-reproduction-ladder | public scientific or ML repository with tests/examples | 8 | Loaded the Iris dataset through scikit-learn, ran five-fold stratified cross-validation, trained a heldout LogisticRegression pipeline, and compared against DummyClassifier and DecisionTreeClassifier. | yes |
| batch6-uci-concrete-baseline-reproduction-ladder | public benchmark dataset with measurable baseline | 8 | Fetched UCI dataset id 165 through ucimlrepo, checked basic schema quality, split 1030 rows into train and test partitions, and ran mean, median, and RandomForestRegressor models. | no |
| batch6-diamonds-data-quality-netoff-ladder | public data-quality target | 9 | Loaded 53940 CSV rows with pandas in a network-off sandbox and checked missing cells, duplicate rows, nonpositive numeric values, empty categorical values, positive carat with nonpositive dimensions, and upper-tail price count. | yes |
