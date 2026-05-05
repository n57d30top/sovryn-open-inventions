# Lab Needs Report

Needs ID: lab-needs-b1200a1e4766

## Research Goal

Test whether unit normalization plus provenance scoring improves inconsistent record detection compared with unit normalization alone.

## Required Measurements

- unit-normalized property conflict rate
- duplicate molecular record groups
- provenance confidence
- outlier flags

## Data Operations

- schema validation
- temperature unit normalization
- limited identifier equivalence grouping
- duplicate detection

## Analysis Operations

- baseline comparison
- candidate method scoring
- statistical analysis
- ablation analysis
- sensitivity analysis
- replication analysis
- falsification case evaluation
- chemistry-data-quality limitation review

## Candidate Packages

- pint: Normalize temperature units with a narrow, policy-reviewed package.
- rapidfuzz: Support fuzzy name/provenance matching with custom fallback.
- graphviz: Render optional pipeline DAG summaries when available.

## Candidate Instruments

- chemistry-property-record-auditor: Audit toy chemistry-style property records with limited identifier equivalence.
- baseline-comparator: Compare baseline and candidate metric outputs.
- replication-runner: Repeat deterministic experiment cases across seeds.
- falsification-case-generator: Generate safe negative and counterexample cases.

## Safety Scope

Safe computational science only. Blocked capabilities: none.

## Limitations

- This inference does not install packages or build tools.
- Candidate tool versions remain unknown until provisioning.
- Build-vs-buy hints are conservative and require a separate decision step.
