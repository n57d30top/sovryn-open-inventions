# Checkpoint Results

The daemon writes checkpoints under the relative artifact root `.sovryn/discovery-daemon/checkpoints/`. Resume reads the latest checkpoint and continues from persisted search state.

This package does not expose raw daemon logs or local absolute paths.
