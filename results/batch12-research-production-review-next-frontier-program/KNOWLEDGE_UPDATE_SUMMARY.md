# Knowledge Update Summary

Promoted domains: benchmark metric validation, scientific dataset reliability.

Narrowed domains: time-series anomaly benchmarks, package install/test reproduction.

Deprioritized domains: source/evidence extraction, claim verification / evidence datasets.

Promoted tools: metric_stress_validator, container_netoff_replay_recipe, reproduction_ladder_artifact_pack.

Downgraded or narrowed tool uses: schema_provenance_auditor, pytest_repro_summary, single_table_schema_discovery_use.

Next claims to test:

- Source-described protocols can change conclusions relative to ordinary random splits.
- `metric_stress_validator` remains useful when paired with official split checks.
- `schema_provenance_auditor` is more useful on split-file or protocol-bearing datasets than on one clean CSV.
- Runtime pytest evidence can make repo/test reproduction promotable later, but static summaries alone cannot.
