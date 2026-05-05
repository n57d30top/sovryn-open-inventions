# Examples

- Study: software-supply-chain-assurance-do-dependency-provenance-features-improve-risk-scoring-for-synth
- Question: Do dependency-provenance features improve risk scoring for synthetic AI-generated pull requests compared with diff-pattern-only baselines?

## Caught Cases

- Normal high usage driven by cold weather should not be classified as a true anomaly.: Observed behavior matched the expected safe synthetic outcome in the current bounded study.
- Weak provenance alone should create a quality note, not an anomaly, when the value is normal.: Observed behavior matched the expected safe synthetic outcome in the current bounded study.
- A true anomaly with trusted provenance should still be detected.: Observed behavior matched the expected safe synthetic outcome in the current bounded study.
- A missing interval should be reported independently from anomaly scoring.: Observed behavior matched the expected safe synthetic outcome in the current bounded study.
- If the simple baseline has lower false-positive rate and equal recall, the hypothesis should be weakened or rejected.: No baseline-win counterexample was observed in the current deterministic seed set; this remains a required future challenge case.

## Not Caught / Limited Cases

- The study remains bounded by deterministic synthetic/proxy data.
