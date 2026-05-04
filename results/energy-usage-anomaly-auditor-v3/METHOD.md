# Method: Energy Usage Anomaly Auditor

## Tool Architecture

Custom tool: energy-record-auditor

External package/tool evidence: pandas

Worker assurance: container-netoff

```mermaid
flowchart LR
  A[Public-safe input records] --> B[energy-record-auditor]
  B --> C[Detected issues]
  C --> D[Prototype tests]
  D --> E[Replay and public hygiene checks]
  E --> F[Curated corpus result]
```

## Evidence Flow

The showcase result is selected only after quality, evidence, reproducibility,
publication safety, replay, safety scan, public hygiene, and anti-template gates
are represented in the public corpus metadata.

## Verification Method

Verification uses toy time-series records with known missing intervals, duplicates, weather-normalized anomalies, and weak provenance.

## Source Evidence Summary

Source-card and claim/feature summaries are public evidence pointers. They are
not legal novelty conclusions and they do not replace human review.
