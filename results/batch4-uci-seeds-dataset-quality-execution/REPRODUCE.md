# Reproduce

1. Fetch the public target from the URL listed in SELECTED_EXTERNAL_TARGET.md.
2. Run the described bounded execution in an isolated environment with network disabled for post-fetch processing when applicable.
3. Recompute the metrics listed in METRICS.json.
4. Compare the result label against the preregistered kill criteria.

The public package intentionally excludes raw logs and local machine paths.
