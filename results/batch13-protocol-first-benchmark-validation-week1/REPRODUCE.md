# Reproduce

1. Create an isolated Python 3.12 environment.
2. Install `numpy`, `pandas`, and `scikit-learn`.
3. From the result directory, run:

```bash
python evidence/batch13_protocol_analysis.py   --output-dir evidence   --data-dir .batch13-data   --extract-dir .batch13-extract
```

4. Build the optional replay image:

```bash
docker build -f Dockerfile.batch13 -t sovryn-batch13-protocol-replay .
```

5. Replay after public data provisioning with external network disabled:

```bash
docker run --rm --network none   -v "$PWD/.batch13-data:/data:ro"   -v "$PWD/.batch13-replay-output:/output"   -v "$PWD/.batch13-replay-extract:/extract"   sovryn-batch13-protocol-replay   --output-dir /output   --data-dir /data   --extract-dir /extract   --replay-only
```

The public package includes structured JSON evidence and omits raw downloaded data and unstructured logs.
