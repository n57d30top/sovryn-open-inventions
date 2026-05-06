# Tool Use Constraints

| Tool | Batch 14 role | Decision |
| --- | --- | --- |
| `metric_stress_validator` | Shuffled-label, macro-vs-accuracy, class-risk, seed/split sensitivity, and severity support. | Keep as reusable support tool; do not use it to prove protocol correctness or leakage absence. |
| `schema_provenance_auditor` | Source hash binding, schema cards, missingness/duplicate checks, protocol metadata. | Keep as packaging-only for these targets. |
| `container_netoff_replay_recipe` | Replay after public data provisioning with external network disabled. | Keep as reusable replay recipe; do not silently fall back to host execution. |

No new framework layer, CLI group, generic service, or standalone repository was created.
