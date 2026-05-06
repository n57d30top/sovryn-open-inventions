# Reproduce

- Create an isolated Python environment with Python 3.12.
- Install ucimlrepo, pandas and scikit-learn.
- Fetch UCI dataset id 165.
- Use an 80/20 train-test split with random_state 20260506.
- Run DummyRegressor with mean and median strategies and RandomForestRegressor with 200 estimators and min_samples_leaf 2.
- Report MAE, RMSE and R2 for each model.

Use public sources listed in SOURCE_CARD.md. Publish only summarized metrics and limitations; do not publish command transcripts or machine-specific paths.
