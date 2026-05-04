# Falsification: Energy Usage Anomaly Auditor

Evaluation label: passes_falsification
Score: 96

## Purpose

This report tries to weaken or falsify the public result before it remains a
showcase or reviewable corpus artifact.

## Checks

- PUBLIC_HYGIENE_PASSED: passed (block). Public hygiene must pass before falsification can accept a result.
- NO_OVERCLAIMS: passed (block). No overclaiming language found.
- NEGATIVE_TESTS_PRESENT: passed (warn). Domain-specific negative tests should exist.
- BENIGN_CASES_NOT_OVERFLAGGED: passed (warn). Falsification should include benign cases that should not be overflagged.
- ADVERSARIAL_SAFE_CASES_FLAGGED: passed (warn). Falsification should include safe synthetic cases that should be flagged.
- README_CLAIMS_GROUNDED: passed (warn). README and public docs should ground claims in evidence, tests, and limitations.
- QUALITY_NOT_WEAK: passed (block). Weak quality labels cannot pass falsification.

## Negative Tests

### seasonal-normal-high-use

- Purpose: Seasonal normal high usage should not be flagged as anomalous when weather explains it.
- Input case: synthetic winter usage with low temperature and expected heating load
- Expected behavior: not anomalous after baseline normalization
- Falsification target: false-positive risk
- Safe synthetic only: true

### missing-interval

- Purpose: Missing interval should be detected.
- Input case: synthetic hourly sequence skips one interval
- Expected behavior: missing interval flag
- Falsification target: false-negative risk
- Safe synthetic only: true

### duplicate-record

- Purpose: Duplicate timestamp should be detected.
- Input case: two records share anonymized meter and timestamp
- Expected behavior: duplicate flag
- Falsification target: data integrity risk
- Safe synthetic only: true

### weather-normalized-anomaly

- Purpose: Usage spike unexplained by weather should be detected.
- Input case: synthetic mild-weather record has extreme usage
- Expected behavior: weather-normalized anomaly flag
- Falsification target: false-negative risk
- Safe synthetic only: true


## Overclaim Findings

No blocking overclaim findings.

## Recommended Action

Keep as reviewable public corpus evidence; continue human interpretation before use.

This is an independent falsification and review artifact. It is not a patent filing, patentability opinion, legal novelty opinion, or freedom-to-operate opinion.
