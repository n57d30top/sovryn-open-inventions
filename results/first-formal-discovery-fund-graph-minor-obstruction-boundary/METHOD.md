# Method

## Data Source

The replay uses the exported formal object check manifest at `raw-reproduction-bundle/formal-object-check-manifest.json`. The public source anchors are House of Graphs and GraphClasses.

## Target Outcome

Bounded graph-minor obstruction residual after size, density, degree-sequence, treewidth-proxy, known-family, and generated-counterexample controls.

## Computation

The standalone script reads each check row, recomputes average obstruction score, average simple-baseline score, signed and absolute residual summaries, candidate-mechanism hold rate, rival-explains rate, and holdout/development counts.

## Baselines and Rivals

Recorded baselines are preserved in `raw-reproduction-bundle/formal-source-cache.json`: size/density/degree/treewidth proxy baseline, matched known-family negative control, and null/trivial structural rule. Rival pressure is scoped to whether these explain the exported bounded manifest signal.

## Residual Formula Caveat

The Product residual magnitude 0.128 is replayed from the source cache. The public row manifest exposes signed residuals; the row-level mean signed residual is 0.105. The exact Product residual normalization is not independently re-derived from the row fields alone, so reviewers should treat the residual magnitude as source-cache replay plus row-level support, not a newly certified theorem.

## Failure Modes

The candidate should be downgraded if the public source families document the same boundary as ordinary known behavior, if an independent HOG/GraphClasses replay does not reproduce the manifest rows, if a simple structural rule explains the pattern, or if generated counterexamples collapse the claim.
