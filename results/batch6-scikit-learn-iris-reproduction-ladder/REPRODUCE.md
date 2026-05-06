# Reproduce

- Create an isolated Python environment with Python 3.12.
- Install scikit-learn.
- Load sklearn.datasets.load_iris().
- Run DummyClassifier, StandardScaler plus LogisticRegression, and DecisionTreeClassifier with five-fold stratified cross-validation using random_state 20260506.
- Compare the dummy and model accuracies; do not report full upstream reproduction unless the upstream test suite is also executed.

Use public sources listed in SOURCE_CARD.md. Publish only summarized metrics and limitations; do not publish command transcripts or machine-specific paths.
