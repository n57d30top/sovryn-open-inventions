# Reproduce

- Study: energy-data-quality-do-provenance-aware-anomaly-scoring-methods-remain-stable-when-synthetic-ene
- Dataset kind: synthetic_energy_usage
- Seeds: 1, 2, 3
- Replication runs: 3
- Worker profile: container-netoff

## Reproduction Steps

1. Inspect the dataset and instrument reports in this result folder.
2. Re-run the deterministic fixture study with the recorded seeds.
3. Compare baseline, statistics, ablation, sensitivity, replication, and
   falsification reports.
4. Treat deviations as limitations unless the same data, same metrics, and same
   instrument version are used.
