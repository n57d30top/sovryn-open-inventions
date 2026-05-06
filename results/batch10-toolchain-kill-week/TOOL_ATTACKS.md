# Tool Attacks

## schema_provenance_auditor

Attack:

- Could ordinary pandas `shape`, `isna`, `duplicated`, and `value_counts` produce the same raw findings?
- Did the tool infer target semantics on Dry Bean?
- Were duplicate-row findings scientifically meaningful or just audit notes?

Outcome:

- Raw single-table findings are dominated by simple pandas checks.
- The tool did not infer Dry Bean's target column or class distribution without Batch 9 wrapper logic.
- Duplicate rows remain useful audit signals, but not proof of invalid records.

Decision: `narrow_but_useful`.

## metric_stress_validator

Attack:

- Could sklearn produce the same base metrics?
- Does shuffled-label control prove the result is free of leakage?
- Does strong LogisticRegression dominance make the toolchain insight less special?

Outcome:

- sklearn can produce the underlying metrics.
- The tool still adds value by packaging dummy controls, shuffled-label controls, macro-F1 checks, and explicit inflation flags.
- Shuffled-label control is not sufficient to prove absence of leakage or official benchmark reproduction.

Decision: `reusable_support_tool`.

## pytest_repro_summary

Attack:

- Is static AST or grep inventory reliable enough to claim runtime reproduction?
- Does dynamic parametrization break static-count interpretation?
- Do dependency failures limit reuse?

Outcome:

- Static inventory is useful, but runtime collection and target dependency state matter more.
- Batch 7 Pluggy had 107 static definitions and 126 runtime passes, showing expected runtime expansion.
- Batch 8 pyproject-hooks had runtime errors under a minimal environment, preserving the dependency limitation.

Decision: `narrow_but_useful_support_only`.
