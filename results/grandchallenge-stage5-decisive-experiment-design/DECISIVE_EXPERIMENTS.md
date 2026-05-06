# Decisive Experiments

Twelve experiments were designed after Stage 4; exactly six were frozen for Stage 6 execution. Deferred designs are retained as non-executed alternatives and were not counted as frozen execution cards.

| id | target | domain | frozen | decidesIf |
| --- | --- | --- | --- | --- |
| DEXP-01 | UCI MAGIC Gamma Telescope | dataset_benchmark | yes | If centroid accuracy barely beats majority while controls remain informative, Principle 2 beats Principle 1. |
| DEXP-02 | UCI Ionosphere | dataset_benchmark | yes | A wide control gap preserves Principle 1; a close control gap preserves Principle 2. |
| DEXP-03 | Monthly Car Sales time series | time_series_temporal | yes | If shuffled-time beats temporal naive, Principle 2 weakens Principle 1. |
| DEXP-04 | slash npm package | tool_usefulness | yes | Passing positive and negative smoke supports both; missing control weakens Principle 2. |
| DEXP-05 | camelcase npm package | tool_usefulness | yes | If smoke succeeds but controls are trivial, Principle 1 beats Principle 2 on review burden. |
| DEXP-06 | escape-string-regexp npm package | tool_usefulness | yes | If both positive and negative smoke pass, both survive but neither becomes general. |
| DEXP-DESIGN-07 | UCI Yacht Hydrodynamics | dataset_benchmark | deferred | A weak control gap makes Principle 1 lose. |
| DEXP-DESIGN-08 | UCI Forest Fires | dataset_benchmark | deferred | A strong direct falsifier with passing controls makes Principle 2 lose as the primary explanation. |
| DEXP-DESIGN-09 | Daily Total Female Births time series | time_series_temporal | deferred | A weak control gap makes Principle 1 lose. |
| DEXP-DESIGN-10 | Shampoo Sales time series | time_series_temporal | deferred | A strong direct falsifier with passing controls makes Principle 2 lose as the primary explanation. |
| DEXP-DESIGN-11 | nanoid npm package | tool_usefulness | deferred | A weak control gap makes Principle 1 lose. |
| DEXP-DESIGN-12 | fast-deep-equal npm package | tool_usefulness | deferred | A strong direct falsifier with passing controls makes Principle 2 lose as the primary explanation. |
