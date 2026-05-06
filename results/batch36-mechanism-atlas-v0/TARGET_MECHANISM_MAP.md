# Target Mechanism Map

| Target | Source | Observed mechanisms | Rejected mechanisms | Not-testable mechanisms | Confidence proxy |
| --- | --- | --- | --- | --- | --- |
| UCI HAR Smartphones | https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones | group_file_subject_overlap, protocol_sensitivity | duplicate_transfer | none | 0.0228 |
| UCI Statlog Shuttle | https://archive.ics.uci.edu/dataset/148/statlog+shuttle | class_imbalance_metric_illusion, model_family_sensitivity | duplicate_transfer | group_file_subject_overlap | 0.1885 |
| UCI Statlog Landsat Satellite | https://archive.ics.uci.edu/dataset/146/statlog+landsat+satellite | no_material_mechanism_control | random_split_inflation | group_file_subject_overlap | 0.0069 |
| UCI Vehicle Silhouettes | https://archive.ics.uci.edu/dataset/149/statlog+vehicle+silhouettes | protocol_ambiguity_barrier, model_family_sensitivity | none | none | 0.0364 |
| UCI Letter Recognition | https://archive.ics.uci.edu/dataset/59/letter+recognition | no_material_mechanism_control | random_split_inflation | group_file_subject_overlap | 0.007 |
| UCI Optical Digits | https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits | protocol_sensitivity | duplicate_transfer | group_file_subject_overlap | 0.021 |
| UCI Image Segmentation | https://archive.ics.uci.edu/dataset/50/image+segmentation | protocol_sensitivity | duplicate_transfer | group_file_subject_overlap | 0.0405 |
| scikit-learn digits | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html | no_material_mechanism_control | random_split_inflation | group_file_subject_overlap | 0.0145 |
| scikit-learn wine | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html | protocol_sensitivity | duplicate_transfer | group_file_subject_overlap | 0.0192 |
| scikit-learn iris | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html | protocol_sensitivity | duplicate_transfer | group_file_subject_overlap | 0.0684 |
| UCI Dry Bean | https://archive.ics.uci.edu/dataset/602/dry+bean+dataset | evidence_packaging_dominance | none | protocol mechanisms not applicable | 0 |
| UCI Rice Cammeo/Osmancik | https://archive.ics.uci.edu/dataset/545/rice+cammeo+and+osmancik | no_material_mechanism_control | none | protocol mechanisms not applicable | 0 |
| itsdangerous package | https://palletsprojects.com/projects/itsdangerous/ | replay_instability | none | protocol mechanisms not applicable | 0 |
| pluggy package | https://pluggy.readthedocs.io/ | evidence_packaging_dominance | none | protocol mechanisms not applicable | 0 |
