# Preregistration

Research question: Can a source-card parser recover benchmark evidence fields from the QASPER public dataset card better than a title/abstract keyword baseline?

## Metrics
- expected source-card fields
- README length chars inspected
- expected fields present in source
- keyword baseline field recall
- source-card parser field recall
- official baseline Token F1 found

## Baselines / challengers
- title/abstract keyword baseline
- source-card parser

## Kill criteria
- Reject improvement if it does not beat or materially extend the baseline under the preregistered metric.
- Reject or downgrade any claim with unrecorded losses, unsupported source binding, or public-hygiene risk.
- Treat negative results as valid outputs.
