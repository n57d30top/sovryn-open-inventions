# Preregistration

Research question: Can a public dataset-quality audit catch quality risks in UCI Wine Quality beyond a schema-only baseline?

## Metrics
- rows audited
- columns audited
- missing cells
- duplicate rows
- duplicate rate
- majority quality share
- rare extreme-quality rows
- schema-only issue recall
- schema+distribution issue recall

## Baselines / challengers
- schema-only audit
- schema+distribution audit

## Kill criteria
- Reject improvement if it does not beat or materially extend the baseline under the preregistered metric.
- Reject or downgrade any claim with unrecorded losses, unsupported source binding, or public-hygiene risk.
- Treat negative results as valid outputs.
