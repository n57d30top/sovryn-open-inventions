# Batch 7 Tool-Building Under Pressure Report

Batch 7 produced three public external research results. Each result used a small custom tool built only because the target needed a specific evidence operation that generic tools did not cover cleanly.

- batch7-wine-quality-schema-provenance-tool: `schema_provenance_auditor` on UCI Wine Quality red and white CSV datasets; status `used_successfully`; learned: The red and white Wine Quality files share the expected 12-column schema and have no missing cells, but they contain 1177 duplicate full rows across the combined public files. That makes this a useful negative data-quality finding for downstream benchmark use.
- batch7-banknote-metric-stress-validator: `metric_stress_validator` on UCI Banknote Authentication classification dataset; status `used_successfully_limited`; learned: The metric validator is useful for comparing a challenger against dummy and shuffled-label controls, but it is explicitly limited because one deterministic split cannot certify an official benchmark protocol or prove absence of leakage.
- batch7-pluggy-pytest-repro-summary-tool: `pytest_repro_summary` on pytest-dev/pluggy repository test suite; status `used_successfully_limited`; learned: The summarizer can create a public-safe reconciliation between static inventory and execution counts, but it must be marked limited because dynamic parametrization means static definitions do not equal runtime cases.

No framework layer, CLI group, generic service, or standalone repository was added.
