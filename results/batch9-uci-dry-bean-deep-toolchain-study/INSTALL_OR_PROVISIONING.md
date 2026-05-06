# Install Or Provisioning

Host execution environment:

- Created a fresh Python virtual environment for Batch 9.
- Installed `pandas`, `scikit-learn`, and `ucimlrepo`.
- Loaded UCI Dry Bean by dataset ID 602.

Host package versions from the run:

- Python: 3.14.4
- pandas: 3.0.2
- scikit-learn: 1.8.0
- numpy: 2.4.4
- ucimlrepo: 0.0.7

Container replay environment:

- Built a local image from `python:3.10-slim` with pinned pandas, numpy, and scikit-learn.
- Replayed a meaningful phase with `--network none` on preloaded public data.
- Container package versions: Python 3.10.20, pandas 2.3.3, scikit-learn 1.7.2.

No host sudo, global install, private data, or standalone repository was used.
