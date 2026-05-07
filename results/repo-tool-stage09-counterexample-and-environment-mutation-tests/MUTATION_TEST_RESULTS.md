# Mutation test results

| mutationId | targetId | packageName | mutation | observedImpact | updatesInstrument |
| --- | --- | --- | --- | --- | --- |
| RRA-MUT01 | repo-blind-01 | packaging | pinned_vs_unpinned | unexpected_partial | true |
| RRA-MUT02 | repo-blind-02 | pyparsing | minimal_vs_dev_install | preserves_lower_label | false |
| RRA-MUT03 | repo-blind-03 | attrs | smoke_vs_full_test | preserves_lower_label | false |
| RRA-MUT04 | repo-blind-04 | pluggy | example_missing | breaks_full_reproduction_claim | false |
| RRA-MUT05 | repo-blind-05 | iniconfig | version_drift | unexpected_partial | true |
| RRA-MUT06 | repo-blind-06 | tomli | fresh_workspace | preserves_lower_label | false |
| RRA-MUT07 | repo-blind-07 | six | pinned_vs_unpinned | breaks_full_reproduction_claim | false |
| RRA-MUT08 | repo-blind-08 | python-dateutil | minimal_vs_dev_install | preserves_lower_label | false |
| RRA-MUT09 | repo-blind-09 | pytz | smoke_vs_full_test | unexpected_partial | true |
| RRA-MUT10 | repo-blind-10 | tzdata | example_missing | breaks_full_reproduction_claim | false |
| RRA-MUT11 | repo-blind-11 | joblib | version_drift | preserves_lower_label | false |
| RRA-MUT12 | repo-blind-12 | threadpoolctl | fresh_workspace | preserves_lower_label | false |
| RRA-MUT13 | repo-blind-13 | networkx | pinned_vs_unpinned | unexpected_partial | true |
| RRA-MUT14 | repo-blind-14 | sympy | minimal_vs_dev_install | preserves_lower_label | false |
| RRA-MUT15 | repo-blind-15 | pint | smoke_vs_full_test | preserves_lower_label | false |
| RRA-MUT16 | repo-blind-16 | uncertainties | example_missing | breaks_full_reproduction_claim | false |
