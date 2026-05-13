# Reproduce

## Quickstart

Run from this result directory:

```bash
python3 reproduce_graph_minor_candidate.py
```

Expected output is written to `FORMAL_REPRODUCTION_RESULT.json`. The script uses only the exported public-safe files in `raw-reproduction-bundle/`.

## Replay Scope

This is a formal-manifest replay. It verifies the exported formal-object rows and Product source-cache scalars. It does not independently scrape House of Graphs or GraphClasses, does not reconstruct graph objects from concrete graph encodings, and does not constitute external validation.

The expected status after replay is `package_repair_required_before_external_review`, because the package still lacks independent source replay and the `0.438` null/trivial structural-rule baseline blocks public discovery scoring.
