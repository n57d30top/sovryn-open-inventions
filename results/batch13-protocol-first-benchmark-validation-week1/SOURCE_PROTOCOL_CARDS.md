# Source And Protocol Cards

| Target | Dataset source | Documentation | Access method | Train/test or split description | Ambiguity | Protocol reproducible? | Random challenger meaningful? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UCI Human Activity Recognition Using Smartphones | https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip | https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones | Direct UCI static public zip download. | source archive contains train/test files and subject_train/subject_test files | Source files are followed as available; no additional paper protocol is claimed. | Yes, `protocol_reproduced`. | Yes; stratified random split tests convenient-split sensitivity. |
| UCI Optical Recognition of Handwritten Digits | https://archive.ics.uci.edu/static/public/80/optical+recognition+of+handwritten+digits.zip | https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits | Direct UCI static public zip download. | source archive contains optdigits.tra and optdigits.tes files | Source files are followed as available; no additional paper protocol is claimed. | Yes, `protocol_reproduced`. | Yes; stratified random split tests convenient-split sensitivity. |
| UCI Pen-Based Recognition of Handwritten Digits | https://archive.ics.uci.edu/static/public/81/pen+based+recognition+of+handwritten+digits.zip | https://archive.ics.uci.edu/dataset/81/pen+based+recognition+of+handwritten+digits | Direct UCI static public zip download. | source archive contains pendigits.tra and pendigits.tes files | Source files are followed as available; no additional paper protocol is claimed. | Yes, `protocol_reproduced`. | Yes; stratified random split tests convenient-split sensitivity. |

Package/tool sources:

| Tool/package | Source |
| --- | --- |
| pandas | https://pandas.pydata.org/ |
| numpy | https://numpy.org/ |
| scikit-learn | https://scikit-learn.org/ |
| Docker container replay | Public data were provisioned before replay; replay ran with external network disabled. |
