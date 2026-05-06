# Results

A container-netoff time-split benchmark on UCI Bike Sharing compared a simple temperature threshold baseline with a weather-comfort challenger; the challenger tied rather than beat the baseline, so no benchmark win is claimed.

## Top-Level Metrics

| Metric | Value |
| --- | ---: |
| target | UCI Bike Sharing day.csv |
| executionProfile | container-netoff |
| rowCount | 731 |
| columnCount | 16 |
| trainRows | 511 |
| testRows | 220 |
| medianTrainDemand | 3974 |
| duplicateRows | 0 |
| wins | 0 |
| losses | 0 |
| ties | 1 |

## Best Baseline

| Field | Value |
| --- | --- |
| feature | temp |
| threshold | 0.44083 |
| direction | gte |
| metric | {"tp":154,"fp":0,"tn":21,"fn":45,"precision":1,"recall":0.774,"specificity":1,"accuracy":0.795,"f1":0.873,"balancedAccuracy":0.887} |

## Challenger

| Field | Value |
| --- | --- |
| name | weather_comfort_score |
| threshold | 0.26339 |
| metric | {"tp":151,"fp":0,"tn":21,"fn":48,"precision":1,"recall":0.759,"specificity":1,"accuracy":0.782,"f1":0.863,"balancedAccuracy":0.879} |
| rejected | false |
