# Reproduce

Re-run the bounded product commands and inspect the package-local claim-evidence bindings.

## Replay

- .sovryn/discovery-daemon/evidence-packages/DISCOVERY-INSIGHT-HARD-GEN-MATBENCH-DESCRIPTOR-TRANSFER-SIGNIFICAN-74933C4/CLAIM_EVIDENCE_BINDINGS.json#replayEvidenceRefs
- .sovryn/discovery-daemon/evidence-packages/DISCOVERY-INSIGHT-HARD-GEN-MATBENCH-DESCRIPTOR-TRANSFER-SIGNIFICAN-74933C4/REPRODUCE.md#replay
- .sovryn/discovery-daemon/generator-insight-closure/INSIGHT-HARD-GEN-MATBENCH-DESCRIPTOR-TRANSFER-SIGNIFICAN-74933C45D6DB.json#replay_feasibility_test
- https://matbench.materialsproject.org/#replay

## Commands

- npm run build
- npm test
- node dist/cli.js discover-daemon generator-fund-closure --json
- node dist/cli.js discover-daemon generator-claim-lift-propose --json
- node dist/cli.js discover-daemon generator-claim-lift --json
