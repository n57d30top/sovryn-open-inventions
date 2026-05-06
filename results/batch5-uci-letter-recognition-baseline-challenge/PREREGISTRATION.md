# Preregistration

## Research Question

Can the selected external target be executed or audited with public-safe evidence, concrete metrics, and honest handling of failures, losses, and rejected claims?

## Metrics

| Metric | Best baseline | Challenger |
| --- | ---: | ---: |
| precision | 0.253 | 0.217 |
| recall | 0.856 | 0.792 |
| specificity | 0.403 | 0.324 |
| accuracy | 0.49 | 0.413 |
| f1 | 0.391 | 0.34 |
| balanced accuracy | 0.63 | 0.558 |

## Kill Criteria

- Reject a challenger when a simple baseline dominates it on preregistered holdout metrics.
- Do not claim full reproduction when only a bounded environment or partial dependency matrix was executed.
- Do not claim benchmark improvement without wins over the stated baseline.
- Publish negative or partial outcomes when they are scientifically useful and public hygiene passes.
