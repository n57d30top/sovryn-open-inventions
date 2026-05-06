# Examples

## What this catches
- NAB is a public benchmark with labeled time-series files and scoring tools.
- The audited file has one labeled anomaly window in combined_windows.json.

## What this does not catch
- Rolling-MAD candidate generated many false positives on this file.
- Derivative challenger had low recall.
- Global z-score baseline had lower recall than desired but dominated candidate precision.
