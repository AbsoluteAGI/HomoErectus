# Contributing

This repository is a public whitepaper plus an early runtime skeleton.

Use it for:

- architecture discussion
- contract review
- public-safe runtime scaffolding
- contributor onboarding

Do not use it for:

- publishing private credentials, deployment data, or proprietary runtime logic
- assuming the public skeleton reflects every implementation detail of the active private runtime

Contribution priorities:

1. Keep architecture documents internally consistent.
2. Prefer minimal, well-named skeleton code over speculative large implementations.
3. When changing architecture terms, update `README.md` and affected layer documents together.
4. Keep public examples runnable with minimal local setup.

For code contributions:

- keep the public runtime surface small and readable
- favor smoke tests over complex infrastructure dependencies
- avoid exposing private environment assumptions from the active development repo
