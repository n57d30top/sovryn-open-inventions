# Next Week Targets

| hypothesis | target(s) | expected evidence | falsification test | negative control | replay plan |
| --- | --- | --- | --- | --- | --- |
| group/file overlap causes random-split inflation | HAR and Landsat | source identifiers or file/spatial proxies reveal overlap differences | no overlap or no metric change under group-aware challenger | shuffled labels and source split replay | fresh split plus container-netoff-equivalent replay |
| class imbalance plus metric choice mimics leakage | Shuttle | rare classes explain macro-F1 delta without duplicate/group leakage | class-balanced controls fail to reduce the delta explanation | majority dummy and shuffled labels | fresh seed and source split replay |
| protocol ambiguity blocks leakage conclusion | Vehicle | competing shard interpretations produce different leakage findings | a source-declared canonical protocol is found | random shard permutation control | fresh shard-holdout replay |
