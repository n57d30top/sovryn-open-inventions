# Schema Provenance Packaging

`schema_provenance_auditor` is packaging-only in Batch 14.

| Target | Source hash prefix | Missing cells | Duplicate full rows | Classes | Value beyond pandas |
| --- | --- | ---: | ---: | ---: | --- |
| UCI Human Activity Recognition Using Smartphones | c00b803081a5c797 | 0 | 0 | 6 | source-hash-bound evidence packaging and explicit protocol metadata, not raw discovery |
| UCI Statlog Shuttle | a03e1f23755093ef | 0 | 0 | 7 | source-hash-bound evidence packaging and explicit protocol metadata, not raw discovery |
| UCI Statlog Landsat Satellite | 7c54e0e11c872a1b | 0 | 0 | 6 | source-hash-bound evidence packaging and explicit protocol metadata, not raw discovery |
| UCI Letter Recognition | 3b5f07a334697b6c | 0 | 1332 | 26 | source-hash-bound evidence packaging and explicit protocol metadata, not raw discovery |

Ordinary pandas checks exposed the raw missingness, duplicate, and class-count facts. The added value was standardized source binding, protocol metadata, and evidence packaging.
