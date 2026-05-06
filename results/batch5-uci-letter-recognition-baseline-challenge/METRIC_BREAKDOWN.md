# Metric Breakdown

## Scalar Metrics

| Metric | Value |
| --- | --- |
| target | UCI Letter Recognition vowel-vs-consonant challenge |
| executionProfile | container-netoff |
| rowCount | 20000 |
| columnCount | 17 |
| trainRows | 16000 |
| testRows | 4000 |
| positiveClass | vowels A/E/I/O/U |
| negativeClass | consonants |
| classCountLetters | 26 |
| duplicateRows | 1332 |
| wins | 0 |
| losses | 1 |
| ties | 0 |

## Main Comparison

| Metric | Best baseline | Challenger |
| --- | ---: | ---: |
| precision | 0.253 | 0.217 |
| recall | 0.856 | 0.792 |
| specificity | 0.403 | 0.324 |
| accuracy | 0.49 | 0.413 |
| f1 | 0.391 | 0.34 |
| balanced accuracy | 0.63 | 0.558 |

## Best Baseline Top 3

| Feature | Threshold | Direction | F1 |
| --- | ---: | --- | ---: |
| xy2bar | 8 | gte | 0.391 |
| ybar | 9 | lt | 0.38 |
| xedgey | 10 | lt | 0.371 |

