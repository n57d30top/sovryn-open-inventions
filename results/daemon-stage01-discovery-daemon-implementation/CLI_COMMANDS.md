# CLI Commands

The new command group is `sovryn discover-daemon ...`.

Implemented commands:

- `sovryn discover-daemon status --json`
- `sovryn discover-daemon init --json`
- `sovryn discover-daemon run --mode silent --until fund --json`
- `sovryn discover-daemon resume --json`
- `sovryn discover-daemon cycle --json`
- `sovryn discover-daemon candidate-status --json`
- `sovryn discover-daemon graveyard --json`
- `sovryn discover-daemon fund-gate --json`
- `sovryn discover-daemon notify-if-fund --json`
- `sovryn discover-daemon audit --json`

The daemon rejects non-silent fund-search invocation modes.
