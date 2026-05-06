# Target Selection

| target name | source URL | prior batch evidence | protocol-card status | split-risk status | expected leakage-risk type | why selected | safety/publication notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UCI HAR Smartphones | https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip | Batches 13, 14, 21, and 22 showed a source-vs-random macro-F1 delta around the moderate split-risk range; subject_train and subject_test are available. | source_train_test_files_with_subject_ids | moderate_split_risk | subject_overlap_or_subject_mixing_risk | It has explicit subject IDs, so group/subject leakage can be tested rather than guessed. | Public safe wearable-sensor classification; no medical advice claim. |
| UCI Statlog Shuttle | https://archive.ics.uci.edu/static/public/148/statlog+shuttle.zip | Batches 14 and 15 found high split-risk symptoms and rare-class / metric-risk limits on the source split. | source_train_test_files | high_split_risk | class_imbalance_mimics_leakage_risk | It is the strongest prior split-risk target and tests whether leakage is actually found or class imbalance better explains the delta. | Public safe tabular classification. |
| UCI Statlog Landsat Satellite | https://archive.ics.uci.edu/static/public/146/statlog+landsat+satellite.zip | Batches 14, 16, and 20 preserved Landsat as spatial/file/protocol-risk evidence with missing spatial-coordinate limitations. | source_train_test_files | high_split_risk_with_spatial_file_caveat | spatial_file_overlap_not_directly_testable | It anchors source-protocol split evidence but is held for Batch 26 because spatial groups are absent from the public table. | Public safe remote-sensing classification. |
| UCI Letter Recognition | https://archive.ics.uci.edu/static/public/59/letter+recognition.zip | Batches 14, 21, and 22 treated Letter as an approximated row-order protocol and a near-control with low source-vs-random delta. | approximated_row_order_protocol | low_or_near_control_split_risk | low_leakage_control_and_protocol_ambiguity_check | It gives Batch 25 a low-risk/near-control target and tests whether leakage tools overclaim on an easy benchmark. | Public safe letter classification. |
| UCI Vehicle Silhouettes | https://archive.ics.uci.edu/static/public/149/statlog+vehicle+silhouettes.zip | Batches 22 and 23 selected and downgraded Vehicle as an ambiguous shard-layout target with no source-declared canonical split. | protocol_ambiguous_source_shards | ambiguous_or_protocol_weak | file_shard_protocol_ambiguity_blocks_leakage_conclusion | It keeps the required ambiguous/protocol-weak case visible without forcing a false leakage conclusion. | Public safe silhouette classification. |

## Rejected candidates

| candidate | reason |
| --- | --- |
| UCI Optical Digits | Deferred because Batch 25 already has three executed targets and uses HAR/Shuttle/Letter for group, high-risk, and control coverage. |
| UCI Pen-Based Digits | Deferred to avoid another digit-style clear split before leakage hypotheses are narrowed. |
| UCI Image Segmentation | Deferred because Batch 26 should compare image/file risk after leakage-card mechanics are checked. |
| scikit-learn bundled digits control | Rejected this week because Letter already supplies a low-risk public benchmark control linked to Protocol Cards. |
| UCI Breast Cancer Wisconsin Diagnostic | Rejected to avoid medical-adjacent targets in this public-safe computational cycle. |
