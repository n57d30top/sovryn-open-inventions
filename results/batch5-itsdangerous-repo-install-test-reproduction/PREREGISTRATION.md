# Preregistration

## Research Question

Can the selected external target be executed or audited with public-safe evidence, concrete metrics, and honest handling of failures, losses, and rejected claims?

## Metrics

| Metric | Value |
| --- | ---: |
| tests passed | 297 |
| tests failed | 0 |
| examples passed | 1 |
| examples failed | 0 |
| pytest exit code | 0 |
| package version | 2.3.0.dev0 |

## Kill Criteria

- Reject a challenger when a simple baseline dominates it on preregistered holdout metrics.
- Do not claim full reproduction when only a bounded environment or partial dependency matrix was executed.
- Do not claim benchmark improvement without wins over the stated baseline.
- Publish negative or partial outcomes when they are scientifically useful and public hygiene passes.
