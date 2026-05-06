# Target Selection Rationale

- Dataset/schema/provenance: UCI Wine Quality was selected because it has two related public CSV files where split-schema and duplicate provenance checks matter.
- Benchmark/metric validation: UCI Banknote Authentication was selected because a measurable classifier baseline can be challenged against dummy and shuffled-label controls.
- Repo/test/result extraction: pytest-dev/pluggy was selected because it is a public Python repository with a real pytest suite and reproducible test execution.
