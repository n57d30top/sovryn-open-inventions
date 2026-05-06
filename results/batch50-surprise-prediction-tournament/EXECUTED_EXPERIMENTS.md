# Executed Experiments

| Experiment | Domain | Target | Observation | Classification |
| --- | --- | --- | --- | --- |
| E01 | benchmark/protocol | HAR | source macro-F1 0.9537 vs random 0.9832; source subject overlap 0 by file construction | principle_A_supported |
| E02 | benchmark/protocol | Shuttle | accuracy-macro gap 0.3604; rare-class reporting downgrades accuracy-only claim | principle_B_supported |
| E03 | claim-safety/ambiguity | Vehicle | random macro-F1 0.8197 vs file-variant 0.8211; competing interpretations change conclusion | principle_A_supported |
| E04 | benchmark/control | Letter | low-risk control had 553 duplicate feature rows but claim-safety did not require broad repair | principle_B_supported |
| E05 | package reproduction | itsdangerous | safe import/version runtime check passed (2.2.0) | principle_C_supported |
| E06 | dataset reliability | Wine | data load and baseline pass, but protocol-first claim is blocked because protocol field is absent | principle_A_supported |
| E07 | time-series | Daily temperature | temporal MAE 3.4288 vs random MAE 3.3126; temporal protocol changes claim | principle_A_supported |
| E08 | package reproduction | markupsafe | safe import/version runtime check passed (3.0.3) | principle_C_supported |
