# Preregistration

Research question: Can provenance-aware source/evidence extraction quality checks improve detection of unreliable public computational-science evidence records compared with external baseline extractors?

## Metrics
- false_positive_rate
- balanced_accuracy
- macro_f1
- calibration_error
- evidence_binding_precision

## Baselines
- keyword-overlap-baseline
- regex-section-extractor-baseline
- bm25-style-term-baseline
- schema-only-validator-baseline
- tfidf-logistic-lightweight-baseline
- source-type-prior-baseline

## Kill Criteria
- Reject candidates dominated by any strong baseline across more than one task.
- Reject candidates that degrade false-positive rate by more than 5 percent relative to the tuned statistical baseline.
- Reject candidates with ambiguous method specifications after independent rebuild.
