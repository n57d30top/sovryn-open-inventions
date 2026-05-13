# Method

## Data Source

The replay uses the exported formal object check manifest at `raw-reproduction-bundle/formal-object-check-manifest.json`. The manifest rows were generated from six canonical graph families (`cycle`, `wheel`, `complete_bipartite`, `grid`, `ladder`, and `complete`) with House of Graphs and GraphClasses serving only as public anchors. The package does not contain concrete HOG/GraphClasses graph IDs, graph6 strings, edge lists, or adjacency matrices for an independent source replay.

## Target Outcome

Bounded graph-family obstruction-score residual after density/average-degree/treewidth-proxy scoring, known-family negative controls, and generated-counterexample controls.

## Computation

The standalone script reads each check row and recomputes:

- average obstruction score (`measuredOutcome = 0.424`)
- average simple-baseline score (`0.319`)
- mean signed row residual (`0.105`)
- mean positive row residual (`0.128`)
- mean absolute row residual (`0.150`)
- known-family negative-control score (`0.356`)
- null/trivial structural-rule score (`0.438`)
- holdout/development row counts and family summaries

## Baselines and Rivals

Recorded baselines are preserved in `raw-reproduction-bundle/formal-source-cache.json`: size/density/degree/treewidth proxy baseline, matched known-family negative control, and null/trivial structural rule.

The public directionality audit treats higher scores as stronger structural signal unless a baseline-specific direction is justified. Under that audit, the `0.438` null/trivial structural-rule score is directionally comparable and exceeds measured outcome `0.424`, so it is fatal for public discovery scoring until repaired.

## Residual Formula Caveat

The Product residual magnitude `0.128` is the mean positive row residual. The public row manifest also exposes signed residuals; the row-level mean signed residual is `0.105`. The derivation is documented in `GRAPH_MINOR_RESIDUAL_FORMULA.md`.

## Failure Modes

The candidate should be downgraded if the public source families document the same boundary as ordinary known behavior, if an independent HOG/GraphClasses replay does not reproduce the manifest rows, if a simple structural rule explains the pattern, or if generated counterexamples collapse the claim.
