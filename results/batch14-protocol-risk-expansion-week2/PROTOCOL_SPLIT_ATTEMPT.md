# Protocol Split Attempt

| Target | Protocol status | Exact protocol used | Ambiguity or missing documentation |
| --- | --- | --- | --- |
| UCI Human Activity Recognition Using Smartphones | protocol_reproduced | Used source train/X_train.txt and test/X_test.txt with y_train/y_test labels. | No paper protocol beyond source files is claimed; subject grouping is available and has zero train/test overlap. |
| UCI Statlog Shuttle | protocol_reproduced | Used shuttle.trn and shuttle.tst source files; shuttle.trn was decompressed from shuttle.trn.Z before analysis. | Documentation says the original dataset was in time order, then randomized, and a portion removed for validation; the source split is reproducible but the original temporal protocol is not reconstructable. |
| UCI Statlog Landsat Satellite | protocol_reproduced | Used sat.trn and sat.tst source files. | Documentation warns not to use cross-validation and describes image-derived spatial neighborhoods, but exact spatial coordinates are absent. |
| UCI Letter Recognition | protocol_approximated | Used the source-described first 16000 rows for training and remaining 4000 rows for test. | The archive provides one data file and says users typically train on the first 16000 items; no separate train/test files are present, so this is approximated rather than file-reproduced. |

No full official benchmark reproduction claim is made. Protocol status describes what was executed from the public source files and documentation.
