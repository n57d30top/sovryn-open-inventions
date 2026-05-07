# Package Replay Sampling

This result is stage 13 of the Open Verifiable Science OS v1.5 Hardening and Scale Gauntlet.

- Product commit: 3b26cfe3947f2f2d28d64178451cd416b06ee770
- Corpus count: 540 -> 564
- Product tests: 6832 -> 7297 (465 added)
- Targets considered: 1000
- Targets selected/routed/rejected with receipts: 400
- Evidence checks: 2004
- Install/provision/execution attempts: 160
- Quick reject/not-testable/safety-control outcomes: 45
- Public packages with manifests: 200
- Route errors/caveats: 19 (0.048)
- Package quality issues: 8 (0.04)
- Replay sample: 50 sampled, 30 verified, 2 failures, 1 mismatch
- Final status: open_verifiable_science_os_v1_5_candidate

## Class Results

| Class | Targets | Packages | Avg factor | Evidence completeness | Route issue rate | Class status |
| --- | --- | --- | --- | --- | --- | --- |
| claim_review | 50 | 50 | 17.153 | 0.923 | 0 | pass |
| tool_usefulness | 50 | 30 | 17.478 | 0.921 | 0.08 | pass |
| dataset_audit | 50 | 20 | 11.144 | 0.936 | 0.06 | pass |
| benchmark_protocol_audit | 45 | 20 | 10.719 | 0.947 | 0.044 | pass |
| scientific_public_data_triage | 45 | 20 | 10.562 | 0.933 | 0.067 | pass |
| repo_package_reproduction | 45 | 20 | 11.031 | 0.92 | 0.044 | pass |
| formal_counterexample | 40 | 20 | 10.555 | 0.907 | 0.05 | pass |
| temporal_evaluation | 30 | 20 | 7.768 | 0.865 | 0.1 | fail |

## Nonclaims

Bounded OS v1.5 candidate package. It reports receipt-backed class-level evidence only; it does not claim broad acceleration, outside uptake, discovery validation, prize significance, broad autonomous intelligence, regulated professional authority, high-risk capability, or universal validity.
