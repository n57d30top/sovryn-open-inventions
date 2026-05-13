# Reviewer Checklist

- [ ] Verify candidate ID matches Product package.
- [ ] Run `python3 reproduce_graph_minor_candidate.py`.
- [ ] Inspect `raw-reproduction-bundle/formal-object-check-manifest.json`.
- [ ] Compare Product measured outcome 0.424 with row recomputation 0.424.
- [ ] Verify that Product residual magnitude 0.128 is mean positive row residual, while mean signed residual is 0.105.
- [ ] Resolve whether null/trivial structural-rule baseline 0.438 explains or dominates measured outcome 0.424.
- [ ] Check `GRAPH_MINOR_BASELINE_DIRECTIONALITY_AUDIT.md` and `GRAPH_MINOR_BASELINE_DECISION.md`.
- [ ] Check whether the residual is already known/source-family documented.
- [ ] Determine whether independent source replay from concrete graph objects is possible.
- [ ] Check whether the structural baselines explain the signal.
- [ ] Check whether holdout/counterexample rows are independent enough for the bounded claim.
- [ ] Confirm no external validation or proof certification is implied.
