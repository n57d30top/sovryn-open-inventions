# Prediction vs Observation

| targetId | predicted | observed | comparison | baseline | horizon |
| --- | --- | --- | --- | --- | --- |
| temporal-blind-target-119 | low_risk_control | selva_a10 | horizon_sensitive | low_risk_control | wrong | 0.734 | 0.208 | caveat |
| temporal-blind-target-009 | low_risk_control | plotly_apple_finance | horizon_sensitive | low_risk_control | wrong | 0.939 | 0.078 | not_attempted |
| temporal-blind-target-144 | low_risk_control | nab_art_daily_no_noise | horizon_sensitive | low_risk_control | wrong | 0.99 | 0.029 | not_attempted |
| temporal-blind-target-024 | low_risk_control | selva_airpassengers | horizon_sensitive | low_risk_control | wrong | 0.751 | 0.346 | not_attempted |
| temporal-blind-target-049 | low_risk_control | brownlee_airline_passengers | horizon_sensitive | low_risk_control | wrong | 0.751 | 0.346 | ok |
| temporal-blind-target-044 | low_risk_control | datasets_brent_daily | window_sensitive | low_risk_control | wrong | 0.966 | 0.04 | ok |
| temporal-blind-target-029 | low_risk_control | nab_ambient_temperature_failure | window_sensitive | low_risk_control | wrong | 0.844 | 0.06 | ok |
| temporal-blind-target-004 | low_risk_control | brownlee_shampoo_sales | window_sensitive | low_risk_control | wrong | 0.389 | 0.126 | caveat |
| temporal-blind-target-054 | low_risk_control | brownlee_yearly_water_usage | window_sensitive | low_risk_control | wrong | 0.969 | 0.088 | not_attempted |
| temporal-blind-target-069 | low_risk_control | brownlee_daily_births | window_sensitive | low_risk_control | wrong | 0.389 | 0.089 | not_attempted |
| temporal-blind-target-090 | mixed_hard | datasets_covid_countries | low_risk_control | baseline_dominated | wrong | 0.992 | 0.023 | ok |
| temporal-blind-target-105 | mixed_hard | plotly_apple_finance | low_risk_control | baseline_dominated | wrong | 0.939 | 0.078 | ok |
| temporal-blind-target-065 | mixed_hard | brownlee_airline_passengers | low_risk_control | baseline_dominated | wrong | 0.751 | 0.346 | ok |
| temporal-blind-target-115 | mixed_hard | brownlee_monthly_sunspots | low_risk_control | baseline_dominated | wrong | 0.797 | 0.073 | ok |
| temporal-blind-target-125 | mixed_hard | nab_ambient_temperature_failure | low_risk_control | baseline_dominated | wrong | 0.844 | 0.06 | ok |
| temporal-blind-target-150 | mixed_hard | brownlee_yearly_water_usage | inconclusive | baseline_dominated | wrong | 0.969 | 0.088 | ok |
| temporal-blind-target-055 | mixed_hard | selva_a10 | inconclusive | baseline_dominated | wrong | 0.734 | 0.208 | ok |
| temporal-blind-target-040 | mixed_hard | selva_airpassengers | inconclusive | baseline_dominated | wrong | 0.751 | 0.346 | ok |
| temporal-blind-target-060 | mixed_hard | datasets_brent_daily | inconclusive | baseline_dominated | wrong | 0.966 | 0.04 | ok |
| temporal-blind-target-145 | mixed_hard | brownlee_airline_passengers | inconclusive | baseline_dominated | wrong | 0.751 | 0.346 | ok |
