# Execution Details

- Execution profile: venv-local-isolated
- Worker assurance: venv-local-isolated
- Actual execution included: true
- Public artifact policy: aggregate metrics only

## Procedure

The run cloned the public repository, created an isolated Python virtual environment, installed the project in editable mode, installed the missing test dependency identified from the first failed run, executed the upstream pytest suite, and executed one curated serializer round-trip example.

## Evidence

297 upstream tests passed after installing the missing test dependency freezegun; 1 curated signing example passed.
