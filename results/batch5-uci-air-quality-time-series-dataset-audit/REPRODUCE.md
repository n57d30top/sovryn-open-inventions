# Reproduce

1. Fetch the public UCI Air Quality ZIP archive.
2. Extract the semicolon-delimited CSV.
3. Parse decimal-comma numeric fields and preserve Date/Time keys.
4. Execute the audit script in a network-disabled container.
5. Count -200 sentinel values by numeric column.
6. Compare the schema-only detector against the sentinel-aware detector and publish aggregate metrics only.

Expected aggregate result label: dataset_quality_audit_supported.
