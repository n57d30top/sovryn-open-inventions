# Release Grade Criteria

## claim_review

- route stability threshold passed
- package manifest present
- replay coverage includes class
- limitations explicit

## tool_usefulness

- route stability threshold passed
- package manifest present
- replay coverage includes class
- limitations explicit

## dataset_audit

- route stability threshold passed
- package manifest present
- replay coverage includes class
- limitations explicit

## benchmark_protocol_audit

- route stability threshold passed
- package manifest present
- replay coverage includes class
- limitations explicit

## scientific_public_data_triage

- route stability threshold passed
- package manifest present
- replay coverage includes class
- limitations explicit

## repo_package_reproduction

- 60 or more deep reproduction executions
- install and runtime tiers separated
- dependency/version checks present
- fresh workspace or container replay sampled
- false reproduction claims blocked

## formal_counterexample

- 60 or more formal route executions
- known/trivial filter present
- counterexample and bounded checks present
- proof/refutation route attempted where feasible
- no checked-proof claim unless actually checked

## temporal_evaluation

- 60 or more executed temporal v2 targets
- false true-fragility positives <= 2
- route/caveat issues <= 10%
- 20 or more public packages
- replay sample complete
