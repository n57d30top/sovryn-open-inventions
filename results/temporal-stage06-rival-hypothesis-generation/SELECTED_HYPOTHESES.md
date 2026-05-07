# Selected Hypotheses

| ID | Name | Mechanism | Variables |
| --- | --- | --- | --- |
| TH-01 | Random Split Optimism Boundary | Random splits can leak local temporal neighborhood information when autocorrelation is high. | autocorrelation, chronological MAE, random challenger MAE, horizon |
| TH-02 | Horizon-Window Instability Boundary | Evaluation fragility appears when short and long horizons produce different baseline rankings. | short horizon error, long horizon error, window policy |
| TH-03 | Seasonality Artifact Rival | Many apparent temporal failures are seasonal naive baseline artifacts. | seasonal lag, seasonal naive error, random challenger error |
| TH-04 | Source Protocol Ambiguity Rival | Temporal claims fail because source/protocol fields are ambiguous rather than due to real temporal structure. | date column clarity, target column clarity, replay stability |
| TH-05 | Nonstationarity Shock Boundary | Temporal fragility is concentrated where later holdout distribution shifts from early training history. | rolling mean drift, holdout variance, trend error |
| TH-06 | Low-Risk Control Boundary | Temporal controls with weak autocorrelation or ambiguous ordering should not support the candidate. | autocorrelation, missing order field, control label |
