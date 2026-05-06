# Method

The run cloned the public repository, created an isolated Python virtual environment, installed the project in editable mode, installed the missing test dependency identified from the first failed run, executed the upstream pytest suite, and executed one curated serializer round-trip example.

## Rejected Overclaims

Rejected stronger claim: full upstream CI reproduction. This local isolated venv run did not reproduce every upstream operating system, Python version, or optional dependency matrix.
