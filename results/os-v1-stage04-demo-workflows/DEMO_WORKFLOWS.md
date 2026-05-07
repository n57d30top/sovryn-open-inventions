# Demo Workflows

| Demo | Class | Command | Package | Limitations |
| --- | --- | --- | --- | --- |
| Claim Review Demo | claim_review | sovryn route intake --target claim-review-demo --json && sovryn route execute --target claim-review-demo --json | claim decision package with evidence route, limitations, and reproduce note | Does not replace expert review and does not validate broad claims. |
| Tool Usefulness Demo | tool_usefulness | sovryn route plan --target tool-usefulness-demo --json && sovryn route execute --target tool-usefulness-demo --json | tool usefulness brief with static scan, route decision, and caveats | Does not certify production fitness. |
| Dataset Audit Demo | dataset_audit | sovryn route plan --target dataset-audit-demo --json && sovryn route execute --target dataset-audit-demo --json | dataset audit package with evidence checks and failure modes | Does not validate domain-specific scientific conclusions. |
| Benchmark Protocol Audit Demo | benchmark_protocol_audit | sovryn route classify --target benchmark-protocol-demo --json && sovryn route execute --target benchmark-protocol-demo --json | benchmark protocol brief with route, minimum evidence, limitations, and package status | Does not prove benchmark superiority. |
| Scientific Public Data Triage Demo | scientific_public_data_triage | sovryn route plan --target scientific-public-data-triage-demo --json && sovryn route package --json | public-data triage package with route, evidence status, and limitations | Does not make real-world scientific validation claims. |
