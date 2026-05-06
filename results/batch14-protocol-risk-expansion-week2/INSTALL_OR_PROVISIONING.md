# Install Or Provisioning

Execution environment:

- Python: 3.12.13
- numpy: 2.4.4
- pandas: 3.0.2
- scikit-learn: 1.8.0
- Host execution used an isolated Python 3.12 environment.
- Docker replay used `python:3.12-slim` with numpy, pandas, and scikit-learn installed at image build time.
- Replay used Docker network mode `none` after public data provisioning.

Provisioning notes:

- Shuttle includes `shuttle.trn.Z`; the host provisioned an uncompressed `shuttle.trn` sidecar for replay because the slim replay container does not include the historical `uncompress` utility.
- During provisioning, public UCI access for some archives was retried from a previously downloaded public cache. Source hashes are recorded in schema/provenance evidence.
- No private data, host sudo, unsafe package source, or silent fallback was used.
