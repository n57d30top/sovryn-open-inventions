# Prediction vs observation

| targetId | packageName | predictedLabel | observedLabel | predictionOutcome |
| --- | --- | --- | --- | --- |
| repo-blind-01 | packaging | runtime_reproducible | replay_unstable | wrong_or_partial |
| repo-blind-02 | pyparsing | runtime_reproducible | runtime_reproducible | matched |
| repo-blind-03 | attrs | runtime_reproducible | runtime_reproducible | matched |
| repo-blind-04 | pluggy | runtime_reproducible | runtime_reproducible | matched |
| repo-blind-05 | iniconfig | runtime_reproducible | runtime_reproducible | matched |
| repo-blind-06 | tomli | runtime_reproducible | runtime_reproducible | matched |
| repo-blind-07 | six | runtime_reproducible | runtime_reproducible | matched |
| repo-blind-08 | python-dateutil | runtime_reproducible | replay_unstable | wrong_or_partial |
| repo-blind-09 | pytz | static_only_evidence | runtime_reproducible | wrong_or_partial |
| repo-blind-10 | tzdata | static_only_evidence | runtime_reproducible | wrong_or_partial |
| repo-blind-11 | joblib | static_only_evidence | runtime_reproducible | wrong_or_partial |
| repo-blind-12 | threadpoolctl | static_only_evidence | runtime_reproducible | wrong_or_partial |
| repo-blind-13 | networkx | static_only_evidence | runtime_reproducible | wrong_or_partial |
| repo-blind-14 | sympy | static_only_evidence | runtime_reproducible | wrong_or_partial |
| repo-blind-15 | pint | static_only_evidence | dependency_pin_fragile | wrong_or_partial |
| repo-blind-16 | uncertainties | static_only_evidence | runtime_reproducible | wrong_or_partial |
