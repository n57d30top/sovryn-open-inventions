# Reproduce

Re-run the bounded product commands and inspect the package-local claim-evidence bindings.

## Replay

- .sovryn/discovery-daemon/evidence-packages/DISCOVERY-INSIGHT-HARD-GEN-BOUNDED-GRAPH-MINOR-OBSTRUCTION-SIGNIFI-4E76B84/CLAIM_EVIDENCE_BINDINGS.json#replayEvidenceRefs
- .sovryn/discovery-daemon/evidence-packages/DISCOVERY-INSIGHT-HARD-GEN-BOUNDED-GRAPH-MINOR-OBSTRUCTION-SIGNIFI-4E76B84/REPRODUCE.md#replay
- .sovryn/discovery-daemon/generator-insight-closure/INSIGHT-HARD-GEN-BOUNDED-GRAPH-MINOR-OBSTRUCTION-SIGNIFI-4E76B8436316.json#replay_feasibility_test
- https://hog.grinvin.org/#replay

## Commands

- npm run build
- npm test
- node dist/cli.js discover-daemon generator-fund-closure --json
- node dist/cli.js discover-daemon generator-claim-lift-propose --json
- node dist/cli.js discover-daemon generator-claim-lift --json
