# Target Protocol Matrix

| Target | New vs Batch 13 | Protocol signal | Protocol status | Split-risk type |
| --- | --- | --- | --- | --- |
| UCI Human Activity Recognition Using Smartphones | carry_forward_control | source archive contains train/test files and subject_train/subject_test files | protocol_reproduced | subject_holdout_risk |
| UCI Statlog Shuttle | new | source archive contains train/test files and documentation says the dataset should be tackled by train/test | protocol_reproduced | class_imbalance_and_time_order_note |
| UCI Statlog Landsat Satellite | new | source archive contains sat.trn and sat.tst and documentation says do not use cross-validation | protocol_reproduced | spatial_file_split_risk |
| UCI Letter Recognition | new | source documentation says the first 16000 items are typically used for training and remaining 4000 for testing, but no separate train/test files are provided | protocol_approximated | documentation_order_split_ambiguity |
