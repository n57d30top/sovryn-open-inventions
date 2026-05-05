# Build-vs-Buy Report

Decision ID: lab-decision-73c29a88a585

## Selected Packages

- pandas: Accepted as a scoped, policy-reviewable tool.
- python-dateutil: Accepted as a scoped, policy-reviewable tool.
- numpy: Accepted as a scoped, policy-reviewable tool.

## Custom Instruments

- provenance-aware-energy-detector: Detect energy anomalies while reducing weather-related false positives.
- baseline-comparator: Compare baseline and candidate metric outputs.
- replication-runner: Repeat deterministic experiment cases across seeds.
- falsification-case-generator: Generate safe negative and counterexample cases.

## Fallback Plan

- If package provisioning fails, use the scoped custom fallback and mark capability degraded.
- If container-netoff is unavailable, stop final validation or record explicit degraded status.

## Limitations

- This decision does not provision packages.
- Unknown package license or version metadata lowers confidence until provisioning evidence exists.
- Custom instruments remain scoped to safe fixture/data-quality use unless extended later.
