# Examples

- Study: energy-data-quality-do-provenance-aware-anomaly-scoring-methods-reduce-false-positives-in-public
- Question: Do provenance-aware anomaly scoring methods reduce false positives in public-weather-proxy energy datasets compared with simple threshold baselines?

## Caught Cases

- Normal high usage driven by cold weather should not be classified as a true anomaly.: Observed behavior matched the expected safe synthetic outcome in the current bounded study.
- Weak provenance alone should create a quality note, not an anomaly, when the value is normal.: Observed behavior matched the expected safe synthetic outcome in the current bounded study.
- A true anomaly with trusted provenance should still be detected.: Observed behavior matched the expected safe synthetic outcome in the current bounded study.
- A missing interval should be reported independently from anomaly scoring.: Observed behavior matched the expected safe synthetic outcome in the current bounded study.
- If the simple baseline has lower false-positive rate and equal recall, the hypothesis should be weakened or rejected.: No baseline-win counterexample was observed in the current deterministic seed set; this remains a required future challenge case.

## Not Caught / Limited Cases

- Real/proxy data uses aggregateKwhIndex while synthetic controls use per-record kWh toy values.
- This comparison validates schema/provenance alignment, not a broad real-world performance claim.
