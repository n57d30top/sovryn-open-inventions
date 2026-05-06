# Claim Boundary Rules

| Rule | Trigger | Decision |
| --- | --- | --- |
| R01 | missing_source_binding | Block or mark not-testable when no public source or artifact source is bound. |
| R02 | missing_required_protocol | Downgrade benchmark and protocol claims when the split or runtime protocol is absent. |
| R03 | missing_baseline | Block strong performance, tool, and repair claims when no simple baseline exists. |
| R04 | missing_negative_control | Caveat or downgrade claims when no negative control or counter-case is present. |
| R05 | missing_replay | Caveat claims when replay is absent; block replay robustness claims. |
| R06 | ambiguous_group_fields | Mark leakage/group-overlap claims not-testable when group fields are absent or ambiguous. |
| R07 | missing_metric_scope | Downgrade metric claims when accuracy, macro-F1, case support, or comparable metric scope is missing. |
| R08 | missing_failure_cases | Downgrade conceptual and transfer claims when failed or partial cases are absent. |
| R09 | missing_environment | Caveat repo/package execution claims when environment and versions are missing. |
| R10 | missing_artifact_manifest | Block public claim-safety claims when required artifacts are absent. |
| R11 | tool_no_ablation | Downgrade tool usefulness claims when simple baseline or ablation comparison is missing. |
| R12 | transfer_no_scope_update | Downgrade transfer claims when failures do not narrow scope. |
