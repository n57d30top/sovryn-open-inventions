# Lab Needs Report

Needs ID: lab-needs-18b7225ca0b9

## Research Goal

Test whether provenance-aware schema-drift checks improve detection of unreliable public scientific dataset records compared with schema-only validation baselines.

## Required Measurements

- schema drift count
- metadata provenance confidence
- duplicate dataset record groups
- missingness and unit metadata consistency

## Data Operations

- public metadata ingestion
- schema version comparison
- provenance label validation
- duplicate dataset-record detection

## Analysis Operations

- baseline comparison
- candidate method scoring
- statistical analysis
- ablation analysis
- sensitivity analysis
- replication analysis
- falsification case evaluation
- scientific-dataset-reliability limitation review

## Candidate Packages

- jsonschema: Validate public-safe dataset metadata records against explicit schemas.
- pandas: Handle small public metadata/proxy tabular datasets.
- python-dateutil: Parse dataset version timestamps deterministically.
- rapidfuzz: Support fuzzy metadata title/provenance matching.
- graphviz: Render optional pipeline DAG summaries when available.

## Candidate Instruments

- schema-drift-detector: Detect safe public metadata schema drift across dataset versions.
- provenance-quality-scorer: Score public dataset metadata provenance strength.
- dataset-record-auditor: Audit duplicate, missing, malformed, and weak-provenance dataset records.
- baseline-schema-validator: Provide the schema-only validation baseline.
- baseline-comparator: Compare baseline and candidate metric outputs.
- replication-runner: Repeat deterministic experiment cases across seeds.
- falsification-case-generator: Generate safe negative and counterexample cases.

## Safety Scope

Safe computational science only. Blocked capabilities: none.

## Limitations

- This inference does not install packages or build tools.
- Candidate tool versions remain unknown until provisioning.
- Build-vs-buy hints are conservative and require a separate decision step.
