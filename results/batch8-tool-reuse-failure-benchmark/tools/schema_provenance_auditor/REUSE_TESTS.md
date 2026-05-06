# Reuse Tests

- student-performance-splits: schema_match=True; rows=1044; missing_cells=0; duplicate_full_rows=0
- bike-sharing-day-hour: schema_match=False; rows=18110; hour file adds an hr column, so split-schema equality is not a valid assumption
