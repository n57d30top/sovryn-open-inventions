# Preregistration

Research question: Can a type-aware public dataset audit catch quality issues that a schema-only baseline misses on UCI Auto MPG?

Metrics fixed before evaluation:
- row count
- column count
- missing horsepower count
- duplicate full rows
- issue recall

Kill criteria:
- dataset cannot be fetched
- missing values cannot be distinguished from strings
- audit claims semantic data correctness

Publication criteria: publish only if the result includes external target binding, concrete metrics, failures/losses, limitations, reproducibility instructions, and public hygiene pass.
