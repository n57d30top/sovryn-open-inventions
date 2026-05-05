# Build-vs-Buy Report

Decision ID: lab-decision-3cd3b4d8af3d

## Selected Packages

- jsonschema: Accepted as a scoped, policy-reviewable tool.
- pandas: Accepted as a scoped, policy-reviewable tool.
- python-dateutil: Accepted as a scoped, policy-reviewable tool.
- rapidfuzz: Accepted as a scoped, policy-reviewable tool.

## Custom Instruments

- schema-drift-detector: Detect safe public metadata schema drift across dataset versions.
- provenance-quality-scorer: Score public dataset metadata provenance strength.
- dataset-record-auditor: Audit duplicate, missing, malformed, and weak-provenance dataset records.
- baseline-schema-validator: Provide the schema-only validation baseline.
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
