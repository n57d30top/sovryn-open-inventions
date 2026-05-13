# Reproduce

Re-run the bounded product commands, then inspect the package-local claim-evidence bindings and the generator-fund-closure ledgers.

## Candidate

DISCOVERY-INSIGHT-HARD-GEN-GAIA-ASTROMETRIC-EXCESS-SIGNIFICANCE-GE-0F9E75E

## Replay

Replay refs are bound in the package-local claim-evidence bindings and reproduce instructions.

## Commands

- npm run build
- npm test
- node dist/cli.js discover-daemon generator-fund-closure --json
- node dist/cli.js discover-daemon audit --json
