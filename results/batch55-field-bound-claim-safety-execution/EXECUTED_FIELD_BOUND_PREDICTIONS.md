# Executed Field-Bound Predictions

| Id | Target | Domain | Predicted | Observed | Outcome |
| --- | --- | --- | --- | --- | --- |
| FBP-01 | sklearn_digits_control | benchmark_protocol_validation | claim_allowed_with_caveats | claim_allowed_with_caveats | match |
| FBP-02 | uci_har_prior_artifact | benchmark_protocol_validation | claim_allowed | claim_allowed | match |
| FBP-03 | batch25_shuttle_leakage | leakage_risk_detection | claim_downgraded | claim_downgraded | match |
| FBP-04 | vehicle_ambiguous_protocol | leakage_risk_detection | not_testable_due_missing_fields | not_testable_due_missing_fields | match |
| FBP-05 | sovryn_cli_help | repo_test_reproduction | claim_allowed | claim_allowed | match |
| FBP-06 | sovryn_npm_test | repo_test_reproduction | claim_allowed_with_caveats | claim_allowed_with_caveats | match |
| FBP-07 | sklearn_wine_quality | dataset_quality_reliability | claim_allowed | claim_allowed | match |
| FBP-08 | sklearn_iris_quality | dataset_quality_reliability | claim_allowed | claim_allowed | match |
| FBP-09 | statsmodels_sunspots_temporal | time_series_temporal_evaluation | claim_allowed_with_caveats | claim_allowed_with_caveats | match |
| FBP-10 | shuffled_temporal_control | time_series_temporal_evaluation | claim_downgraded | claim_blocked | partial_or_stronger_than_predicted |
| FBP-11 | batch41_risk_detector | tool_usefulness | claim_downgraded | claim_downgraded | match |
| FBP-12 | metric_stress_validator_support | tool_usefulness | claim_allowed_with_caveats | claim_allowed_with_caveats | match |
| FBP-13 | required_evidence_field_boundary | conceptual_principle | claim_allowed_with_caveats | claim_allowed_with_caveats | match |
| FBP-14 | cross_domain_transfer_claim_batch51 | conceptual_principle | claim_downgraded | claim_downgraded | match |
| FBP-15 | benchmark_repair_standard_prior | benchmark_repair | claim_blocked | claim_blocked | partial_or_stronger_than_predicted |
| FBP-16 | duplicate_aware_repair_prior | benchmark_repair | claim_downgraded | claim_downgraded | match |
