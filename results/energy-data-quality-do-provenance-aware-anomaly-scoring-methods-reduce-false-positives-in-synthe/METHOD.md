# Method

- Study: energy-data-quality-do-provenance-aware-anomaly-scoring-methods-reduce-false-positives-in-synthe
- Baseline: simple threshold baseline over energy usage residuals
- Metrics: true positives, false positives, true negatives, false negatives, precision, recall, false positive rate, false negative rate
- Instruments: threshold-baseline-detector, provenance-aware-energy-detector, experiment-runner
- External packages: node
- Worker profile: container-netoff
- No silent fallback: true

## Controls

- same seeded datasets for baseline and candidate detector
- same anomaly labels for both methods
- same threshold sweep for sensitivity analysis

## Safety Scope

This is safe computational science using synthetic or public non-sensitive data.
It excludes wet-lab protocols, hazardous chemistry, medical advice, exploit
development, raw logs, secrets, private configuration, and local paths.
