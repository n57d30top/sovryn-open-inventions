# Hypotheses

## sci-h-0afdcfbe02ec

A provenance-aware anomaly scoring method will reduce false positives on weather-related normal high-usage records compared with a simple threshold baseline.

- Null hypothesis: A provenance-aware anomaly scoring method will not reduce the false-positive rate compared with a simple threshold baseline on the same synthetic energy-usage records.
- Alternative hypothesis: Provenance-aware scoring reduces false positives while preserving materially similar recall for true anomaly spikes.
- Falsification criteria: The threshold baseline has equal or lower false-positive rate with comparable recall.; Normal high usage caused by weather is still flagged as anomalous by the candidate method.; Performance improvement disappears when provenance labels are noisy but non-adversarial.

## sci-h-11ecc976f5e8

Combining provenance scoring with missing-interval and duplicate-record checks will improve dataset-quality triage compared with anomaly scoring alone.

- Null hypothesis: Adding provenance, missing-interval, and duplicate-record checks will not improve dataset-quality triage compared with anomaly scoring alone.
- Alternative hypothesis: A combined detector better separates true anomalies, data-quality defects, and benign high-usage records than an anomaly-only baseline.
- Falsification criteria: Missing intervals or duplicate records are not detected reliably.; Weak provenance alone causes normal records to be falsely marked as anomalies.; An anomaly-only baseline produces equal or better triage labels under the same metrics.

