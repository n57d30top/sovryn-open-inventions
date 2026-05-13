# Reproduce

## Quickstart

Run from this result directory:

```bash
python3 reproduce_graph_minor_candidate.py
```

Expected output is written to `FORMAL_REPRODUCTION_RESULT.json`. The script uses only the exported public-safe files in `raw-reproduction-bundle/`.

## Replay Scope

This is a formal-manifest replay. It verifies the exported formal-object rows and Product source-cache scalars. It does not independently scrape House of Graphs or GraphClasses and does not constitute external validation.
