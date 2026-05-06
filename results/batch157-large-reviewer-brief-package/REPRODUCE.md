# Reproduce

1. Build and test the product.
2. Run `sovryn review receipts verify --json`.
3. Inspect `SUMMARY.json` and `BATCH_REPORT.md`.
4. For execution batches, use the public source URLs listed in `PUBLIC_RECEIPT_SUMMARIES.json`; private receipts remain in the product evidence store and public files contain redacted summaries only.
