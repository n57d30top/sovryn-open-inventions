# Decision Thresholds

| Decision | Threshold |
| --- | --- |
| reject | Strong baselines explain most residuals, replay caveats hit decisive cases, or counterexamples dominate. |
| partial_signal | Some residuals survive but support is inconsistent or domain-bound. |
| promising_with_strong_caveats | Residuals survive across both narrowed target families with replay and counterexample pressure controlled. |
| validation_ready_candidate | Holdout support, replay support, baseline resistance, mutation behavior, and counterexample handling are all strong. |
