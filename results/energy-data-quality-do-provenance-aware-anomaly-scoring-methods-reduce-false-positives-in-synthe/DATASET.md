# Dataset

- Study: energy-data-quality-do-provenance-aware-anomaly-scoring-methods-reduce-false-positives-in-synthe
- Dataset kind: synthetic_energy_usage
- Dataset count: 3
- Seeds: 1, 2, 3
- Privacy scope: Synthetic toy records only; no private meter data, household identity, surveillance use case, or personal data publication.

## Schema

- recordId
- meterId
- timestamp
- season
- outdoorTempC
- kwh
- provenance
- expectedAnomaly
- expectedQualityIssues

## Required Patterns

- normal seasonal usage
- weather-related high usage that should not be a false positive
- missing intervals
- duplicate records
- weak-provenance records
- true anomaly spikes
- provenance labels

## Limitations

- Synthetic data may encode cleaner labels than real energy datasets.
- Weather normalization is represented by bounded toy temperature cases.
- Later phases must test public non-sensitive datasets before broader claims.
