# Prediction vs Observation

| Prediction | Predicted | Observed | Reason |
| --- | --- | --- | --- |
| rp42-01 | repair_expected_to_block_claim | downgraded_random_only_claim | source/protocol split materially changes the random split metric |
| rp42-02 | repair_expected_to_block_claim | downgraded_random_only_claim | source/protocol split materially changes the random split metric |
| rp42-03 | repair_expected_to_not_help | narrowed_duplicate_sensitive_claim | 553 test rows overlapped train feature vectors in the random split |
| rp42-04 | repair_expected_to_not_help | no_material_repair | no train/test duplicate feature overlap was found |
| rp42-05 | repair_expected_to_not_help | no_material_repair | no train/test duplicate feature overlap was found |
