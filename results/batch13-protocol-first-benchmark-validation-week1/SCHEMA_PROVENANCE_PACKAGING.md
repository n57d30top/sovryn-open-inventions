# Schema Provenance Packaging

`schema_provenance_auditor` is intentionally used as packaging-only evidence in this batch.

| Target | Rows | Features | Classes | Missing cells | Duplicate full rows | Value beyond pandas |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| UCI Human Activity Recognition Using Smartphones | 10299 | 561 | 6 | 0 | 0 | source-hash-bound evidence packaging and explicit protocol metadata, not raw discovery |
| UCI Optical Recognition of Handwritten Digits | 5620 | 64 | 10 | 0 | 0 | source-hash-bound evidence packaging and explicit protocol metadata, not raw discovery |
| UCI Pen-Based Recognition of Handwritten Digits | 10992 | 16 | 10 | 0 | 0 | source-hash-bound evidence packaging and explicit protocol metadata, not raw discovery |

Ordinary pandas checks exposed the same raw missingness and duplicate facts. The custom tool value was source-hash binding, protocol metadata packaging, and standardized evidence cards.
