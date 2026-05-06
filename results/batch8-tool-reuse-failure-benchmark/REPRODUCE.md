# Reproduce

1. Start from the Batch 7 custom tools.
2. Create an isolated Python environment with pandas, scikit-learn, and pytest.
3. Download the six public targets listed in SOURCE_CARD.md.
4. Run schema_provenance_auditor on Student Performance and Bike Sharing split files.
5. Run metric_stress_validator on Sonar and Spambase.
6. Run pytest_repro_summary on iniconfig and pyproject-hooks after editable installs.
7. Compare the curated metrics with SUMMARY.json and TARGET_RESULTS.md.

Expected outcome: the same qualitative tool decisions, with exact numeric metrics varying only if upstream targets change.
