# Dataset Audit Demo

- Input: A safe public dataset metadata page and small sample artifact.
- Command: `sovryn route plan --target dataset-audit-demo --json && sovryn route execute --target dataset-audit-demo --json`
- Expected package: dataset audit package with evidence checks and failure modes
- Interpretation: Use the output to identify missing metadata, quality caveats, and reproducibility blockers.
- Limitations: Does not validate domain-specific scientific conclusions.
