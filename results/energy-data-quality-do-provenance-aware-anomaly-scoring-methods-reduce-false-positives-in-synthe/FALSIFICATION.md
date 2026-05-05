# Falsification

Hypothesis impact: partially_supported
Material failures: 0

Sovryn attempted to weaken the hypothesis with safe synthetic counterexamples. This is not proof of general truth.

| Case | Passed | Material failure |
| --- | --- | --- |
| normal-cold-weather-high-usage | true | false |
| weak-provenance-normal-value | true | false |
| strong-provenance-true-spike | true | false |
| missing-interval-independent | true | false |
| baseline-win-counterexample | true | false |

## Failure Cases

No material failure cases were observed in this bounded synthetic run.

## Limitations

- Falsification uses safe synthetic counterexamples only.
- No real household, infrastructure, or private meter data is used.
- Future work should add public non-sensitive datasets and independent adversarial cases.
