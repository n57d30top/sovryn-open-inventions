# Reproduce

1. Create an isolated Python environment.
2. Install pytest 9.0.1.
3. Clone pytest-dev/pluggy and check out commit a469596df2c9f7f9d5219b85c764c644b81896f7.
4. Install the checkout in editable mode.
5. Run pytest_repro_summary with the testing target enabled.

Expected output is a curated JSON measurement summary with the metrics reported in SUMMARY.json.
