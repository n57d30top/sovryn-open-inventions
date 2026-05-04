# Energy Usage Anomaly Auditor

Sovryn produces autonomous open-research artifacts, defensive publications, and open-source research evidence. It is not a patent filing system and does not provide legal patentability, legal novelty, or freedom-to-operate opinions.

## Problem Statement

Public-safe energy-style records can contain duplicate timestamps, missing intervals, high-usage spikes, weather-normalization mismatches, and weak provenance. This result focuses on reproducible data-quality checks for toy or public aggregate records.

## Method

The method normalizes timestamps, groups anonymized meter records, builds seasonal/weather-aware baselines, flags missing intervals and duplicate records, and produces a bounded anomaly score.

## Custom Tool

energy-record-auditor

The curated result uses the recorded tool evidence and package evidence to keep
the method reproducible. External package/tool evidence: pandas.

## What This Catches

- Duplicate timestamp records for an anonymized toy meter.
- Missing hourly or daily intervals in public-safe time-series data.
- Usage spikes that remain unusual after a seasonal/weather baseline.
- Weak provenance sources that reduce reliability scoring.

## What This Does Not Catch

- It does not use private smart-meter records or identify real households.
- It does not optimize energy trading or surveillance decisions.
- It is a bounded anomaly-audit method, not a production forecasting system.

## Tests

The result keeps prototype and test evidence in the curated release package.
The tests are meant to demonstrate the method on bounded public-safe examples,
not to prove production readiness.

## Source Evidence Summary

The public corpus entry is backed by source-card, claim/feature, counter-evidence,
worker, replay, quality, safety, and public-hygiene summaries. Query links,
adapter failures, and placeholders are not treated as reviewed prior art.

## Counter-Evidence And Limitations

- "disclaimer": "This is an autonomous open-research artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion. It was published automatically after automated policy gates and still requires human interpretation before use.",
- README_CLAIMS_GROUNDED: passed (warn). README and public docs should ground claims in evidence, tests, and limitations.
- Expected behavior: not anomalous after baseline normalization
- This is an independent falsification and review artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion.
- This is an autonomous open-research artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion. It was published automatically after automated policy gates and still requires human interpretation before use.
- "expectedBehavior": "not anomalous after baseline normalization",

## How To Reproduce

See [REPRODUCE.md](REPRODUCE.md). The reproduction path uses only public
curated artifacts and does not require private Sovryn state.

## Autopublish Record

See [AUTOPUBLISH_RECORD.json](AUTOPUBLISH_RECORD.json). This result was
published automatically after automated gates. Human interpretation is still
required before operational use.

## Safety Scope

This is a bounded open-source research artifact. It is not a legal filing, not
a legal novelty opinion, and not operational advice for unsafe activity.
