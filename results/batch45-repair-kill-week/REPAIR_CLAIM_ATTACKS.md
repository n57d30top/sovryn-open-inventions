# Repair Claim Attacks

| Prediction | Target | Repair | Observed outcome | Claim-safety label |
| --- | --- | --- | --- | --- |
| rp42-01 | UCI HAR Smartphones | group-aware split repair | supported_or_partial | downgraded_random_only_claim |
| rp42-02 | UCI Optical Digits | file-aware source split repair | supported_or_partial | downgraded_random_only_claim |
| rp42-03 | UCI Letter Recognition | duplicate-aware evaluation | partial_or_failed | narrowed_duplicate_sensitive_claim |
| rp42-04 | UCI Statlog Shuttle | duplicate-aware evaluation | confirmed_no_improvement_control | no_material_repair |
| rp42-05 | scikit-learn digits | duplicate-aware evaluation | confirmed_no_improvement_control | no_material_repair |
| rp42-06 | UCI Vehicle Silhouettes | ambiguity gate | supported_or_partial | blocked_or_needs_clarification |
| rp42-07 | scikit-learn wine | ambiguity gate | supported_or_partial | blocked_or_needs_clarification |
| rp42-08 | UCI Statlog Shuttle | rare-class metric reporting | supported | downgraded_accuracy_only_claim |
| rp42-09 | UCI Letter Recognition | rare-class metric reporting | confirmed_no_improvement_control | preserved_low_risk_metric_claim |
| rp42-10 | UCI Image Segmentation | ambiguity gate | supported_or_partial | pass_with_caveats |
