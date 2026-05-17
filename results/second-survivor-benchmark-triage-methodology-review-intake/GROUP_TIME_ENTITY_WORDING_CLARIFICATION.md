# Group / Time / Entity Wording Clarification

The V2 100-claim challenge uses concrete public-field deterministic split
manifests.

These manifests are not claimed to be official dataset-author group, time, or
entity protocols unless a dataset source separately documents that protocol.

Recommended wording:

- Use: `public-field deterministic split manifest`.
- Use: `stress-test split` when the split is constructed by Sovryn from a public
  field.
- Use: `official group/time/entity protocol` only when an external dataset or
  benchmark source explicitly provides that protocol.

What this package currently shows:

- each 100-claim row has a public OpenML task/dataset receipt;
- each row has a deterministic field-based split construction;
- V2 selected 17 plausible non-control rows whose manifest-backed
  deep-validation rows survived the bounded checks.

What this package does not show:

- no claim that all OpenML tasks have official group/time/entity split metadata;
- no claim that the public-field stress-test split is the unique correct split;
- no claim of external validation or benchmark-theory acceptance.
