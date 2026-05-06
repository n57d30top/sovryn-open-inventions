# Batch 15 Shuttle Deep Protocol-Risk Study

Batch 15 deeply studies UCI Statlog Shuttle because Batch 14 found the strongest random-over-source macro-F1 delta on this target.

This result loaded real Shuttle data, reproduced the source train/test files, compared source, stratified random, non-stratified random, repeated stratified seeds, and class-balanced variants, then replayed the protocol in a network-off container.

Hard answer: Shuttle's Batch 14 high severity is preserved. The strongest mechanism is rare-class and metric risk: aggregate accuracy remains high while macro-F1 and per-class F1 expose weak rare-class behavior.
