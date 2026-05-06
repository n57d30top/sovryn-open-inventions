# Examples and Non-Examples

## Examples

| Id | Example |
| --- | --- |
| benchmark_protocol_example | HAR source-vs-random split claim with subject fields, source split, baselines, metric stress, replay, and limitations. |
| leakage_not_testable_example | Vehicle-like target where group fields are absent and protocol language is ambiguous, so leakage mechanism cannot be strongly claimed. |
| repo_reproduction_example | CLI help/build/test reproduction claim with repo revision, build result, command result, and environment summary. |
| dataset_quality_example | Wine dataset quality claim with schema, class support, missingness, duplicate check, and negative control. |
| conceptual_principle_example | Required Evidence Field Boundary claim with rival principles, frozen predictions, failed cases, and scope update. |

## Non-Examples

| Id | Non-example |
| --- | --- |
| metric_only_nonexample | A high accuracy number without split definition, baseline, negative control, or replay does not support a strong benchmark claim. |
| leakage_guess_nonexample | A random split delta alone does not support a leakage claim when group, duplicate, or feature overlap fields are absent. |
| tool_demo_nonexample | A tool demo without baseline comparison does not support a tool usefulness claim. |
| transfer_slogan_nonexample | A principle name appearing in two domains without prediction failures or scope narrowing does not support transfer. |
| ambiguous_protocol_nonexample | A dataset description with unclear file roles does not support official protocol reproduction. |
