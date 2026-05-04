# Tool Design: mol-record-auditor

The tool reads a small chemistry-style molecular-property dataset, validates
required fields, normalizes Celsius/Kelvin values with `pint`, groups a fixed
toy identifier equivalence map, detects duplicate conflicts and outliers, scores
provenance, and writes deterministic public audit artifacts.

The custom tool is needed because the research question is about reproducible
data-quality evidence, not chemical modeling. The tool deliberately avoids
synthesis, wet-lab guidance, drug-design, hazardous optimization, and broad
SMILES canonicalization claims.
