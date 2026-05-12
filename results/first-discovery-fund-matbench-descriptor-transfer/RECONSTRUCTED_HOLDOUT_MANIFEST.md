# Reconstructed Holdout Manifest

This deterministic holdout supports public replay of the proxy experiment. It is not an independent source-family holdout for the Product claim.

- Split rule: `sha256(formula)[0:8] modulo 5 equals 0 for holdout; all other buckets train`
- Holdout rows: `194`
- Classification: `deterministic_formula_hash_holdout_not_source_family_independent`
- Machine-readable manifest: `RECONSTRUCTED_HOLDOUT_MANIFEST.json`
