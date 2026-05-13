# Independent Source Replay Plan

## Goal

Attempt to replay the candidate from public graph sources rather than from Product/exported manifest rows.

## Source Targets

| Source | Intended Use | Required for Success |
|---|---|---|
| House of Graphs / HOG | concrete public graph objects or graph identifiers matching manifest rows | graph object IDs or graph6/adjacency data for the 72 rows |
| GraphClasses / ISGCI | class/family definitions and known relation context | graph-class facts that bind specific rows to known classes |
| Exported corpus bundle | public-safe fallback | not sufficient for independent source replay by itself |

## Replay Steps

1. Fetch public source landing pages and confirm source availability.
2. Look for concrete graph object definitions or downloadable row-level graph encodings.
3. If source objects are available, recompute vertices, edges, density, degree sequence, treewidth proxy, obstruction score, baselines, residuals, controls, and holdout.
4. If source objects are unavailable, attempt reconstruction only from public manifest rows and classify as manifest replay, not independent source replay.

## Success Criteria

Independent source replay succeeds only if a reviewer can start from public HOG/GraphClasses graph object data or public graph encodings and reproduce the relevant row-level quantities without relying on Product-generated canonical family rows.

## Non-Success Criteria

The following do not count as independent source replay:

- rerunning `reproduce_graph_minor_candidate.py` on exported Product manifest rows,
- reconstructing generic `cycle`, `wheel`, `complete_bipartite`, `grid`, `ladder`, or `complete` graphs from family names alone,
- relying on Product formulas without source object IDs,
- citing HOG/GraphClasses landing pages without binding them to concrete objects.
