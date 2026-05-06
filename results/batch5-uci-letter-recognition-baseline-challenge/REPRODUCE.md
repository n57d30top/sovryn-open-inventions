# Reproduce

1. Fetch the public UCI Letter Recognition data file.
2. Split rows deterministically into the first 16000 training rows and final 4000 holdout rows.
3. Define positive class as A/E/I/O/U and negative class as consonants.
4. Tune single-feature threshold baselines on the training split.
5. Freeze the compact_geometry_vowel_score challenger.
6. Run the frozen baseline and challenger in a network-disabled container and compare holdout metrics.

Expected aggregate result label: benchmark_challenge_negative_result.
