# Falsifiers

- runtime_reproducible is falsified by failed runtime, failed replay, hidden data dependency, or full-test mismatch.
- install_only_reproducible is falsified by stable runtime plus replay evidence.
- static_only_evidence is falsified by successful install/runtime evidence.
- dependency_pin_fragile is falsified by stable pinned and unpinned installs.
- dynamic_test_mismatch is falsified by full-test success matching smoke success.
- hidden_data_dependency is falsified by public artifact retrieval and replay.
- example_missing is falsified by an executable public example.
- docs_overclaim is falsified by docs that point to executable tests/examples that run.
- smoke_only_success is falsified by full-test or example success.
- replay_unstable is falsified by fresh workspace replay support.
- low_risk_control is falsified by evidence that it is a real reproduction claim.
- inconclusive is resolved by missing evidence becoming available.
