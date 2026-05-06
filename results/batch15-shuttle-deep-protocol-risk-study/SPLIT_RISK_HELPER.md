# Split-Risk Helper

A tiny target-local helper is included at `evidence/split_risk_helper.py`.

It computes protocol-vs-random deltas, rare-class warnings, and severity labels from metric tables. It was tested with:

- positive case: high macro-F1 delta plus rare-class warning gives high severity.
- negative case: tiny delta and no rare-class warning gives low/none severity.

The helper adds packaging value and consistent scoring. It does not replace sklearn metrics or manual per-class review.
