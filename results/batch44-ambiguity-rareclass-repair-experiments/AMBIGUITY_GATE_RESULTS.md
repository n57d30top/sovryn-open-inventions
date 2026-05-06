# Ambiguity Gate Results

| Target | Gate decision | Reason | Claim-safety effect |
| --- | --- | --- | --- |
| UCI Vehicle Silhouettes | block_claim | Multiple plausible split interpretations exist and no single source train/test protocol is public enough for a strong protocol-first claim. | blocked_or_needs_clarification |
| scikit-learn wine | block_claim | No source train/test protocol is present; protocol-first claim should be blocked while ordinary baseline reporting may continue. | blocked_or_needs_clarification |
| UCI Image Segmentation | pass_with_caveats | Source files exist, but train/test size asymmetry makes broad claims require caveats. | pass_with_caveats |
