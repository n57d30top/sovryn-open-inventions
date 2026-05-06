# Reproduce

Reproduction outline:

1. Read the public `SUMMARY.json` and supporting artifacts for the attacked results.
2. Compare each custom tool's raw findings against a declared simple baseline:
   - pandas checks for schema/provenance.
   - sklearn metrics for metric-stress outputs.
   - grep, AST inventory, and pytest runtime evidence for repo-test summaries.
3. Inspect Batch 9 for metric inflation, class-specific failures, extension overclaim risk, and replay scope.
4. Inspect Batch 7 and Batch 8 for tool generalization and failure cases.
5. Recheck at least one older negative result for scope and preservation.
6. Record claim downgrades, preserved claims, updated confidence, and revision queue entries.

This package contains curated public evidence only. It does not include private execution records or private execution paths.
