# Preregistration

## Research Question

Can the selected external target be executed or audited with public-safe evidence, concrete metrics, and honest handling of failures, losses, and rejected claims?

## Metrics

| Metric | Schema-only baseline | Sentinel-aware challenger |
| --- | ---: | ---: |
| true positives | 0 | 4 |
| false positives | 0 | 0 |
| true negatives | 9 | 9 |
| false negatives | 4 | 0 |
| precision | 0 | 1 |
| recall | 0 | 1 |
| f1 | 0 | 1 |

## Kill Criteria

- Reject a challenger when a simple baseline dominates it on preregistered holdout metrics.
- Do not claim full reproduction when only a bounded environment or partial dependency matrix was executed.
- Do not claim benchmark improvement without wins over the stated baseline.
- Publish negative or partial outcomes when they are scientifically useful and public hygiene passes.
