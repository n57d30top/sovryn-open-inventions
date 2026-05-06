# Reproduce

1. Create an isolated Python environment.
2. Install pandas 3.0.2.
3. Download the three UCI Wine Quality source files listed in SOURCE_CARD.md.
4. Run schema_provenance_auditor on red and white CSV files with semicolon delimiter.
5. Use a network-denied profile for the final local-data replay if available.

Expected output is a curated JSON measurement summary with the metrics reported in SUMMARY.json.
