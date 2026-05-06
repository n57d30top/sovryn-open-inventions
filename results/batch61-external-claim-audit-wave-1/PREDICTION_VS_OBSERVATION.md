# Prediction vs Observation

| Audit | Prediction | Observation | Outcome |
| --- | --- | --- | --- |
| AUD-01 | blocked | blocked | match |
| AUD-02 | downgraded | downgraded | match |
| AUD-03 | not_testable | not_testable | match |
| AUD-04 | blocked | allowed_with_caveats | mismatch |
| AUD-05 | downgraded | allowed | mismatch |
| AUD-06 | not_testable | allowed_with_caveats | mismatch |
| AUD-07 | blocked | downgraded | mismatch |
| AUD-08 | downgraded | allowed | mismatch |
| AUD-09 | not_testable | blocked | mismatch |
| AUD-10 | blocked | allowed_with_caveats | partial |
| AUD-11 | downgraded | allowed | mismatch |
| AUD-12 | not_testable | not_testable | match |
| AUD-13 | allowed_with_caveats | downgraded | mismatch |
| AUD-14 | allowed_with_caveats | allowed_with_caveats | match |
| AUD-15 | allowed_with_caveats | allowed | mismatch |
