# Field Missingness Decisions

| Missing field class | Default decision | Reason |
| --- | --- | --- |
| blocking required field | claim_blocked or not_testable | The claim lacks the field needed to evaluate its core assertion. |
| baseline field | claim_downgraded | The result may be explained by a simple comparator. |
| negative control field | claim_allowed_with_caveats or downgraded | Anti-hype evidence is absent. |
| replay field | claim_allowed_with_caveats | The observation may not survive rerun. |
| group or protocol field | not_testable_due_missing_fields | Mechanism-specific claims require explicit fields. |
