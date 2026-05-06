# Schema Provenance Attacks

Targets attacked:

- Batch 7 Wine Quality schema/provenance result.
- Batch 8 schema reuse on Student Performance and Bike Sharing.
- Batch 9 Dry Bean schema/provenance component.

Findings:

- Wine Quality duplicate and missingness findings are reproducible by ordinary pandas checks.
- Dry Bean duplicate and missingness findings are also reproducible by ordinary pandas checks.
- Batch 8 Bike Sharing remains an important failure case: related files can have intentionally different schemas, so schema equality must not be assumed.
- Dry Bean target-column and class-distribution reporting required Batch 9 wrapper context.

Decision:

`schema_provenance_auditor` is downgraded to `narrow_but_useful`.

Allowed future claim:

The tool is useful for evidence packaging, source hashes, schema comparison cards, and consistent public audit fields.

Forbidden future claim:

The tool uniquely discovers ordinary single-table shape, missingness, duplicate, or class-count facts that pandas cannot find.
