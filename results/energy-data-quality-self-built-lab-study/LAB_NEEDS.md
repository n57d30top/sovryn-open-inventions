# Lab Needs Report

Needs ID: lab-needs-dbb64be66c05

## Research Goal

Test whether provenance-aware anomaly scoring reduces false positives compared with simple threshold baselines.

## Required Measurements

- false-positive rate
- false-negative rate
- weather-normalized anomaly score
- provenance confidence

## Data Operations

- timestamp parsing
- season/weather feature extraction
- missing interval detection
- duplicate record detection

## Analysis Operations

- baseline comparison
- candidate method scoring
- statistical analysis
- ablation analysis
- sensitivity analysis
- replication analysis
- falsification case evaluation
- energy-data-quality limitation review

## Candidate Packages

- pandas: Handle small tabular fixture datasets in isolated provisioning.
- python-dateutil: Parse deterministic timestamp fixtures.
- numpy: Support deterministic numeric summary calculations.
- graphviz: Render optional pipeline DAG summaries when available.

## Candidate Instruments

- provenance-aware-energy-detector: Detect energy anomalies while reducing weather-related false positives.
- baseline-comparator: Compare baseline and candidate metric outputs.
- replication-runner: Repeat deterministic experiment cases across seeds.
- falsification-case-generator: Generate safe negative and counterexample cases.

## Safety Scope

Safe computational science only. Blocked capabilities: none.

## Limitations

- This inference does not install packages or build tools.
- Candidate tool versions remain unknown until provisioning.
- Build-vs-buy hints are conservative and require a separate decision step.
