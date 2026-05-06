# Split-Risk Vs Leakage-Risk

| target | prior split-risk severity | source macro-F1 | random macro-F1 | delta | leakage-risk finding | relation |
| --- | --- | --- | --- | --- | --- | --- |
| UCI HAR Smartphones | moderate_split_risk | 0.935249 | 0.975267 | 0.040018 | leakage_not_found | leakage_not_found |
| UCI Statlog Shuttle | high_split_risk | 0.382773 | 0.453021 | 0.070248 | leakage_not_testable | leakage_not_testable |
| UCI Letter Recognition | low_or_near_control_split_risk | 0.692537 | 0.689473 | -0.003064 | confirmed_duplicate_overlap | leakage_partially_explains_delta |

Batch 25 did not find enough direct evidence to claim leakage explains the observed split deltas. HAR subject IDs were testable and had zero source train/test subject overlap; Shuttle and Letter lacked group identifiers, so group leakage was not testable rather than cleared.
