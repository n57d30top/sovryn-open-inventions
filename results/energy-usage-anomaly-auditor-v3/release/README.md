# Energy Usage Anomaly Auditor

A safe open-source data-quality method for auditing anonymized toy home-energy usage records.

The `energy-record-auditor` prototype checks synthetic toy records for duplicate
timestamps, missing intervals, high-usage spikes, weather-normalized anomalies,
and weak provenance. It provisioned or fixture-provisioned `pandas` under
policy and validated the public evidence through Node Alpha using
`container-netoff` with no silent fallback.

## Issues Detected

- duplicate_timestamp: Duplicate timestamp for anonymized toy household.
- high_usage_spike: Usage is high relative to seasonal/weather-normalized expectation.
- high_usage_spike: Usage is high relative to seasonal/weather-normalized expectation.
- missing_interval: Missing 1 daily interval(s) before 2026-01-05T00:00:00Z.
- weak_provenance: Record source is weak or unknown.
- weather_normalized_anomaly: Warm-weather record has unusually high usage for the toy baseline.

## Safety Scope

No private smart-meter data is used. This is not a surveillance system, not an energy-market trading system, and not a personal-data publication workflow.

## Disclaimer

This is an autonomous open-research artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion. It was published automatically after automated policy gates and still requires human interpretation before use.
