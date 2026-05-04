# Method: Molecular Record Auditor for Chemistry-Style Dataset Quality

## Tool Architecture

Custom tool: mol-record-auditor

External package/tool evidence: pint

Worker assurance: container-netoff

```mermaid
flowchart LR
  A[Public-safe input records] --> B[mol-record-auditor]
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

Verification uses toy public-safe molecular-property records with unit conversion, duplicate identifier, outlier, and malformed-record cases.

## Source Evidence Summary

Source-card and claim/feature summaries are public evidence pointers. They are
not legal novelty conclusions and they do not replace human review.
