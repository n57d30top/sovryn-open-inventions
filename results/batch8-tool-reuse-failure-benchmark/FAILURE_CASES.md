# Failure Cases

- bike-sharing-day-hour: schema_match=False; rows=18110; hour file adds an hr column, so split-schema equality is not a valid assumption
- pyproject-hooks-pytest: ast_tests=32; grep_tests=32; runtime_errors=6; return_code=2

These failures are preserved as evidence and are not backfilled as success claims.
