# Examples

- Study: chemistry-data-quality-does-explicit-low-confidence-identifier-equivalence-reduce-overconfident-
- Question: Does explicit low-confidence identifier equivalence reduce overconfident chemistry-style record audits when unit-normalized values agree?

## Caught Cases

- Consistent Celsius/Kelvin pairs should not be treated as property conflicts.: Observed behavior matched the expected safe synthetic outcome in the bounded toy chemistry study.
- Weak provenance alone should create a quality note, not a chemical-property conflict.: Observed behavior matched the expected safe synthetic outcome in the bounded toy chemistry study.
- A large acetone boiling-point conflict should still be flagged after unit normalization.: Observed behavior matched the expected safe synthetic outcome in the bounded toy chemistry study.
- Unknown identifier equivalence should remain low confidence rather than becoming canonical.: Observed behavior matched the expected safe synthetic outcome in the bounded toy chemistry study.

## Not Caught / Limited Cases

- The study remains bounded by deterministic synthetic/proxy data.
