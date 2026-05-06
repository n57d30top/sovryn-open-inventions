# Executed Repair Predictions

| Prediction | Target | Repair | Expected | Observed safety | Outcome |
| --- | --- | --- | --- | --- | --- |
| rp42-01 | UCI HAR Smartphones | group-aware split repair | repair_expected_to_block_claim | downgraded_random_only_claim | supported_or_partial |
| rp42-02 | UCI Optical Digits | file-aware source split repair | repair_expected_to_block_claim | downgraded_random_only_claim | supported_or_partial |
| rp42-03 | UCI Letter Recognition | duplicate-aware evaluation | repair_expected_to_not_help | narrowed_duplicate_sensitive_claim | partial_or_failed |
| rp42-04 | UCI Statlog Shuttle | duplicate-aware evaluation | repair_expected_to_not_help | no_material_repair | confirmed_no_improvement_control |
| rp42-05 | scikit-learn digits | duplicate-aware evaluation | repair_expected_to_not_help | no_material_repair | confirmed_no_improvement_control |
