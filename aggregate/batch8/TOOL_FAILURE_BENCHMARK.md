# Tool Failure Benchmark

- `schema_provenance_auditor`: Bike day/hour files are related but not schema-identical; the tool must not turn that into a data-quality defect claim without context.
- `pytest_repro_summary`: pyproject-hooks produced six test collection/runtime errors in the minimal environment; the tool correctly preserved failure as a result.
- `metric_stress_validator`: no tool failure on Sonar or Spambase, but Sonar produced high FP/FN rates that limit any performance interpretation.
