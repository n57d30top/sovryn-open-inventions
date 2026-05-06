# Target Results

## student-performance-splits

- Tool: `schema_provenance_auditor`
- Target: UCI Student Performance math and Portuguese CSV splits
- Status: `reusable_success`
- Execution: network-off replay after public archive download
- Result: schema_match=True; rows=1044; missing_cells=0; duplicate_full_rows=0

## bike-sharing-day-hour

- Tool: `schema_provenance_auditor`
- Target: UCI Bike Sharing day and hour CSV files
- Status: `failure_case_expected_schema_mismatch`
- Execution: network-off replay after public archive download
- Result: schema_match=False; rows=18110; hour file adds an hr column, so split-schema equality is not a valid assumption

## sonar-classification

- Tool: `metric_stress_validator`
- Target: UCI Sonar binary classification dataset
- Status: `reusable_success_with_high_error_rates`
- Execution: deterministic stratified split with dummy, logistic, and shuffled-label controls
- Result: logistic_balanced_accuracy=0.794; majority_balanced_accuracy=0.500; shuffled_balanced_accuracy=0.445; false_positive_rate=0.206; false_negative_rate=0.207

## spambase-classification

- Tool: `metric_stress_validator`
- Target: UCI Spambase binary classification dataset
- Status: `reusable_success`
- Execution: deterministic stratified split with dummy, logistic, and shuffled-label controls
- Result: logistic_balanced_accuracy=0.914; majority_balanced_accuracy=0.500; shuffled_balanced_accuracy=0.511; false_positive_rate=0.053; false_negative_rate=0.119

## iniconfig-pytest

- Tool: `pytest_repro_summary`
- Target: pytest-dev/iniconfig repository
- Status: `reusable_success`
- Execution: editable package install, AST inventory, grep baseline, and pytest target execution
- Result: ast_tests=31; grep_tests=31; runtime_passed=49; return_code=0

## pyproject-hooks-pytest

- Tool: `pytest_repro_summary`
- Target: pypa/pyproject-hooks repository
- Status: `failure_case_minimal_environment_errors`
- Execution: editable package install, AST inventory, grep baseline, and pytest target execution
- Result: ast_tests=32; grep_tests=32; runtime_errors=6; return_code=2
