# Baseline Reproduction

| Baseline | Evidence | Metric | Failure / limitation |
| --- | --- | --- | --- |
| README-only protocol parser | label/predicted_label/evidence | 0.75 recall | missed predicted_evidence formatting note |
| schema-aware parser | label/predicted_label/evidence/predicted_evidence | 1.00 recall | still no full dataset baseline run |

Baseline reproduction is bounded to public-safe data or source-card evidence. Missing full-scale reproduction is recorded as a limitation, not hidden.
