# COMP423 Base Dev Container

The purpose of this dev container is to serve as a starting point for COMP423 projects
driven by Architectural Design Records.

## Development — Dev Container

- **Dev Container:** A minimal VS Code Dev Container is provided at [.devcontainer/devcontainer.json](.devcontainer/devcontainer.json).
- **Image (pinned):** The container is pinned to Microsoft-supported Python `3.14` using `mcr.microsoft.com/devcontainers/python:3.14`.
- **Why pinned:** Pinning to `3.14` ensures a reproducible Python runtime across developer machines and CI while remaining on the latest stable Python supported by the Dev Containers images.
- **Recommended extensions:** The container suggests `ms-python.python`, `ms-python.vscode-pylance`, and testing tools.
- **Usage:** In VS Code, choose _Remote-Containers: Open Folder in Container..._ and open the repository root to start the container.

This setup is intentionally minimal to keep onboarding fast and match CI tooling. Customize the Dev Container only if project-specific tools are required.

## Running Tests

### Via VSCode Testing Pane

1. Open the Testing pane (flask icon in the Activity Bar)
2. Click "Run all tests" or run individual tests
3. View code coverage in the integrated terminal

### Via Command Line

Run all tests with coverage:

```bash
uv run pytest
```

Run specific test file:

```bash
uv run pytest tests/test_main.py
```

Run with verbose output:

```bash
uv run pytest -v
```

View coverage report in HTML format:

```bash
uv run pytest --cov=src --cov-report=html
open htmlcov/index.html
```

### Test Configuration

All test configuration is in [pyproject.toml](pyproject.toml):
- **Test discovery:** Looks for tests in the `tests/` directory
- **Coverage:** Measures coverage for the `src/` module
- **Reports:** Generates terminal and HTML coverage reports