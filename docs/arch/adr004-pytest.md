# ADR004: Testing Framework and Coverage Strategy


## Context
We need to prove our code works without just saying "it ran once on my machine." We need a way to write automated tests and see a "Coverage" report that tells us exactly which lines of code have been tested.

## Forces
* **Boilerplate:** I want to spend my time writing tests, not writing the "ceremony" or setup code required to make tests run.
* **Visuals:** I want to see my tests in the VSCode "Testing" tab (the flask icon).

## Decision
I am choosing **pytest** along with the **pytest-cov** plugin.

I chose `pytest` over the built-in `unittest` because `unittest` requires a lot of extra "boilerplate" (like creating classes for every test). `pytest` is much simpler to write and is more popular in the industry. The `pytest-cov` plugin will give us the percentage report Chad needs to see for "validation."

## Consequences
* **Positive:** Tests are easy to write and the output is very readable.
* **Negative:** It's another dev dependency to manage, but the productivity gain is worth it.