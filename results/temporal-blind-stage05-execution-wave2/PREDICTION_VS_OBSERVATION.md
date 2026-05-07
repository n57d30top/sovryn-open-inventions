# Prediction vs Observation

| targetId | predicted | observed | comparison | baseline | horizon |
| --- | --- | --- | --- | --- | --- |
| temporal-blind-target-137 | temporal_classification | plotly_apple_finance | baseline_dominated | baseline_dominated | correct | 0.939 | 0.078 | ok |
| temporal-blind-target-052 | temporal_classification | brownlee_shampoo_sales | baseline_dominated | true_temporal_fragility_candidate | wrong | 0.389 | 0.126 | caveat |
| temporal-blind-target-037 | temporal_classification | brownlee_daily_births | baseline_dominated | inconclusive | wrong | 0.389 | 0.089 | ok |
| temporal-blind-target-022 | temporal_classification | brownlee_yearly_water_usage | baseline_dominated | baseline_dominated | correct | 0.969 | 0.088 | ok |
| temporal-blind-target-017 | temporal_classification | brownlee_airline_passengers | baseline_dominated | baseline_dominated | correct | 0.751 | 0.346 | caveat |
| temporal-blind-target-072 | temporal_classification | selva_airpassengers | baseline_dominated | baseline_dominated | correct | 0.751 | 0.346 | not_attempted |
| temporal-blind-target-087 | temporal_classification | selva_a10 | baseline_dominated | baseline_dominated | correct | 0.734 | 0.208 | not_attempted |
| temporal-blind-target-047 | temporal_classification | nab_nyc_taxi | baseline_dominated | baseline_dominated | correct | 0.872 | 0.289 | ok |
| temporal-blind-target-117 | temporal_classification | brownlee_daily_births | baseline_dominated | inconclusive | wrong | 0.389 | 0.089 | not_attempted |
| temporal-blind-target-082 | temporal_classification | brownlee_daily_min_temperature | baseline_dominated | true_temporal_fragility_candidate | wrong | 0.647 | 0.155 | ok |
| temporal-blind-target-108 | anomaly | datasets_brent_daily | leakage_artifact | window_sensitive | wrong | 0.966 | 0.04 | not_attempted |
| temporal-blind-target-068 | anomaly | brownlee_shampoo_sales | leakage_artifact | true_temporal_fragility_candidate | wrong | 0.389 | 0.126 | caveat |
| temporal-blind-target-053 | anomaly | brownlee_daily_births | leakage_artifact | inconclusive | wrong | 0.389 | 0.089 | ok |
| temporal-blind-target-118 | anomaly | brownlee_yearly_water_usage | leakage_artifact | inconclusive | wrong | 0.969 | 0.088 | ok |
| temporal-blind-target-013 | anomaly | nab_ambient_temperature_failure | leakage_artifact | inconclusive | wrong | 0.844 | 0.06 | ok |
| temporal-blind-target-043 | anomaly | datasets_vix_daily | shuffled_time_artifact | inconclusive | wrong | 0.87 | 0.077 | ok |
| temporal-blind-target-148 | anomaly | brownlee_shampoo_sales | shuffled_time_artifact | true_temporal_fragility_candidate | wrong | 0.389 | 0.126 | caveat |
| temporal-blind-target-008 | anomaly | selva_airpassengers | shuffled_time_artifact | horizon_sensitive | wrong | 0.751 | 0.346 | ok |
| temporal-blind-target-093 | anomaly | nab_ambient_temperature_failure | shuffled_time_artifact | inconclusive | wrong | 0.844 | 0.06 | not_attempted |
| temporal-blind-target-033 | anomaly | brownlee_airline_passengers | shuffled_time_artifact | horizon_sensitive | wrong | 0.751 | 0.346 | not_attempted |
