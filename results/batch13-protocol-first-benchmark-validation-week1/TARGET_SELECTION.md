# Target Selection

Selected targets:

| Target | Source URL | Why selected | Protocol/split signal | Expected baseline feasibility | Expected risk |
| --- | --- | --- | --- | --- | --- |
| UCI Human Activity Recognition Using Smartphones | https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip | Public safe benchmark with explicit source split files. | source archive contains train/test files and subject_train/subject_test files | Dummy, LogisticRegression, and RandomForest are feasible. | ordinary random split can mix subjects and weaken the source holdout question |
| UCI Optical Recognition of Handwritten Digits | https://archive.ics.uci.edu/static/public/80/optical+recognition+of+handwritten+digits.zip | Public safe benchmark with explicit source split files. | source archive contains optdigits.tra and optdigits.tes files | Dummy, LogisticRegression, and RandomForest are feasible. | random split may hide source train/test distribution differences |
| UCI Pen-Based Recognition of Handwritten Digits | https://archive.ics.uci.edu/static/public/81/pen+based+recognition+of+handwritten+digits.zip | Public safe benchmark with explicit source split files. | source archive contains pendigits.tra and pendigits.tes files | Dummy, LogisticRegression, and RandomForest are feasible. | random split may not test the same source-provided holdout distribution |

Rejected alternatives:

| Alternative | Rejection reason |
| --- | --- |
| UCI Letter Recognition | Deferred because the Week 1 program prioritized explicit separate train/test files over documentation-only split conventions. |
| UCI Statlog Landsat Satellite | Deferred because the loader/protocol details need a larger Week 2 expansion pass. |
| UCI Statlog Shuttle | Deferred because class imbalance and target size make it better for the Week 2 stress expansion, not the first three-target proof. |
| UCI Statlog Vehicle Silhouettes follow-up | Deferred because Batch 11 already exposed a target-quality failure; it should return only with a dedicated protocol card. |
