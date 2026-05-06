# Duplicate Transfer Results

| Target | Exact source train/test duplicate feature overlap | Linear delta | Interpretation |
| --- | --- | --- | --- |
| UCI HAR Smartphones | 0 | 0.0228 | duplicate mechanism not confirmed |
| UCI Statlog Shuttle | 0 | 0.1885 | duplicate mechanism not confirmed |
| UCI Statlog Landsat Satellite | 0 | 0.0069 | duplicate mechanism not confirmed |
| UCI Letter Recognition | 399 | -0.007 | duplicates noted but not sufficient |
| UCI Vehicle Silhouettes | 0 | -0.0364 | duplicate mechanism not confirmed |
| UCI Optical Digits | 0 | 0.021 | duplicate mechanism not confirmed |
| scikit-learn digits control | 0 | -0.0145 | duplicate mechanism not confirmed |

Exact duplicate transfer did not directly explain HAR or Shuttle deltas. Letter had duplicate feature overlap under random partitioning, but it was a protocol-absent control and did not support a broad leakage conclusion.
