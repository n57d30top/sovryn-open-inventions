# Install Or Provisioning

Host execution used an isolated Python environment with:

- Python 3.14.4
- pandas 3.0.2
- numpy 2.4.4
- scikit-learn 1.8.0
- ucimlrepo 0.0.7

External package provisioning performed:

- `pandas`
- `scikit-learn`
- `ucimlrepo`

Container replay:

- Image build succeeded: true
- Container run succeeded: true
- Network mode: `none`
- Targets replayed in container: 2

The container replay reran both required tools and a LogisticRegression replay for Rice and Optical Digits.
