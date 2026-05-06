# Data Schema Provenance Audit

Tool used: `schema_provenance_auditor`.

Findings:

- Rows: 13611
- Columns: 17
- Feature columns: 16
- Target column: `Class`
- Missing cells: 0
- Duplicate full rows: 68
- Duplicate feature rows: 68
- Suspicious sentinel counts: {'-1': 0, '0': 0, '999': 0, '9999': 0}
- Class distribution: {"BARBUNYA": 1322, "BOMBAY": 522, "CALI": 1630, "DERMASON": 3546, "HOROZ": 1928, "SEKER": 2027, "SIRA": 2636}

Manual/schema-only baseline:

A simple pandas baseline can report shape, null count, duplicate count, and class value counts. The custom tool adds a hash-bound schema/provenance evidence card and explicit duplicate/missing gates, but Batch 9 had to add target-column and UCI metadata context.

What the tool missed:

- It did not infer target semantics without the Batch 9 wrapper.
- It did not detect train/test leakage because the public dataset was loaded as a single table without an official split.
- It cannot decide whether duplicate feature rows are invalid observations without row-level provenance.

Decision update:

`schema_provenance_auditor` moves from `narrow_but_useful` to `reusable_for_single_table_tabular_benchmark_screening`, with the limitation that it still needs target-specific context.
