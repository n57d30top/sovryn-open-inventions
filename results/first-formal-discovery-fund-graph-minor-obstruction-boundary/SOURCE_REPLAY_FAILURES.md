# Source Replay Failures

## Failure 1: No Concrete Source Object Binding

The public bundle does not contain HOG or GraphClasses object identifiers for the 72 rows. It contains generated family labels and row-level summary fields.

Impact: reviewers cannot independently map `FORMAL-GRAPH-MINOR-CHECK-001` through `FORMAL-GRAPH-MINOR-CHECK-072` to public source objects.

## Failure 2: No Public Graph Encoding

The public bundle does not include graph6 strings, adjacency matrices, edge lists, or source download receipts for the specific checked objects.

Impact: object-level recomputation from source is not possible.

## Failure 3: Generated Canonical Families

The Product generator constructs rows from canonical family formulas for `cycle`, `wheel`, `complete_bipartite`, `grid`, `ladder`, and `complete`.

Impact: reconstructing those families verifies the Product generator shape, but not independent HOG/GraphClasses source replay.

## Failure 4: Holdout Is Not Source-Independent

The holdout slice has the same rounded aggregate metrics as the development slice.

Impact: the holdout is replay-consistent but not persuasive as an independent source-family holdout.

## Failure 5: Baseline Dominance Ambiguity

The null/trivial structural-rule baseline is `0.438`, above the measured outcome `0.424`.

Impact: public discovery scoring is blocked until directionality is resolved or the candidate beats this baseline under the same metric direction.
