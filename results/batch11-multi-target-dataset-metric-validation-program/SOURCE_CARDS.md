# Source Cards

## UCI Rice Cammeo/Osmancik

- Source URL: https://archive.ics.uci.edu/dataset/545/rice+cammeo+and+osmancik
- UCI ID: 545
- DOI: not recorded in this run
- Access method: `ucimlrepo.fetch_ucirepo(id=...)` plus local CSV export for repeatable analysis.
- Expected task: binary classification of rice grain varieties from image-derived morphology features.
- Expected metric: accuracy and macro-F1.
- Safety note: safe agricultural image-derived classification dataset.
- License/access note: UCI public dataset page was used as source authority; downstream reuse should follow the UCI page and dataset citation.

## UCI Optical Recognition of Handwritten Digits

- Source URL: https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits
- UCI ID: 80
- DOI: not recorded in this run
- Access method: `ucimlrepo.fetch_ucirepo(id=...)` plus local CSV export for repeatable analysis.
- Expected task: ten-class classification of 8x8 handwritten digit feature grids.
- Expected metric: accuracy and macro-F1.
- Safety note: safe image-derived digit classification dataset.
- License/access note: UCI public dataset page was used as source authority; downstream reuse should follow the UCI page and dataset citation.

## UCI Iris

- Source URL: https://archive.ics.uci.edu/dataset/53/iris
- UCI ID: 53
- DOI: https://doi.org/10.24432/C56C76
- Access method: `ucimlrepo.fetch_ucirepo(id=...)` plus local CSV export for repeatable analysis.
- Expected task: three-class plant species classification from tabular morphology features.
- Expected metric: accuracy and macro-F1.
- Safety note: safe classic tabular classification dataset.
- License/access note: UCI public dataset page was used as source authority; downstream reuse should follow the UCI page and dataset citation.

## UCI Wine Recognition

- Source URL: https://archive.ics.uci.edu/dataset/109/wine
- UCI ID: 109
- DOI: https://doi.org/10.24432/C5PC7J
- Access method: `ucimlrepo.fetch_ucirepo(id=...)` plus local CSV export for repeatable analysis.
- Expected task: three-class cultivar classification from physicochemical measurements.
- Expected metric: accuracy and macro-F1.
- Safety note: safe small tabular classification dataset.
- License/access note: UCI public dataset page was used as source authority; downstream reuse should follow the UCI page and dataset citation.

## Tool And Package Sources

- `schema_provenance_auditor`: Batch 7 Sovryn custom tool, reused unchanged.
- `metric_stress_validator`: Batch 7 Sovryn custom tool, reused unchanged.
- `pandas`: tabular loading and ordinary baseline checks.
- `scikit-learn`: dummy, linear, tree, metric, split, and replay baselines.
- `ucimlrepo`: public UCI dataset loader.

## Source Reference Evidence

`evidence/source-references.json` records the same public source set in structured form.
