# Build-vs-Buy Report

Decision ID: lab-decision-54ce00600aef

## Selected Packages

- pint: Accepted as a scoped, policy-reviewable tool.
- rapidfuzz: Accepted as a scoped, policy-reviewable tool.

## Custom Instruments

- chemistry-property-record-auditor: Audit toy chemistry-style property records with limited identifier equivalence.
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
