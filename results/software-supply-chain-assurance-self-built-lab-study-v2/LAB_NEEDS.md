# Lab Needs Report

Needs ID: lab-needs-486b778122cc

## Research Goal

Test whether dependency provenance plus test-impact signals improves detection of risky synthetic AI-generated patches compared with diff-pattern-only baselines.

## Required Measurements

- dependency-change risk
- install-script risk
- test-impact mismatch
- patch provenance weakness

## Data Operations

- toy repository metadata ingestion
- dependency manifest parsing
- synthetic diff parsing
- test-impact feature extraction

## Analysis Operations

- baseline comparison
- candidate method scoring
- statistical analysis
- ablation analysis
- sensitivity analysis
- replication analysis
- falsification case evaluation
- software-supply-chain-assurance limitation review

## Candidate Packages

- simple-git: Read safe toy repository metadata without exploit execution.
- acorn: Parse JavaScript/package metadata in a bounded defensive analyzer.
- graphviz: Render optional pipeline DAG summaries when available.

## Candidate Instruments

- patch-risk-auditor-lite: Score safe synthetic patch-risk examples without exploit generation.
- baseline-comparator: Compare baseline and candidate metric outputs.
- replication-runner: Repeat deterministic experiment cases across seeds.
- falsification-case-generator: Generate safe negative and counterexample cases.

## Safety Scope

Safe computational science only. Blocked capabilities: none.

## Limitations

- This inference does not install packages or build tools.
- Candidate tool versions remain unknown until provisioning.
- Build-vs-buy hints are conservative and require a separate decision step.
