# Reviewer Checklist

- [ ] Verify candidate ID matches Product package.
- [ ] Run `python3 reproduce_graph_minor_candidate.py`.
- [ ] Inspect `raw-reproduction-bundle/formal-object-check-manifest.json`.
- [ ] Compare Product measured outcome 0.424 with row recomputation 0.424.
- [ ] Check whether the residual is already known/source-family documented.
- [ ] Check whether the structural baselines explain the signal.
- [ ] Check whether holdout/counterexample rows are independent enough for the bounded claim.
- [ ] Confirm no external validation or proof certification is implied.
