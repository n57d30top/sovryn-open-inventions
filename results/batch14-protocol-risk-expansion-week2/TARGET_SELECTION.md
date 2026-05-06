# Target Selection

| Target | Source URL | New vs Batch 13 | Why selected | Protocol/split signal | Expected split-risk type | Safety notes |
| --- | --- | --- | --- | --- | --- | --- |
| UCI Human Activity Recognition Using Smartphones | https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip | carry_forward_control | Public safe benchmark selected for protocol-risk expansion. | source archive contains train/test files and subject_train/subject_test files | subject_holdout_risk | Safe public computational benchmark; no private or unsafe data. |
| UCI Statlog Shuttle | https://archive.ics.uci.edu/static/public/148/statlog+shuttle.zip | new | Public safe benchmark selected for protocol-risk expansion. | source archive contains train/test files and documentation says the dataset should be tackled by train/test | class_imbalance_and_time_order_note | Safe public computational benchmark; no private or unsafe data. |
| UCI Statlog Landsat Satellite | https://archive.ics.uci.edu/static/public/146/statlog+landsat+satellite.zip | new | Public safe benchmark selected for protocol-risk expansion. | source archive contains sat.trn and sat.tst and documentation says do not use cross-validation | spatial_file_split_risk | Safe public computational benchmark; no private or unsafe data. |
| UCI Letter Recognition | https://archive.ics.uci.edu/static/public/59/letter+recognition.zip | new | Public safe benchmark selected for protocol-risk expansion. | source documentation says the first 16000 items are typically used for training and remaining 4000 for testing, but no separate train/test files are provided | documentation_order_split_ambiguity | Safe public computational benchmark; no private or unsafe data. |

Rejected alternatives:

| Alternative | Rejection reason |
| --- | --- |
| UCI Optical Recognition of Handwritten Digits | Already used in Batch 13; not needed as a second carry-forward control. |
| UCI Pen-Based Recognition of Handwritten Digits | Already used in Batch 13; Batch 14 needed newer and harder targets. |
| UCI Image Segmentation | Deferred because Shuttle, Landsat, and Letter offered stronger Week 2 coverage of imbalance, spatial/file split, and documentation-order ambiguity. |
| UCI Vehicle Silhouettes follow-up | Deferred because Batch 11 exposed target encoding/fallback risk; it should return only with a dedicated cleanup and protocol card. |
| UCI Statlog Shuttle only | Rejected because Batch 14 needed a four-target severity matrix, not one large imbalanced benchmark. |
