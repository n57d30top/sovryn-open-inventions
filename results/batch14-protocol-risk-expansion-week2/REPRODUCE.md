# Reproduce

1. Create an isolated Python 3.12 environment.
2. Install `numpy`, `pandas`, and `scikit-learn`.
3. From the result directory, run:

```bash
python evidence/batch14_protocol_risk_analysis.py   --output-dir evidence   --data-dir .batch14-data   --extract-dir .batch14-extract
```

4. If replaying Shuttle in a minimal container, provision an uncompressed `shuttle.trn` beside `shuttle.zip` after public download.
5. Build the optional replay image:

```bash
docker build -f Dockerfile.batch14 -t sovryn-batch14-protocol-risk-replay .
```

6. Replay after public data provisioning with external network disabled:

```bash
docker run --rm --network none   -v "$PWD/.batch14-data:/data:ro"   -v "$PWD/.batch14-replay-output:/output"   -v "$PWD/.batch14-replay-extract:/extract"   sovryn-batch14-protocol-risk-replay   --output-dir /output   --data-dir /data   --extract-dir /extract   --replay-only
```

The public package includes structured JSON evidence and omits raw downloaded data and unstructured logs.
