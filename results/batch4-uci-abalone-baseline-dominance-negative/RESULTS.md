# Results

A container-netoff benchmark challenge on UCI Abalone rejected a hand-built shell-size challenger because the best simple shell-weight threshold baseline reached F1 0.770 while the challenger reached F1 0.724.

## Top-Level Metrics

| Metric | Value |
| --- | ---: |
| target | UCI Abalone |
| executionProfile | container-netoff |
| rowCount | 4177 |
| columnCount | 9 |
| trainRows | 3341 |
| testRows | 836 |
| duplicateRows | 0 |
| wins | 0 |
| losses | 1 |
| ties | 0 |

## Best Baseline

| Field | Value |
| --- | --- |
| feature | shell_weight |
| threshold | 0.172 |
| direction | gte |
| metric | {"tp":368,"fp":169,"tn":248,"fn":51,"precision":0.685,"recall":0.878,"specificity":0.595,"accuracy":0.737,"f1":0.77,"balancedAccuracy":0.737} |

## Challenger

| Field | Value |
| --- | --- |
| name | provenance_weighted_shell_size_score |
| metric | {"tp":320,"fp":145,"tn":272,"fn":99,"precision":0.688,"recall":0.764,"specificity":0.652,"accuracy":0.708,"f1":0.724,"balancedAccuracy":0.708} |
| rejected | true |
