# Failure Autopsy

Formal v0 failed because the candidate generator produced many shallow patterns and because finite testing could not substitute for proof. v1 treated that as a generator-design problem rather than trying to revive v0 candidates.

Concrete failure causes:
- candidate templates overused small seed windows
- known-pattern rejection was local and incomplete
- simple arithmetic and periodic rules consumed search budget
- one-off candidates were easier to falsify than parameterized families
- counterexample search found boundary witnesses late
- proof sketches lacked lemma structure
- bounded tests gave confidence without proof route clarity
- holdout predictions were too similar to generation cases
- replay verified computations but not general truth
- baseline low-complexity rules explained many candidates
- symbolic identities included tautology risk
- automata outputs often collapsed to periodic patterns
