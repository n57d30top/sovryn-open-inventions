# Reproduction Preregistration

Research question: Can a targeted provenance-aware extension improve public scientific claim/evidence extraction over the selected external benchmark baseline without increasing false positives?

## Metrics
- macro_f1
- evidence_binding_precision
- evidence_binding_recall
- false_positive_rate
- calibration_error

## Baselines
- original-scifact-abstract-retrieval-baseline
- bm25-claim-to-abstract-baseline
- tfidf-logistic-evidence-baseline
- keyword-overlap-evidence-baseline
- source-metadata-prior-baseline
- majority-label-control-baseline

## Kill Criteria
- Reject improvement if it fails to beat reproduced baseline on preregistered primary metrics.
- Reject improvement if holdout gains disappear under ablation or sensitivity tests.
- Reject improvement if independent rebuild diverges beyond tolerance.
