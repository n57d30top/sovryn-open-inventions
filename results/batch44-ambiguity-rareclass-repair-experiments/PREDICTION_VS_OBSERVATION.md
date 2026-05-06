# Prediction vs Observation

| Prediction | Predicted | Observed | Reason |
| --- | --- | --- | --- |
| rp42-06 | repair_expected_to_reveal_ambiguity | blocked_or_needs_clarification | Multiple plausible split interpretations exist and no single source train/test protocol is public enough for a strong protocol-first claim. |
| rp42-07 | repair_expected_to_block_claim | blocked_or_needs_clarification | No source train/test protocol is present; protocol-first claim should be blocked while ordinary baseline reporting may continue. |
| rp42-08 | repair_expected_to_help | downgraded_accuracy_only_claim | macro/per-class evidence exposes rare-class weakness |
| rp42-09 | repair_expected_to_not_help | preserved_low_risk_metric_claim | macro and accuracy remain aligned |
| rp42-10 | repair_expected_to_reveal_ambiguity | pass_with_caveats | Source files exist, but train/test size asymmetry makes broad claims require caveats. |
