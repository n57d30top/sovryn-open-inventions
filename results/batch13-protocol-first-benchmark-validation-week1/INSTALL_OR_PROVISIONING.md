# Install Or Provisioning

Execution environment:

- Python: 3.12.13
- numpy: 2.4.4
- pandas: 3.0.2
- scikit-learn: 1.8.0
- Host package provisioning used an isolated Python 3.12 environment.
- Docker replay image used `python:3.12-slim` with numpy, pandas, and scikit-learn installed at build time.
- The successful replay run used Docker network mode `none` and local copies of the public UCI archives.

No private data, secrets, or unsafe domains were used. The result uses direct public UCI downloads rather than a generic framework service.
