# Required Evidence by Label

- runtime_reproducible: install succeeds, runtime path succeeds, example/test/smoke evidence is executable, and replay is stable.
- install_only_reproducible: install/provisioning succeeds but runtime evidence is missing or failing.
- static_only_evidence: metadata, docs, or files exist but install/runtime was not executed or unavailable.
- dependency_pin_fragile: dependency pinning or version resolution explains failure.
- dynamic_test_mismatch: smoke evidence and fuller tests disagree.
- hidden_data_dependency: runtime needs unavailable data or artifact state.
- example_missing: executable example path is missing.
- docs_overclaim: docs suggest reproducibility without executable evidence.
- smoke_only_success: only smoke-level execution works.
- replay_unstable: replay diverges or carries material caveat.
- low_risk_control: target is a bounded control and not a reproduction claim.
- inconclusive: evidence is mixed or insufficient.
