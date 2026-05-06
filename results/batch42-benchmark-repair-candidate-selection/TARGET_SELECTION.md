# Target Selection

| Target | Source URL | Why selected | Rows | Features | Classes |
| --- | --- | --- | --- | --- | --- |
| UCI HAR Smartphones | https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip | high/moderate protocol fragility and subject split evidence | 10299 | 561 | 6 |
| UCI Statlog Shuttle | https://archive.ics.uci.edu/static/public/148/statlog+shuttle.zip | high rare-class metric risk | 58000 | 9 | 7 |
| UCI Vehicle Silhouettes | https://archive.ics.uci.edu/static/public/149/statlog+vehicle+silhouettes.zip | ambiguous/protocol-weak | 846 | 18 | 4 |
| UCI Letter Recognition | https://archive.ics.uci.edu/static/public/59/letter+recognition.zip | low-risk duplicate control with duplicate feature vectors | 20000 | 16 | 26 |
| UCI Optical Digits | https://archive.ics.uci.edu/static/public/80/optical+recognition+of+handwritten+digits.zip | source train/test files with random split optimism | 5620 | 64 | 10 |
| UCI Image Segmentation | https://archive.ics.uci.edu/static/public/50/image+segmentation.zip | source train/test files with caveats | 2310 | 19 | 7 |
| scikit-learn digits | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html | low-risk control | 1797 | 64 | 10 |
| scikit-learn wine | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html | protocol-absent low-risk control | 178 | 13 | 3 |

Rejected candidates included UCI Dry Bean, Rice, Iris, package-only targets, and source/evidence extraction tasks because they did not provide enough repair-specific split or claim-safety leverage for this program.
