# Pipeline Report

Pipeline ID: lab-pipeline-48df1f2e1931

## Stages

- data_ingestion: container-netoff, replay-critical=true
- data_validation: container-netoff, replay-critical=true
- preprocessing: container-netoff, replay-critical=true
- feature_extraction: container-netoff, replay-critical=true
- baseline_run: container-netoff, replay-critical=true
- candidate_method_run: container-netoff, replay-critical=true
- statistical_analysis: container-netoff, replay-critical=true
- ablation: container-netoff, replay-critical=true
- sensitivity: container-netoff, replay-critical=true
- replication: container-netoff, replay-critical=true
- falsification: container-netoff, replay-critical=true
- report_generation: container-netoff, replay-critical=false
- corpus_packaging: container-netoff, replay-critical=true

All stages use curated public-safe outputs and degrade with evidence rather than silently skipping required outputs.
