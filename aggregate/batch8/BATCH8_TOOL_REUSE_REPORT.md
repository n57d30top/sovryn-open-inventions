# Batch 8 Tool Reuse and Failure Benchmark Report

Batch 8 reused the three Batch 7 custom tools on six new public external targets.

## Inputs from Batch 7

- `schema_provenance_auditor`: previously kept as a reusable candidate after UCI Wine Quality.
- `metric_stress_validator`: previously downgraded to narrow_but_useful after UCI Banknote.
- `pytest_repro_summary`: previously kept with dynamic-parametrization limitations after Pluggy.

## New targets

- UCI Student Performance math and Portuguese CSV splits.
- UCI Bike Sharing day and hour CSV files.
- UCI Sonar binary classification dataset.
- UCI Spambase binary classification dataset.
- pytest-dev/iniconfig repository.
- pypa/pyproject-hooks repository.

## Outcomes

- `metric_stress_validator` is promoted to reusable for controlled binary-classification metric checks.
- `schema_provenance_auditor` is narrowed to comparable split-file datasets because Bike day/hour files are related but not schema-identical.
- `pytest_repro_summary` is narrowed because static inventory generalized, but pyproject-hooks failed in the minimal runtime environment.

## Program learning

Batch 8 shows continuity across results: prior tools were reused, prior claims were attacked, failures were preserved, confidence was updated, and the next research direction was selected from accumulated evidence.

Next direction: promote dataset and metric validation as the next deep toolchain direction, while keeping repo test summarization as a narrow support instrument until dependency handling is tested further.
