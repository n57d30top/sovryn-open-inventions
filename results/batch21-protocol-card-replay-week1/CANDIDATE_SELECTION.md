# Candidate Selection

| target | source | why selected | expected protocol signal | expected replay feasibility | expected split-risk type | expected ambiguity | safety note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UCI HAR Smartphones | https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip | covers protocol-card replay pool | Archive provides train/test files and subject identifiers. | ready | subject_holdout_risk | Low ambiguity in file split; subject grouping must remain explicit. | Public safe human-activity sensor classification; no medical advice claim. |
| UCI Statlog Shuttle | https://archive.ics.uci.edu/static/public/148/statlog+shuttle.zip | covers protocol-card replay pool | Archive provides shuttle.trn and shuttle.tst; documentation notes time-order and majority-class context. | ready | rare_class_and_time_order_risk | Source split is replayable, but original time-order generation is not fully reconstructable. | Public safe tabular classification. |
| UCI Statlog Landsat Satellite | https://archive.ics.uci.edu/static/public/146/statlog+landsat+satellite.zip | covers protocol-card replay pool | Archive provides sat.trn and sat.tst and documentation warns against cross-validation. | ready | spatial_file_protocol_risk | Spatial/file context is described but exact geographic grouping is absent. | Public safe remote-sensing classification. |
| UCI Optical Digits | https://archive.ics.uci.edu/static/public/80/optical+recognition+of+handwritten+digits.zip | covers protocol-card replay pool | Archive provides optdigits.tra and optdigits.tes train/test files. | ready | writer_or_file_split_risk | Writer/source grouping is partly described but not fully exposed in the compact files. | Public safe digit recognition. |
| UCI Pen-Based Digits | https://archive.ics.uci.edu/static/public/81/pen+based+recognition+of+handwritten+digits.zip | covers protocol-card replay pool | Archive provides pendigits.tra and pendigits.tes train/test files. | ready | writer_or_file_split_risk | Writer grouping is not fully replayed from the compact train/test files. | Public safe digit recognition. |
| UCI Letter Recognition | https://archive.ics.uci.edu/static/public/59/letter+recognition.zip | covers protocol-card replay pool | Documentation describes first 16000 rows for training and remaining 4000 for testing, but no separate split files. | ready | documentation_order_split_ambiguity | The order split is source-described but not file-separated. | Public safe letter classification. |
| UCI Image Segmentation | https://archive.ics.uci.edu/static/public/50/image+segmentation.zip | covers protocol-card replay pool | Archive provides segmentation.data and segmentation.test files with class label first. | ready | image_file_split_risk | File split is clear, but image-source grouping details are limited. | Public safe image-derived classification. |
| UCI Vehicle Silhouettes | https://archive.ics.uci.edu/static/public/149/statlog+vehicle+silhouettes.zip | covers protocol-card replay pool | Archive provides multiple xaa-xai data shards, but no single canonical train/test split is provided. | ready | file_shard_protocol_ambiguity | Multiple plausible file-shard and random interpretations exist. | Public safe silhouette classification. |
| UCI Waveform Database Generator | https://archive.ics.uci.edu/static/public/107/waveform+database+generator+version+1.zip | covers protocol-card replay pool | Archive provides generator code and compressed generated data; fixed benchmark split is weakly specified. | deferred | generator_protocol_ambiguity | Generated data can be replayed in multiple ways; fixed split semantics are weak. | Public safe synthetic waveform classification. |
| scikit-learn bundled digits control | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html | covers protocol-card replay pool | Bundled low-risk toy dataset with no source-described benchmark split. | ready | low_risk_protocol_absent_control | Useful only as a low-risk control; no source protocol should be invented. | Public safe built-in toy dataset. |

## Rejected candidates

| candidate | reason |
| --- | --- |
| UCI Breast Cancer Wisconsin Diagnostic | Deferred because the program avoids medical-adjacent targets for this cycle. |
| OpenML arbitrary task search | Deferred because a stable documented split was less certain than the selected public archives. |
| CIFAR-10 | Deferred due size and because Batch 21 needs small replayable cards first. |
| MNIST full dataset | Deferred due mirror/access and because UCI digit targets already cover clear file splits. |
| Any private Kaggle task | Rejected because private account-gated data is outside public-safe scope. |
