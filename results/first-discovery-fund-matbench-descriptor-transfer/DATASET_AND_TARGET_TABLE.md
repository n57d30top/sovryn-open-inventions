# Dataset And Target Table

| Item | Value | Public/copy ref | Review caveat |
| --- | --- | --- | --- |
| Domain | computational_materials_property_data | `FUND_CANDIDATE.json` | Domain label is Product-recorded. |
| Public benchmark family | Matbench materials property tasks | `https://matbench.materialsproject.org/` | Public source is inspectable; URL fragments in Product refs may be semantic. |
| Raw public data pointer | Matbench experimental band-gap JSON | `https://huggingface.co/datasets/smgjch/Matbench/resolve/main/matbench_expt_gap.json` | Source access can be checked independently; this package does not include full raw-data recomputation code. |
| Product source receipt | `rawTargetCount: 300`; source receipt and hashes recorded | `copied-product-evidence/matbench-source-cache.json` | Supporting context for a Matbench source-cache run. |
| Candidate runtime output | `matbench_descriptor_transfer_significance_generator-output-01` | `copied-product-evidence/runtime-evidence-output-01.json` | Primary Product runtime evidence copied for public inspection. |
| Target id | `matbench_descriptor_transfer_significance_generator-target-01` | `copied-product-evidence/runtime-evidence-output-01.json` | Product-generated target id, not an external Matbench task id. |
| Measured variable | `matbench_descriptor_transfer_property_residual` | `copied-product-evidence/runtime-evidence-output-01.json` | Reviewer should request exact feature construction before scientific acceptance. |
| Measured outcome | `0.72` | `copied-product-evidence/runtime-evidence-output-01.json` | Product-recorded scalar. |
| Residual magnitude | `0.21` | `copied-product-evidence/runtime-evidence-output-01.json` | Product-recorded scalar; no uncertainty interval is claimed. |
| Tool families | pymatgen, matminer, ase, scikit-learn, numpy | `copied-product-evidence/runtime-evidence-output-01.json` | Tool names are recorded, but this package does not expose a full runnable pipeline script. |

