# Experiment Design

- Experiment: sci-exp-1d5365f2097d
- Baseline: simple threshold baseline over energy usage residuals
- Worker profile: container-netoff

## Success criteria

- candidate false-positive rate is lower than baseline on weather-related normal high-usage cases
- candidate recall does not drop by more than 0.05 compared with baseline
- result remains stable across at least three seeded replications

## Failure criteria

- baseline has equal or lower false-positive rate with comparable recall
- candidate fails on normal high-usage weather cases
- candidate relies on unsupported causal or production-readiness claims
