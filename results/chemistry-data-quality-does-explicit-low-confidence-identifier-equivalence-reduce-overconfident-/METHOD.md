# Method

- Study: chemistry-data-quality-does-explicit-low-confidence-identifier-equivalence-reduce-overconfident-
- Baseline: unit-normalization-only conflict detector
- Metrics: true positives, false positives, true negatives, false negatives, precision, recall, false positive rate, false negative rate
- Instruments: unit-normalization-baseline, unit-provenance-chemistry-detector, chemistry-experiment-runner
- External packages: node
- Worker profile: container-netoff
- No silent fallback: true

## Controls

- same seeded records for baseline and candidate detector
- same known inconsistency labels for both methods
- same limited equivalence map for all runs

## Safety Scope

This is safe computational science using synthetic or public non-sensitive data.
It excludes wet-lab protocols, hazardous chemistry, medical advice, exploit
development, raw logs, secrets, private configuration, and local paths.
