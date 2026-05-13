# Exact Graph-Minor Claim

## Reviewer-Facing Bounded Claim

In the exported public-safe formal object check manifest, 72 bounded graph-family rows generated from six canonical families (`cycle`, `wheel`, `complete_bipartite`, `grid`, `ladder`, and `complete`) have mean obstruction score `0.424`. The row-level simple structural baseline has mean `0.319`, and the Product residual magnitude equals the mean positive row residual `0.128`. This supports only a bounded replay signal over the exported manifest rows: some family slices, especially `wheel`, have obstruction-score residuals above the simple baseline under the recorded formulas.

## Object Class

- Object class: exported bounded graph-family rows in `raw-reproduction-bundle/formal-object-check-manifest.json`.
- Families represented: `cycle`, `wheel`, `complete_bipartite`, `grid`, `ladder`, `complete`.
- Row count: 72.
- Development rows: 48.
- Holdout rows: 24.
- Public source anchors: House of Graphs and GraphClasses.

## Measured Property

The measured property is `bounded_graph_minor_obstruction_residual`, defined over the exported row fields as:

- `obstructionScore`: bounded score derived from treewidth proxy, degree variance, and a graph-family term.
- `simpleBaselineScore`: bounded score derived from density and average degree.
- `residual`: `obstructionScore - simpleBaselineScore`.

## Candidate Prediction

The bounded candidate prediction is that positive residual structure persists across at least two graph-family/source slices after simple size, density, degree, treewidth-proxy, known-family, and generated-control pressure.

## Rival Predictions

- Size/density/degree/treewidth rival: the measured residual is ordinary structural complexity.
- Known-family rival: `wheel`, `complete_bipartite`, or other family membership explains the high residual rows.
- Source-family rival: nominal HOG/GraphClasses family assignment explains the observed split.
- Null/trivial structural-rule rival: a trivial rule based on density or normalized degree matches or dominates the measured outcome.

## Falsifiers

The candidate is downgraded if any of these hold:

- The `0.438` null/trivial structural-rule baseline is directionally comparable to `measuredOutcome = 0.424` and therefore dominates it.
- Independent source replay cannot reconstruct concrete HOG/GraphClasses graph objects corresponding to the 72 rows.
- The holdout slice is only a repeated generated-family distribution rather than an independent source-family slice.
- Known graph-family facts explain the high residual rows.
- The claim cannot be turned into a precise forbidden-minor, obstruction, proof, or refutation statement.

## What Is Not Claimed

This package does not claim:

- a proved theorem,
- a certified forbidden-minor characterization,
- a new graph-minor obstruction family,
- independent HOG or GraphClasses reproduction,
- external human validation,
- Nobel/Einstein-level significance,
- breakthrough status,
- external adoption.

## Current Reviewer Interpretation

The current package is best read as a replayable bounded manifest signal, not as an accepted mathematical discovery. It requires independent source replay and graph-theory review before discovery scoring should be restored.
