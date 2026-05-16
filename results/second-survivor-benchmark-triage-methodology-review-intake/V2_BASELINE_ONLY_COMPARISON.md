# V2 Versus Baseline-Only

V2 survivor yield: 1.000
Baseline-only survivor yield: 0.680
V2 selected plausible claims: 17
Baseline-only selected plausible claims: 25

Baseline-only selects only on model-vs-baseline margin. V2 additionally requires split pressure, negative-control margin, rival closure, receipt replay, and manifest quality.

| Claim                     | Task | Baseline delta | Holdout delta | Negative margin | Baseline-only              | V2                         | Outcome  | Death cause           |
| ------------------------- | ---: | -------------: | ------------: | --------------: | -------------------------- | -------------------------- | -------- | --------------------- |
| V2Y-PLAUS-001-OPENML-32   |   32 |          0.099 |         0.136 |           0.134 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-002-OPENML-59   |   59 |          0.119 |         0.086 |           0.154 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-008-OPENML-43   |   43 |          0.210 |         0.125 |           0.245 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-009-OPENML-15   |   15 |          0.160 |         0.068 |           0.195 | advance_to_deep_validation | triage_reject              | killed   | holdout_not_supported |
| V2Y-PLAUS-010-OPENML-1    |    1 |          0.169 |         0.075 |           0.204 | advance_to_deep_validation | triage_reject              | killed   | holdout_not_supported |
| V2Y-PLAUS-012-OPENML-12   |   12 |          0.272 |         0.085 |           0.307 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-013-OPENML-14   |   14 |          0.081 |         0.113 |           0.116 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-015-OPENML-20   |   20 |          0.120 |         0.070 |           0.156 | advance_to_deep_validation | triage_reject              | killed   | holdout_not_supported |
| V2Y-PLAUS-016-OPENML-23   |   23 |          0.138 |         0.122 |           0.173 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-018-OPENML-27   |   27 |          0.270 |         0.095 |           0.306 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-019-OPENML-30   |   30 |          0.111 |         0.138 |           0.146 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-021-OPENML-37   |   37 |          0.150 |         0.106 |           0.185 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-022-OPENML-38   |   38 |          0.211 |         0.067 |           0.246 | advance_to_deep_validation | triage_reject              | killed   | holdout_not_supported |
| V2Y-PLAUS-024-OPENML-41   |   41 |          0.130 |         0.063 |           0.166 | advance_to_deep_validation | triage_reject              | killed   | holdout_not_supported |
| V2Y-PLAUS-025-OPENML-42   |   42 |          0.111 |         0.127 |           0.146 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-026-OPENML-48   |   48 |          0.195 |         0.087 |           0.230 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-028-OPENML-52   |   52 |          0.143 |         0.075 |           0.178 | advance_to_deep_validation | triage_reject              | killed   | holdout_not_supported |
| V2Y-PLAUS-029-OPENML-58   |   58 |          0.201 |         0.086 |           0.237 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-030-OPENML-60   |   60 |          0.153 |         0.108 |           0.188 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-031-OPENML-219  |  219 |          0.184 |         0.132 |           0.219 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-034-OPENML-29   |   29 |          0.224 |         0.099 |           0.259 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-036-OPENML-3902 | 3902 |          0.356 |         0.103 |           0.392 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
| V2Y-PLAUS-037-OPENML-3917 | 3917 |          0.282 |         0.067 |           0.316 | advance_to_deep_validation | triage_reject              | killed   | holdout_not_supported |
| V2Y-PLAUS-039-OPENML-66   |   66 |          0.131 |         0.064 |           0.166 | advance_to_deep_validation | triage_reject              | killed   | holdout_not_supported |
| V2Y-PLAUS-040-OPENML-68   |   68 |          0.217 |         0.119 |           0.252 | advance_to_deep_validation | advance_to_deep_validation | survived | none                  |
