# Executed Transfer Tests

| Domain | Target | Result | Evidence |
| --- | --- | --- | --- |
| package install/test reproduction | itsdangerous signing check | partial_success | roundtrip passed and tamper negative control passed |
| package install/test reproduction | markupsafe escape check | success | escaping changed unsafe markup into inert text |
| repo/test reproduction with runtime evidence | pluggy runtime hook check | success | runtime hook returned expected value |
| time-series temporal split benchmark | daily minimum temperature temporal split | partial_success | temporal_rmse=6.451; random_rmse=3.936 |
| scientific dataset reliability | UCI Letter duplicate/reliability check | partial_success | duplicate_overlap=399; low-risk delta=-0.007 |
| scientific dataset reliability | scikit-learn wine class support check | success | classes=3; low-risk delta=-0.0192 |
| protocol-card benchmark validation | HAR protocol source control | success | source group overlap=0; random group overlap=30 |
| protocol-card benchmark validation | Vehicle ambiguity control | partial_success | file partitions executable but protocol meaning remains ambiguous |
| source/evidence extraction evidence check | Batch evidence-card completeness check | not_testable | transfer did not include new source extraction execution |
