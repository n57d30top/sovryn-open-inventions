# Competing Protocol Interpretations

| interpretation | why plausible | assumptions | source evidence | missing evidence | claim boundary |
| --- | --- | --- | --- | --- | --- |
| source_shard_holdout_last_file | Uses source shard boundaries as a holdout convention. | xaa-xah train, xai test. | shard files exist. | no source text declares this as canonical. | approximated only |
| two_shard_file_holdout | Holds out more source shards to test shard sensitivity. | last two shards are test. | ordered shard file names exist. | no benchmark protocol declares this. | stress variant only |
| stratified_random_same_size | ordinary challenger for comparison. | random class-preserving split is acceptable only as challenger. | none as source protocol. | all protocol semantics. | not source protocol |
| non_stratified_random_same_size | tests sensitivity to ordinary random split without class preservation. | same test fraction. | none as source protocol. | all protocol semantics. | negative control only |
