# Conjecture Families

## formal-v1-family-01-01

For the generated small-graph family F_20, the degree-radius compression invariant bounds the clique/independent-set gap after leaf expansion.

- generatorFamily: graph_invariant
- candidateIds: formal-v1-promoted-001
- parameters: vertices, edges, degree_sequence, radius, clique_bound
- falsifier: A parameterized witness where the invariant relation fails.
- proof route: degree-sum invariant plus extremal graph induction

## formal-v1-family-01-02

For the generated small-graph family F_30, the degree-radius compression invariant bounds the clique/independent-set gap after leaf expansion.

- generatorFamily: graph_invariant
- candidateIds: formal-v1-promoted-002
- parameters: vertices, edges, degree_sequence, radius, clique_bound
- falsifier: The generated family is falsified or narrowed by size=18.
- proof route: degree-sum invariant plus extremal graph induction

## formal-v1-family-02-01

For recurrence family F_20, the second finite-difference transform predicts a stable modular residue class beyond the seed window.

- generatorFamily: recurrence_relation
- candidateIds: formal-v1-promoted-021
- parameters: n, seed_window, finite_difference, modulus
- falsifier: A parameterized witness where the invariant relation fails.
- proof route: finite-difference induction and recurrence characteristic route

## formal-v1-family-02-02

For recurrence family F_30, the second finite-difference transform predicts a stable modular residue class beyond the seed window.

- generatorFamily: recurrence_relation
- candidateIds: formal-v1-promoted-022
- parameters: n, seed_window, finite_difference, modulus
- falsifier: The generated family is falsified or narrowed by size=18.
- proof route: finite-difference induction and recurrence characteristic route

## formal-v1-family-03-01

For polynomial family F_20, the bounded coefficient transform preserves the finite-sum identity under the registered parameter shift.

- generatorFamily: symbolic_identity
- candidateIds: formal-v1-promoted-041
- parameters: n, degree, coefficient_vector, shift
- falsifier: A parameterized witness where the invariant relation fails.
- proof route: coefficient comparison and polynomial identity route

## formal-v1-family-04-01

For automaton family F_20, accepted-word counts obey a state-compression recurrence after quotienting mirror-equivalent states.

- generatorFamily: automata_combinatorial
- candidateIds: formal-v1-promoted-056
- parameters: word_length, states, alphabet, transition_matrix
- falsifier: A parameterized witness where the invariant relation fails.
- proof route: transfer-matrix recurrence and state quotient invariant route
