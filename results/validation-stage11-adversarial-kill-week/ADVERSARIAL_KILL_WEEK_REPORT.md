# Adversarial Kill Week Report

| Attack | Type | Component | Decision |
| --- | --- | --- | --- |
| AK-01 | holdout attack | Iris CSV schema residual | downgraded_or_narrowed |
| AK-02 | counterexample attack | Penguins CSV missingness residual | downgraded_or_narrowed |
| AK-03 | rival theory attack | Planets CSV sparse field residual | downgraded_or_narrowed |
| AK-04 | mutation attack | UCI Wine class-field residual | downgraded_or_narrowed |
| AK-05 | replay attack | NASA GISTEMP temporal descriptor | downgraded_or_narrowed |
| AK-06 | baseline attack | NOAA Mauna Loa monthly CO2 descriptor | downgraded_or_narrowed |
| AK-07 | overclaim attack | SILSO monthly sunspot descriptor | downgraded_or_narrowed |
| AK-08 | usefulness attack | RCSB PDB 1CRN atom descriptor | downgraded_or_narrowed |
| AK-09 | hidden assumption attack | RCSB PDB 4HHB chain descriptor | downgraded_or_narrowed |
| AK-10 | holdout attack | NASA exoplanet table descriptor | downgraded_or_narrowed |
| AK-11 | counterexample attack | simple-statistics package metadata | preserved_with_evidence |
| AK-12 | rival theory attack | csv-parse package metadata | preserved_with_evidence |
| AK-13 | mutation attack | fast-xml-parser package metadata | preserved_with_evidence |
| AK-14 | replay attack | dayjs package metadata | preserved_with_evidence |
| AK-15 | baseline attack | ajv package metadata | preserved_with_evidence |
| AK-16 | overclaim attack | lodash package manifest | preserved_with_evidence |
| AK-17 | usefulness attack | d3-array package manifest | preserved_with_evidence |
| AK-18 | hidden assumption attack | scikit-learn pyproject manifest | preserved_with_evidence |
| AK-19 | holdout attack | pymatgen pyproject manifest | preserved_with_evidence |
| AK-20 | counterexample attack | RCSB JSON entry 1CRN descriptor | preserved_with_evidence |
| AK-21 | rival theory attack | descriptor-stable but non-residual case | caveated |
| AK-22 | mutation attack | residual-like but receipt-caveated case | caveated |
| AK-23 | replay attack | receipt-stable but trivial-baseline case | caveated |
| AK-24 | baseline attack | rival-theory-favoring case | marked_uncertain |
| AK-25 | overclaim attack | low-risk control | caveated |
| AK-26 | usefulness attack | descriptor-stable but non-residual case | caveated |
| AK-27 | hidden assumption attack | residual-like but receipt-caveated case | caveated |
| AK-28 | holdout attack | receipt-stable but trivial-baseline case | marked_uncertain |
| AK-29 | counterexample attack | data artifact | caveated |
| AK-30 | rival theory attack | descriptor artifact | caveated |
| AK-31 | mutation attack | overfitting | caveated |
| AK-32 | replay attack | receipt/retrieval artifact | marked_uncertain |
| AK-33 | baseline attack | baseline insufficiency | caveated |
| AK-34 | overclaim attack | random residual noise | caveated |
| AK-35 | usefulness attack | descriptor mutation | caveated |
| AK-36 | hidden assumption attack | receipt/source mutation | marked_uncertain |
| AK-37 | holdout attack | baseline mutation | caveated |
| AK-38 | counterexample attack | residual threshold mutation | caveated |
| AK-39 | rival theory attack | label/target mutation | caveated |
| AK-40 | mutation attack | randomization control | marked_uncertain |
