# Reproduce

1. Create an isolated Python environment.
2. Install pandas 3.0.2 and scikit-learn 1.8.0.
3. Download the UCI Banknote Authentication text dataset listed in SOURCE_CARD.md.
4. Run metric_stress_validator with target column index -1 and random_state=7.

Expected output is a curated JSON measurement summary with the metrics reported in SUMMARY.json.
