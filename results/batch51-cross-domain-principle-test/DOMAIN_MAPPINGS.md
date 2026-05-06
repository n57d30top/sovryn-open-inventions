# Domain Mappings

| Domain | Required field analogue | Failure mode |
| --- | --- | --- |
| benchmark/protocol | source split, group/file fields, metric fields | strong claim blocked if fields absent |
| repo/test reproduction | test command, runtime dependency, failure classification | install/import pass too narrow for broad reproduction claim |
| dataset reliability | source, schema, protocol, target fields | data loads but protocol claim blocked |
| package install/test | import/version/runtime check | only narrow runtime claim supported |
| time-series | temporal order and split field | random split weakens temporal claim |
| source/evidence extraction | execution-backed evidence field | metadata-only transfer not applicable |
