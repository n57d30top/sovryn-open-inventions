# Demo Script

1. Claim Review Demo: run `sovryn route intake --target claim-review-demo --json && sovryn route execute --target claim-review-demo --json` and inspect the generated claim decision package with evidence route, limitations, and reproduce note.
2. Tool Usefulness Demo: run `sovryn route plan --target tool-usefulness-demo --json && sovryn route execute --target tool-usefulness-demo --json` and inspect the generated tool usefulness brief with static scan, route decision, and caveats.
3. Dataset Audit Demo: run `sovryn route plan --target dataset-audit-demo --json && sovryn route execute --target dataset-audit-demo --json` and inspect the generated dataset audit package with evidence checks and failure modes.
4. Benchmark Protocol Audit Demo: run `sovryn route classify --target benchmark-protocol-demo --json && sovryn route execute --target benchmark-protocol-demo --json` and inspect the generated benchmark protocol brief with route, minimum evidence, limitations, and package status.
5. Scientific Public Data Triage Demo: run `sovryn route plan --target scientific-public-data-triage-demo --json && sovryn route package --json` and inspect the generated public-data triage package with route, evidence status, and limitations.
