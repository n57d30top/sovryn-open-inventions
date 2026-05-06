# Failed Or Partial Reproductions

- batch6-scikit-learn-iris-reproduction-ladder: partial, because the installed-package example path ran but the full upstream repository test suite did not.
- batch6-diamonds-data-quality-netoff-ladder: negative data-quality finding, because duplicate rows and zero-dimension records were confirmed under network-off replay.

No failed installation was hidden. Docker container-netoff provisioning was attempted for the network-off target and was replaced with a documented sandbox-exec network-denied replay when the local Docker VM was unavailable.
