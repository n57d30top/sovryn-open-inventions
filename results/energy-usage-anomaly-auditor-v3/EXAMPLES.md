# Examples: Energy Usage Anomaly Auditor

## What This Catches

- Duplicate timestamp records for an anonymized toy meter.
- Missing hourly or daily intervals in public-safe time-series data.
- Usage spikes that remain unusual after a seasonal/weather baseline.
- Weak provenance sources that reduce reliability scoring.

## What This Should Not Overclaim

- It does not use private smart-meter records or identify real households.
- It does not optimize energy trading or surveillance decisions.
- It is a bounded anomaly-audit method, not a production forecasting system.

## Why This Is Useful

The result is useful because it shows how data-quality failures can be separated from normal seasonal or weather-driven variation.

These examples are bounded demonstrations for public research artifacts. They
are not claims of production coverage, legal novelty, or freedom-to-operate.
