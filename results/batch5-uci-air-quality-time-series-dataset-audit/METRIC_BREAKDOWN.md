# Metric Breakdown

## Scalar Metrics

| Metric | Value |
| --- | --- |
| target | UCI Air Quality UCI time-series dataset |
| executionProfile | container-netoff |
| rowCount | 9357 |
| columnCount | 15 |
| numericColumnCount | 13 |
| duplicateTimestamps | 0 |
| timeGapCount | 0 |
| maxGapHours | 1 |
| negativeTimeDiffs | 0 |
| wins | 1 |
| losses | 0 |
| ties | 0 |

## Main Comparison

| Metric | Schema-only baseline | Sentinel-aware challenger |
| --- | ---: | ---: |
| true positives | 0 | 4 |
| false positives | 0 | 0 |
| true negatives | 9 | 9 |
| false negatives | 4 | 0 |
| precision | 0 | 1 |
| recall | 0 | 1 |
| f1 | 0 | 1 |

## Missing Sentinel Rates

| Column | Rate |
| --- | ---: |
| NMHC(GT) | 0.902 |
| CO(GT) | 0.18 |
| NOx(GT) | 0.175 |
| NO2(GT) | 0.175 |
| PT08.S1(CO) | 0.039 |
| C6H6(GT) | 0.039 |
| PT08.S2(NMHC) | 0.039 |
| PT08.S3(NOx) | 0.039 |
| PT08.S4(NO2) | 0.039 |
| PT08.S5(O3) | 0.039 |
| T | 0.039 |
| RH | 0.039 |
| AH | 0.039 |

## Numeric Summaries

| Column | Summary |
| --- | --- |
| CO(GT) | usableCount: 7674, min: 0.1, max: 11.9, mean: 2.153, iqr: 1.8, iqrOutliers: 215 |
| PT08.S1(CO) | usableCount: 8991, min: 647, max: 2040, mean: 1099.833, iqr: 294, iqrOutliers: 118 |
| NMHC(GT) | usableCount: 914, min: 7, max: 1189, mean: 218.812, iqr: 230, iqrOutliers: 55 |
| C6H6(GT) | usableCount: 8991, min: 0.1, max: 63.7, mean: 10.083, iqr: 9.6, iqrOutliers: 228 |
| PT08.S2(NMHC) | usableCount: 8991, min: 383, max: 2214, mean: 939.153, iqr: 382, iqrOutliers: 64 |
| NOx(GT) | usableCount: 7718, min: 2, max: 1479, mean: 246.897, iqr: 228, iqrOutliers: 435 |
| PT08.S3(NOx) | usableCount: 8991, min: 322, max: 2683, mean: 835.494, iqr: 312, iqrOutliers: 240 |
| NO2(GT) | usableCount: 7715, min: 2, max: 340, mean: 113.091, iqr: 64, iqrOutliers: 107 |
| PT08.S4(NO2) | usableCount: 8991, min: 551, max: 2775, mean: 1456.265, iqr: 447, iqrOutliers: 97 |
| PT08.S5(O3) | usableCount: 8991, min: 221, max: 2523, mean: 1022.906, iqr: 543, iqrOutliers: 91 |
| T | usableCount: 8991, min: -1.9, max: 44.6, mean: 18.318, iqr: 12.6, iqrOutliers: 3 |
| RH | usableCount: 8991, min: 9.2, max: 88.7, mean: 49.234, iqr: 26.7, iqrOutliers: 0 |
| AH | usableCount: 8991, min: 0.185, max: 2.231, mean: 1.026, iqr: 0.577, iqrOutliers: 2 |

