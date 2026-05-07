# Reproduce

Build and inspect the daemon with relative commands from the product repository:

```bash
npm run build
npm test
node dist/cli.js discover-daemon init --json
node dist/cli.js discover-daemon run --mode silent --until fund --max-cycles 1 --json
node dist/cli.js discover-daemon status --json
node dist/cli.js discover-daemon audit --json
```

A no-fund run should remain `continue_searching` and suppress notification.
