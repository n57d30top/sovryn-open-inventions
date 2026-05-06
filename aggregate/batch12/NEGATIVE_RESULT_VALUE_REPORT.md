# Negative Result Value Report

| Result | Decision | What it taught Sovryn |
| --- | --- | --- |
| batch5-uci-letter-recognition-baseline-challenge | preserve | A simple challenger can dominate or falsify a proposed method, so baseline-dominance checks must be mandatory. |
| batch6-diamonds-data-quality-netoff-ladder | preserve_with_scope | Duplicate and zero-dimension records are useful data-quality signals but do not make the entire dataset unusable. |
| batch7-wine-quality-schema-provenance-tool | preserve_with_tool_downgrade | Duplicate rows matter, but pandas can produce the raw finding; tool value is evidence packaging. |
| batch7-banknote-metric-stress-validator | preserve_with_scope | Dummy and shuffled-label controls are valuable, but one split cannot certify a benchmark protocol. |
| batch7-pluggy-pytest-repro-summary-tool | preserve_with_tool_narrowing | Static test inventory is useful only when reconciled against runtime collection and execution. |
| batch8-tool-reuse-failure-benchmark | preserve | Tool reuse evidence is only credible when failures and downgraded targets stay visible. |
| batch9-uci-dry-bean-deep-toolchain-study | preserve | The rejected class-weight extension prevented an unsupported improvement claim. |
| batch11-multi-target-dataset-metric-validation-program | preserve_with_program_narrowing | Seven of eight class-weight extensions were rejected or downgraded, and Vehicle fallback showed target access can fail honestly. |

Negative results were not treated as failures of the program. They were used to narrow tools and choose the next research direction.
