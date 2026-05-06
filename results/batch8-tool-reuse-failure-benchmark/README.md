# Batch 8 Tool Reuse and Failure Benchmark

Batch 8 reused the three custom tools created in Batch 7 across six new external public-safe targets.

The point was not to produce isolated results. The point was to test whether prior tools generalized, failed, needed narrowing, or should guide the next research direction.

## Result

- `metric_stress_validator` is reusable across two classification datasets, with explicit error-rate caveats.
- `schema_provenance_auditor` is narrow but useful: it works on comparable split files and correctly exposes non-comparable split schemas.
- `pytest_repro_summary` is narrow but useful: it summarizes static and runtime test evidence, but repository dependency failures must be treated as first-class outcomes.

## What changed from Batch 7

Batch 7 built tools under pressure. Batch 8 tested whether those tools survived contact with new targets.

The answer is mixed and useful: one tool is promoted, two are narrowed, and two failure cases are documented.

## Next direction

Promote dataset and metric validation as the next deep toolchain direction, while keeping repo test summarization as a narrow support instrument until dependency handling is tested further.

Sovryn produces autonomous open-research artifacts, defensive publications, and open-source research evidence. It is not a patent filing system and does not provide legal patentability, legal novelty, or freedom-to-operate opinions.
