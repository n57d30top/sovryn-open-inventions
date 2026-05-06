# Target Selection

| protocolCardId | target | Batch 21 decision | why selected | protocol clarity | replay readiness | expected risk | expected failure mode |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pc21-01-uci-har-smartphones | UCI HAR Smartphones | execute_now | clear/approximated replay, ambiguous case, or low-risk control | clear | ready | subject_holdout_risk | Low ambiguity in file split; subject grouping must remain explicit. |
| pc21-02-uci-statlog-shuttle | UCI Statlog Shuttle | execute_now | clear/approximated replay, ambiguous case, or low-risk control | clear | ready | rare_class_and_time_order_risk | Source split is replayable, but original time-order generation is not fully reconstructable. |
| pc21-03-uci-statlog-landsat | UCI Statlog Landsat Satellite | hold_for_deep_study | clear/approximated replay, ambiguous case, or low-risk control | clear | ready | spatial_file_protocol_risk | Spatial/file context is described but exact geographic grouping is absent. |
| pc21-06-uci-letter-recognition | UCI Letter Recognition | low_risk_control | clear/approximated replay, ambiguous case, or low-risk control | approximated | ready | documentation_order_split_ambiguity | The order split is source-described but not file-separated. |
| pc21-08-uci-vehicle-silhouettes | UCI Vehicle Silhouettes | ambiguous_needs_deep_study | clear/approximated replay, ambiguous case, or low-risk control | ambiguous | ready | file_shard_protocol_ambiguity | Multiple plausible file-shard and random interpretations exist. |

## Rejected/deferred Batch 21 cards

| target | reason |
| --- | --- |
| UCI Optical Digits | deferred to keep Week 2 focused on five cards |
| UCI Pen-Based Digits | deferred to keep Week 2 focused on five cards |
| UCI Image Segmentation | deferred to keep Week 2 focused on five cards |
| UCI Waveform Database Generator | deferred to keep Week 2 focused on five cards |
