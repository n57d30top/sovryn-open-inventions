# Reproduce

1. Clone the public pallets/itsdangerous repository.
2. Create an isolated Python virtual environment.
3. Install the project in editable mode with pytest.
4. If test collection reports the freezegun dependency as missing, install the upstream test dependency.
5. Run pytest.
6. Execute a small URLSafeSerializer round-trip example and compare aggregate pass/fail counts.

Expected aggregate result label: external_reproduction_success.
