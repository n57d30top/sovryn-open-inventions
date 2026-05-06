# Protocol Cards

Exactly 10 Protocol Cards were created in `protocol-cards/`.

| protocolCardId | target | status | decision | signal |
| --- | --- | --- | --- | --- |
| pc21-01-uci-har-smartphones | UCI HAR Smartphones | clear | execute_now | Archive provides train/test files and subject identifiers. |
| pc21-02-uci-statlog-shuttle | UCI Statlog Shuttle | clear | execute_now | Archive provides shuttle.trn and shuttle.tst; documentation notes time-order and majority-class context. |
| pc21-03-uci-statlog-landsat | UCI Statlog Landsat Satellite | clear | hold_for_deep_study | Archive provides sat.trn and sat.tst and documentation warns against cross-validation. |
| pc21-04-uci-optical-digits | UCI Optical Digits | clear | hold_for_deep_study | Archive provides optdigits.tra and optdigits.tes train/test files. |
| pc21-05-uci-pen-digits | UCI Pen-Based Digits | clear | hold_for_deep_study | Archive provides pendigits.tra and pendigits.tes train/test files. |
| pc21-06-uci-letter-recognition | UCI Letter Recognition | approximated | low_risk_control | Documentation describes first 16000 rows for training and remaining 4000 for testing, but no separate split files. |
| pc21-07-uci-image-segmentation | UCI Image Segmentation | clear | hold_for_deep_study | Archive provides segmentation.data and segmentation.test files with class label first. |
| pc21-08-uci-vehicle-silhouettes | UCI Vehicle Silhouettes | ambiguous | ambiguous_needs_deep_study | Archive provides multiple xaa-xai data shards, but no single canonical train/test split is provided. |
| pc21-09-uci-waveform-generator | UCI Waveform Database Generator | ambiguous | defer | Archive provides generator code and compressed generated data; fixed benchmark split is weakly specified. |
| pc21-10-sklearn-digits-control | scikit-learn bundled digits control | absent | low_risk_control | Bundled low-risk toy dataset with no source-described benchmark split. |
