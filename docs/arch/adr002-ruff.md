# ADR002: Choosing a Linter and Formatter for SynerCast.ai


## Context
Our code is currently inconsistent, which makes it hard for the team to read and causes "noise" in our Git commits. We need a way to automatically format code (fixing spaces/quotes) and lint code (catching logical errors like unused variables) before Chad does his next demo.

## Forces
* **Simplicity:** As a student, I want fewer configuration files to manage.
* **Speed:** The tool should be fast enough that I don't mind it running every time I save.
* **All-in-one:** Choosing one tool that does both jobs is better than juggling multiple tools like Black and Pylint.

## Decision
I am choosing **Ruff**. 

Ruff is a modern tool written in Rust that is extremely fast. It replaces both Black (the formatter) and Pylint/Flake8 (the linters). It’s easy to set up in a single `pyproject.toml` file, which fits our goal of reducing "toil."

## Consequences
* **Positive:** We only need one dev dependency for both formatting and linting. VSCode integration is seamless.
* **Negative:** Ruff is newer than the traditional tools, but it's becoming the industry standard very quickly.