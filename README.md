# Dev Container and Toolchain ADRs

A reproducible Python development environment, with each tooling choice documented as an
architectural decision record.

## What it is

A dev container specification plus the reasoning behind it. Rather than a configuration
that simply exists, every tool in the stack has a written record of what was chosen, what
the alternatives were, and why the tradeoff went the way it did.

## The decisions

```
docs/arch/
  adr000-dev-container.md   containerised development as the baseline
  adr001-use-uv.md          uv for dependency resolution and virtual environments
  adr002-ruff.md            ruff for linting and formatting
  adr003-pyright.md         pyright for static type checking
  adr004-pytest.md          pytest as the test runner
```

Each record follows the standard ADR shape — context, decision, consequences — so a future
reader can tell whether a decision still holds or whether the conditions behind it have
changed.

The stack itself is modern and deliberately fast: `uv` in place of pip and venv, `ruff`
replacing flake8 and black, `pyright` for type checking, `pytest` for tests. Pinning these
in a container means every contributor gets byte-identical tooling.

## Using it

Open in VS Code with the Dev Containers extension, or:

```bash
uv sync
uv run pytest
```
