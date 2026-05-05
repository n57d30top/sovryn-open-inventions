# Falsification

Hypothesis impact: partially_supported
Material failures: 0

Sovryn attempted to weaken the hypothesis with safe synthetic counterexamples. This is not proof of general truth.

| Case | Passed | Material failure |
| --- | --- | --- |
| consistent-unit-conversion | true | false |
| weak-provenance-normal-value | true | false |
| acetone-outlier-conflict | true | false |
| unknown-identifier-low-confidence | true | false |

## Failure Cases

No material failure cases were observed in this bounded synthetic run.

## Limitations

- Falsification uses safe synthetic molecular-property records only.
- The tool does not perform general SMILES canonicalization or chemistry inference.
- Future work should compare against policy-approved RDKit/OpenBabel integration.
