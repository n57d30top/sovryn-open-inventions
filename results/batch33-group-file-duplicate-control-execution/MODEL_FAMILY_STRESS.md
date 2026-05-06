# Model Family Stress

| Target | Linear delta | Forest delta | ExtraTrees delta |
| --- | --- | --- | --- |
| UCI HAR Smartphones | 0.0228 | 0.0564 | 0.0452 |
| UCI Statlog Shuttle | 0.1885 | -0.0024 | not run |
| UCI Statlog Landsat Satellite | 0.0069 | -0.0001 | not run |
| UCI Vehicle Silhouettes | -0.0364 | 0.0384 | 0.0459 |
| UCI Optical Digits | 0.021 | 0.0145 | 0.014 |

Mechanism strength was model-family sensitive. Shuttle showed a large linear delta but no matching forest delta, so its mechanism should be phrased as class/metric/model-dependent rather than universal split inflation.
