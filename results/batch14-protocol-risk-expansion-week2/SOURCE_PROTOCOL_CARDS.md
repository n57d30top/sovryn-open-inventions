# Source And Protocol Cards

| Target | Dataset source | Documentation | Access method | Train/test or split description | Protocol ambiguity | Protocol status expectation |
| --- | --- | --- | --- | --- | --- | --- |
| UCI Human Activity Recognition Using Smartphones | https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip | https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones | Direct UCI static public zip; cached after public download for replay. | Used source train/X_train.txt and test/X_test.txt with y_train/y_test labels. | No paper protocol beyond source files is claimed; subject grouping is available and has zero train/test overlap. | likely_protocol_reproduced |
| UCI Statlog Shuttle | https://archive.ics.uci.edu/static/public/148/statlog+shuttle.zip | https://archive.ics.uci.edu/dataset/148/statlog+shuttle | Direct UCI static public zip; cached after public download for replay. | Used shuttle.trn and shuttle.tst source files; shuttle.trn was decompressed from shuttle.trn.Z before analysis. | Documentation says the original dataset was in time order, then randomized, and a portion removed for validation; the source split is reproducible but the original temporal protocol is not reconstructable. | likely_protocol_reproduced |
| UCI Statlog Landsat Satellite | https://archive.ics.uci.edu/static/public/146/statlog+landsat+satellite.zip | https://archive.ics.uci.edu/dataset/146/statlog+landsat+satellite | Direct UCI static public zip; cached after public download for replay. | Used sat.trn and sat.tst source files. | Documentation warns not to use cross-validation and describes image-derived spatial neighborhoods, but exact spatial coordinates are absent. | likely_protocol_reproduced |
| UCI Letter Recognition | https://archive.ics.uci.edu/static/public/59/letter+recognition.zip | https://archive.ics.uci.edu/dataset/59/letter+recognition | Direct UCI static public zip; cached after public download for replay. | Used the source-described first 16000 rows for training and remaining 4000 rows for test. | The archive provides one data file and says users typically train on the first 16000 items; no separate train/test files are present, so this is approximated rather than file-reproduced. | likely_protocol_approximated |

Package/tool sources:

| Tool/package | Source |
| --- | --- |
| pandas | https://pandas.pydata.org/ |
| numpy | https://numpy.org/ |
| scikit-learn | https://scikit-learn.org/ |
| Docker replay | Container replay used pre-provisioned public archives with external network disabled. |
