# Prediction vs Observation

| Id | Expected | Observed | Interpretation |
| --- | --- | --- | --- |
| FBP-01 | claim_allowed_with_caveats | claim_allowed_with_caveats | match |
| FBP-02 | claim_allowed | claim_allowed | match |
| FBP-03 | claim_downgraded | claim_downgraded | match |
| FBP-04 | not_testable_due_missing_fields | not_testable_due_missing_fields | match |
| FBP-05 | claim_allowed | claim_allowed | match |
| FBP-06 | claim_allowed_with_caveats | claim_allowed_with_caveats | match |
| FBP-07 | claim_allowed | claim_allowed | match |
| FBP-08 | claim_allowed | claim_allowed | match |
| FBP-09 | claim_allowed_with_caveats | claim_allowed_with_caveats | match |
| FBP-10 | claim_downgraded | claim_blocked | partial_or_stronger_than_predicted |
| FBP-11 | claim_downgraded | claim_downgraded | match |
| FBP-12 | claim_allowed_with_caveats | claim_allowed_with_caveats | match |
| FBP-13 | claim_allowed_with_caveats | claim_allowed_with_caveats | match |
| FBP-14 | claim_downgraded | claim_downgraded | match |
| FBP-15 | claim_blocked | claim_blocked | partial_or_stronger_than_predicted |
| FBP-16 | claim_downgraded | claim_downgraded | match |
