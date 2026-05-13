# Independent Source Replay Results

## Result

`independent_source_replay_failed_manifest_only_replay_available`

## Public Source Fetch

| Source | Fetch Result | Replay Usefulness |
|---|---|---|
| `https://hog.grinvin.org/` | redirects to `https://houseofgraphs.org/`; landing page fetched | confirms public source exists, but does not bind the 72 manifest rows to concrete public graph objects |
| `https://www.graphclasses.org/` | landing page fetched | confirms public graph-class source exists, but does not provide the 72 row object definitions |

## What Was Replayed

The public script replays the exported manifest:

- 72 rows loaded from `raw-reproduction-bundle/formal-object-check-manifest.json`
- measured outcome recomputed as `0.424`
- simple baseline recomputed as `0.319`
- signed row residual recomputed as `0.105`
- Product residual magnitude recomputed as mean positive residual `0.128`
- null/trivial structural rule recomputed as `0.438`

## What Was Not Replayed

The following were not independently replayed from source:

- HOG graph object IDs,
- graph6/adjacency encodings,
- GraphClasses class membership witnesses,
- true minor-obstruction checks against public graph objects,
- source-family independent holdout objects.

## Decision

The current package has public manifest replay, not independent source replay. This blocks external-review-ready discovery scoring until concrete source objects or source receipts are added and the replay is rerun from those public objects.
