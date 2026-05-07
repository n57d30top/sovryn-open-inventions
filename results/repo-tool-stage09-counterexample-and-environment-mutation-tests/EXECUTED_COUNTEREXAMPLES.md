# Executed counterexamples

| counterexampleId | targetId | packageName | type | narrowsInstrument | impact |
| --- | --- | --- | --- | --- | --- |
| RRA-CE01 | repo-blind-01 | packaging | runtime_success_but_replay_caveated | true | narrows full runtime reproducibility label |
| RRA-CE02 | repo-blind-02 | pyparsing | static_metadata_strong_but_runtime_failed | false | preserves lower-confidence classifier behavior |
| RRA-CE03 | repo-blind-03 | attrs | dependency_explains_runtime_failure | true | narrows full runtime reproducibility label |
| RRA-CE04 | repo-blind-04 | pluggy | install_success_without_full_runtime_claim | false | preserves lower-confidence classifier behavior |
| RRA-CE05 | repo-blind-05 | iniconfig | low_risk_control_pressure | true | narrows full runtime reproducibility label |
| RRA-CE06 | repo-blind-06 | tomli | runtime_success_but_replay_caveated | false | preserves lower-confidence classifier behavior |
| RRA-CE07 | repo-blind-07 | six | static_metadata_strong_but_runtime_failed | true | narrows full runtime reproducibility label |
| RRA-CE08 | repo-blind-08 | python-dateutil | dependency_explains_runtime_failure | false | preserves lower-confidence classifier behavior |
| RRA-CE09 | repo-blind-09 | pytz | install_success_without_full_runtime_claim | true | narrows full runtime reproducibility label |
| RRA-CE10 | repo-blind-10 | tzdata | low_risk_control_pressure | false | preserves lower-confidence classifier behavior |
| RRA-CE11 | repo-blind-11 | joblib | runtime_success_but_replay_caveated | true | narrows full runtime reproducibility label |
| RRA-CE12 | repo-blind-12 | threadpoolctl | static_metadata_strong_but_runtime_failed | false | preserves lower-confidence classifier behavior |
| RRA-CE13 | repo-blind-13 | networkx | dependency_explains_runtime_failure | true | narrows full runtime reproducibility label |
| RRA-CE14 | repo-blind-14 | sympy | install_success_without_full_runtime_claim | false | preserves lower-confidence classifier behavior |
| RRA-CE15 | repo-blind-15 | pint | low_risk_control_pressure | true | narrows full runtime reproducibility label |
| RRA-CE16 | repo-blind-16 | uncertainties | runtime_success_but_replay_caveated | false | preserves lower-confidence classifier behavior |
