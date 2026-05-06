# Preregistration

Research question: Can a type-aware dataset-quality audit catch Palmer Penguins missing-value issues that a schema-only baseline under-detects?

Metrics fixed before execution:
- row count
- column count
- missing cells by field
- duplicate full rows
- issue recall

Kill criteria:
- source unavailable
- missing values hidden as valid strings
- semantic correctness claimed without source review
