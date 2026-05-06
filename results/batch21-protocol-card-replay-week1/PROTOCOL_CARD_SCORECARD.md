# Protocol Card Scorecard

| protocolCardId | source clarity | split clarity | access feasibility | execution feasibility | baseline feasibility | replay feasibility | ambiguity risk | scientific usefulness | decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pc21-01-uci-har-smartphones | 90 | 90 | 95 | 95 | 95 | 92 | Low ambiguity in file split; subject grouping must remain explicit. | subject_holdout_risk | execute_now |
| pc21-02-uci-statlog-shuttle | 90 | 90 | 95 | 95 | 95 | 92 | Source split is replayable, but original time-order generation is not fully reconstructable. | rare_class_and_time_order_risk | execute_now |
| pc21-03-uci-statlog-landsat | 90 | 90 | 95 | 95 | 95 | 80 | Spatial/file context is described but exact geographic grouping is absent. | spatial_file_protocol_risk | hold_for_deep_study |
| pc21-04-uci-optical-digits | 90 | 90 | 95 | 95 | 95 | 80 | Writer/source grouping is partly described but not fully exposed in the compact files. | writer_or_file_split_risk | hold_for_deep_study |
| pc21-05-uci-pen-digits | 90 | 90 | 95 | 95 | 95 | 80 | Writer grouping is not fully replayed from the compact train/test files. | writer_or_file_split_risk | hold_for_deep_study |
| pc21-06-uci-letter-recognition | 70 | 65 | 95 | 95 | 95 | 80 | The order split is source-described but not file-separated. | documentation_order_split_ambiguity | low_risk_control |
| pc21-07-uci-image-segmentation | 90 | 90 | 95 | 95 | 95 | 80 | File split is clear, but image-source grouping details are limited. | image_file_split_risk | hold_for_deep_study |
| pc21-08-uci-vehicle-silhouettes | 50 | 40 | 95 | 95 | 95 | 80 | Multiple plausible file-shard and random interpretations exist. | file_shard_protocol_ambiguity | ambiguous_needs_deep_study |
| pc21-09-uci-waveform-generator | 50 | 40 | 60 | 55 | 70 | 45 | Generated data can be replayed in multiple ways; fixed split semantics are weak. | generator_protocol_ambiguity | defer |
| pc21-10-sklearn-digits-control | 35 | 20 | 95 | 95 | 95 | 80 | Useful only as a low-risk control; no source protocol should be invented. | low_risk_protocol_absent_control | low_risk_control |
