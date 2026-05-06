# Claim Safety Prediction Candidates

| Id | Target | Domain | Claim type | Predicted label |
| --- | --- | --- | --- | --- |
| FBP-01 | sklearn_digits_control | benchmark_protocol_validation | benchmark_performance_claim | claim_allowed_with_caveats |
| FBP-02 | uci_har_prior_artifact | benchmark_protocol_validation | protocol_first_evaluation_claim | claim_allowed |
| FBP-03 | batch25_shuttle_leakage | leakage_risk_detection | leakage_risk_claim | claim_downgraded |
| FBP-04 | vehicle_ambiguous_protocol | leakage_risk_detection | leakage_risk_claim | not_testable_due_missing_fields |
| FBP-05 | sovryn_cli_help | repo_test_reproduction | repo_test_reproduction_claim | claim_allowed |
| FBP-06 | sovryn_npm_test | repo_test_reproduction | repo_test_reproduction_claim | claim_allowed_with_caveats |
| FBP-07 | sklearn_wine_quality | dataset_quality_reliability | dataset_quality_claim | claim_allowed |
| FBP-08 | sklearn_iris_quality | dataset_quality_reliability | dataset_quality_claim | claim_allowed |
| FBP-09 | statsmodels_sunspots_temporal | time_series_temporal_evaluation | time_series_anomaly_claim | claim_allowed_with_caveats |
| FBP-10 | shuffled_temporal_control | time_series_temporal_evaluation | time_series_anomaly_claim | claim_downgraded |
| FBP-11 | batch41_risk_detector | tool_usefulness | tool_usefulness_claim | claim_downgraded |
| FBP-12 | metric_stress_validator_support | tool_usefulness | tool_usefulness_claim | claim_allowed_with_caveats |
| FBP-13 | required_evidence_field_boundary | conceptual_principle | conceptual_principle_claim | claim_allowed_with_caveats |
| FBP-14 | cross_domain_transfer_claim_batch51 | conceptual_principle | cross_domain_transfer_claim | claim_downgraded |
| FBP-15 | benchmark_repair_standard_prior | benchmark_repair | repair_success_claim | claim_blocked |
| FBP-16 | duplicate_aware_repair_prior | benchmark_repair | repair_success_claim | claim_downgraded |
| FBP-17 | package_import_markupsafe | repo_test_reproduction | repo_test_reproduction_claim | claim_allowed |
| FBP-18 | package_import_itsdangerous | repo_test_reproduction | repo_test_reproduction_claim | claim_allowed |
| FBP-19 | sklearn_linnerud_quality | dataset_quality_reliability | dataset_quality_claim | claim_allowed_with_caveats |
| FBP-20 | digits_leakage_control | leakage_risk_detection | leakage_risk_claim | claim_blocked |
| FBP-21 | wine_metric_claim | benchmark_protocol_validation | benchmark_performance_claim | claim_allowed_with_caveats |
| FBP-22 | sunspots_replay_claim | time_series_temporal_evaluation | time_series_anomaly_claim | claim_allowed_with_caveats |
| FBP-23 | tool_value_compression_claim | tool_usefulness | tool_usefulness_claim | claim_downgraded |
| FBP-24 | conceptual_transfer_low_risk | conceptual_principle | conceptual_principle_claim | claim_allowed_with_caveats |
| FBP-25 | unexecuted_openml_candidate | benchmark_protocol_validation | benchmark_performance_claim | claim_blocked |
| FBP-26 | package_without_tests_candidate | repo_test_reproduction | repo_test_reproduction_claim | claim_downgraded |
| FBP-27 | ambiguous_dataset_quality_candidate | dataset_quality_reliability | dataset_quality_claim | not_testable_due_missing_fields |
| FBP-28 | repair_no_before_after_candidate | benchmark_repair | repair_success_claim | claim_blocked |
| FBP-29 | leakage_group_absent_candidate | leakage_risk_detection | leakage_risk_claim | not_testable_due_missing_fields |
| FBP-30 | principle_without_rivals_candidate | conceptual_principle | conceptual_principle_claim | claim_blocked |
