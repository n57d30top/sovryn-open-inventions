# Tool Use Constraints

| Tool | Batch 13 role | Decision |
| --- | --- | --- |
| `metric_stress_validator` | Shuffled-label, macro-vs-accuracy, class-risk, and seed/split stress support. | Keep as reusable support tool; do not use it to claim protocol correctness or leakage absence. |
| `schema_provenance_auditor` | Source-hash binding, schema cards, missingness/duplicate packaging, protocol metadata. | Keep as packaging-only for these targets; pandas explained raw findings. |
| `container_netoff_replay_recipe` | Replay after public data provisioning with external network disabled. | Keep as reusable replay recipe for protocol validation batches. |

No new framework layer, CLI group, generic service, or standalone repository was created.
