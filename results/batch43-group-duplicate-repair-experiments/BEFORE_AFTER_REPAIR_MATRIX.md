# Before/After Repair Matrix

| Prediction | Target | Before acc | Before macro-F1 | After acc | After macro-F1 | Claim safety |
| --- | --- | --- | --- | --- | --- | --- |
| rp42-01 | UCI HAR Smartphones | 0.982 | 0.9832 | 0.8967 | 0.9009 | downgraded_random_only_claim |
| rp42-02 | UCI Optical Digits | 0.9722 | 0.9722 | 0.9499 | 0.95 | downgraded_random_only_claim |
| rp42-03 | UCI Letter Recognition | 0.771 | 0.7692 | 0.7531 | 0.7507 | narrowed_duplicate_sensitive_claim |
| rp42-04 | UCI Statlog Shuttle | 0.9654 | 0.62 | 0.9654 | 0.62 | no_material_repair |
| rp42-05 | scikit-learn digits | 0.9815 | 0.9814 | 0.9815 | 0.9814 | no_material_repair |
