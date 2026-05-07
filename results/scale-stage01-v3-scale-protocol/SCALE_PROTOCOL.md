# Scale Protocol

Objective: test whether route_policy_v3 can scale from two class-level candidate classes to at least four under a larger blind workload.

Target classes:
- claim_review
- tool_usefulness
- repo_package_reproduction
- dataset_audit
- benchmark_protocol_audit
- formal_counterexample
- temporal_evaluation
- scientific_public_data_triage

The run uses no Product changes because v3 already contains class-specific thresholds, confidence calibration, package-quality prediction, and class acceleration scoring.
