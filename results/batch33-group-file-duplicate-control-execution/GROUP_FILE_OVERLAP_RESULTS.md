# Group/File/Subject Overlap Results

| Target | Source train/test group overlap | Random train/test group overlap | Group/file field status |
| --- | --- | --- | --- |
| UCI HAR Smartphones | 0 | 30 | present |
| UCI Vehicle Silhouettes | 0 | 9 | present |
| UCI Statlog Shuttle | None | None | not testable |
| UCI Statlog Landsat Satellite | None | None | not testable |
| UCI Letter Recognition | None | None | not testable |
| UCI Optical Digits | None | None | not testable |
| scikit-learn digits control | None | None | not testable |

HAR supported the group/subject-overlap mechanism: source overlap was 0 while random splitting mixed all 30 subjects. Vehicle file partitions were usable as approximations but protocol semantics remain ambiguous. Other targets lacked explicit group/file IDs, so overlap was marked not testable rather than inferred.
