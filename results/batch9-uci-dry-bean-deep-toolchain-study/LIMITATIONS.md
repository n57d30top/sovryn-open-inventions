# Limitations

- This result does not claim a full benchmark reproduction.
- No official train/test split or exact paper protocol was reproduced.
- The UCI data was treated as one public table; leakage checks are limited without source split metadata.
- Duplicate row findings are audit signals, not proof that records are invalid.
- Class-weight extension results are bounded to the tested split and replay seed.
- The public package contains curated evidence, not raw command logs or private execution paths.
- The study is safe computational analysis only; it contains no operationally unsafe content.
