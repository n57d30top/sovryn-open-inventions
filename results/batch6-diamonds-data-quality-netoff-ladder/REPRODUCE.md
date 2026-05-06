# Reproduce

- Download diamonds.csv from the public seaborn-data repository.
- Create an isolated Python environment with Python 3.12 and pandas installed.
- Run the audit script under a network-denied sandbox profile.
- Compute duplicate-row counts and nonpositive numeric values for carat, depth, table, price, x, y and z.
- Treat duplicate and zero-dimension records as data-quality findings, not as proof that the dataset is unusable.

Use public sources listed in SOURCE_CARD.md. Publish only summarized metrics and limitations; do not publish command transcripts or machine-specific paths.
