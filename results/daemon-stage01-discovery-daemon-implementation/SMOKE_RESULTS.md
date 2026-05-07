# Smoke Results

Verified commands after build:

- `discover-daemon status --json`: returned `continue_searching` with `fundFound: false`.
- `discover-daemon run --mode silent --until fund --max-cycles 1 --json`: executed one bounded cycle, suppressed notification, and kept `continue_searching`.
- `discover-daemon candidate-status --json`: reported an internal killed candidate status only.
- `discover-daemon graveyard --json`: reported one internal graveyard entry after the smoke cycle.
- `discover-daemon notify-if-fund --json`: suppressed notification because no fund exists.
- `discover-daemon audit --json`: passed the required daemon gates.

No public Fund notification package was produced.
