# Preregistration

Research question: Does a rolling-MAD candidate beat simple baselines on a public NAB labeled anomaly file?

## Metrics
- rows evaluated
- label windows
- labeled points
- global z-score precision
- global z-score recall
- rolling MAD precision
- rolling MAD recall
- derivative challenger precision
- candidate rejected

## Baselines / challengers
- global_zscore_3sigma
- rolling_mad_4sigma_candidate
- derivative_zscore_challenger

## Kill criteria
- Reject improvement if it does not beat or materially extend the baseline under the preregistered metric.
- Reject or downgrade any claim with unrecorded losses, unsupported source binding, or public-hygiene risk.
- Treat negative results as valid outputs.
