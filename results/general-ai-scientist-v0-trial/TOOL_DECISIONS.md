# Tool Decisions

- protocol cards: use_existing_tool. Prior Protocol Card work provides source/protocol split bindings.
- leakage-risk cards: use_existing_tool. Batch 25 created the current leakage-risk card format.
- metric_stress_validator: preserve_with_constraints. Useful as anti-hype support, not as leakage proof.
- new product leakage detector: reject_tool_need. Current trial can run with existing public cards and bounded local checks.
- leakage-risk mechanism inference: narrow. The trial did not confirm leakage as the cause of split deltas.
- Node/npm runtime: use_existing_tool. Repo/test reproduction can execute bounded runtime probes with the current product toolchain.
- pytest_repro_summary: narrow. Prior evidence keeps it support-only unless runtime collection is available.
- new generic agent swarm: reject_tool_need. A concrete bounded service is sufficient; no broad framework is promoted.
- repo/test reproduction route: preserve_with_constraints. Runtime probes passed, but third-party repository execution remains future work.
