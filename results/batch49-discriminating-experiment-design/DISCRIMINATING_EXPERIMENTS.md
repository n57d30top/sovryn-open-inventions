# Discriminating Experiments

| Experiment | Domain | Target | P01 prediction | P02 prediction | P03 prediction | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | benchmark/protocol | HAR | P01 predicts field-complete subject/source evidence downgrades random-only claim | P02 predicts claim-safety change matters even if metric gain is absent | P03 predicts replay cannot alone settle subject protocol claim | selected |
| E02 | benchmark/protocol | Shuttle | P01 predicts rare-class fields are required for valid claim | P02 predicts accuracy-only claim is downgraded without metric gain | P03 predicts replay preserves but does not validate metric claim | selected |
| E03 | claim-safety/ambiguity | Vehicle | P01 predicts missing protocol fields block strong claim | P02 predicts ambiguity gate is useful even without metric improvement | P03 predicts replay cannot resolve ambiguity | selected |
| E04 | benchmark/control | Letter | P01 predicts low missing-field pressure | P02 predicts repair should not materially change low-risk control | P03 predicts replay integrity is sufficient for control claim | selected |
| E05 | package reproduction | itsdangerous | P01 predicts package claim needs runtime fields not benchmark metrics | P02 predicts metric repair concepts do not transfer strongly | P03 predicts replay/import success is mostly sufficient for install claim | selected |
| E06 | dataset reliability | Wine | P01 predicts protocol-first claim blocked by absent protocol field | P02 predicts claim-safety gate useful despite good baseline | P03 predicts replay of data load is not enough for protocol claim | selected |
| E07 | time-series | Daily temperature | P01 predicts temporal-order field changes claim safety | P02 predicts metric comparison alone insufficient | P03 predicts replay alone cannot choose random vs temporal split | selected |
| E08 | package reproduction | markupsafe | P01 predicts install fields define narrow claim scope | P02 predicts no benchmark repair value | P03 predicts replay/import evidence sufficient for package-runtime claim | selected |
| E09 | benchmark/control | Digits | P01 predicts protocol-absent low-risk control blocks protocol-specific claim | P02 predicts no metric repair needed | P03 predicts replay sufficient for dataset-load claim | deferred |
| E10 | benchmark/protocol | Optical | P01 predicts source train/test fields enable protocol claim | P02 predicts claim-safety over metric gain | P03 predicts replay only integrity | deferred |
| E11 | benchmark/protocol | Image segmentation | P01 predicts source files pass with caveats | P02 predicts gate has claim-safety value | P03 predicts replay not enough for broad claim | deferred |
| E12 | package reproduction | Pluggy | P01 predicts package claim fields differ from benchmark fields | P02 predicts repair concepts mostly not applicable | P03 predicts runtime replay sufficient for package import claim | deferred |
