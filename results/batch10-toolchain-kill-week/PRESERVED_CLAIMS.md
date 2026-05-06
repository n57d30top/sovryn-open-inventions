# Preserved Claims

The following claims survive the attack:

- Batch 9 loaded real public UCI Dry Bean data and executed baseline, stress, extension, and replay phases.
- Batch 9 correctly avoided a full official benchmark reproduction claim.
- Batch 9 correctly rejected the class-weight balanced LogisticRegression extension because macro-F1 decreased on the primary split.
- The Batch 9 shuffled-label control remained far below real-label LogisticRegression metrics.
- Batch 6 Diamonds remains a useful negative data-quality result, provided it is framed as an audit signal and not a claim that the dataset is unusable.
- Batch 8's pyproject-hooks failure remains a useful negative tool-reuse case for `pytest_repro_summary`.
- Batch 5 Air Quality remains useful as a sentinel-aware missingness audit where a schema-only baseline missed sentinel-coded missingness.
