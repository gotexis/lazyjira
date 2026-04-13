# Contributing to lazyjira

Thanks for your interest in contributing! lazyjira is a zero-dependency CLI for Jira Cloud, and we'd love your help making it better.

## Development Setup

```bash
# Clone
git clone https://github.com/gotexis/lazyjira.git
cd lazyjira

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in editable mode
pip install -e .

# Run tests
python -m pytest
```

## Project Structure

```
src/lazyjira/
├── __init__.py          # Version
├── __main__.py          # python -m lazyjira entry
├── cli.py               # Argument parsing and routing
├── api.py               # HTTP client (urllib only)
├── config.py            # Configuration resolution
├── format.py            # Output formatting + Markdown→ADF
└── commands/
    ├── issues.py        # issues subcommand
    ├── comments.py      # comments subcommand
    ├── move.py          # status transitions
    ├── labels.py        # label listing
    ├── links.py         # issue linking
    ├── projects.py      # project listing
    └── query.py         # raw JQL
```

## The Golden Rule: Zero Dependencies

lazyjira uses **only the Python standard library**. No exceptions. This is the project's core differentiator.

- HTTP? `urllib.request`
- JSON? `json`
- CLI args? `argparse`
- Colors? ANSI escape codes

If your contribution adds an `import` that isn't in stdlib, it will not be merged.

## Code Style

- **Type hints** — use them on function signatures
- **Docstrings** — one-liner for simple functions, multi-line for complex ones
- **No classes where functions suffice** — keep it simple
- **`from __future__ import annotations`** — at the top of every module
- **Max line length** — 100 characters (soft limit)
- **Formatting** — we use standard Python conventions. Run your editor's formatter

## Making Changes

1. **Fork** the repo and create a branch from `main`
2. **Write code** — follow the style guide above
3. **Write tests** — add tests in `tests/` for new functionality
4. **Test locally** — `python -m pytest`
5. **Commit** — use clear, descriptive commit messages
6. **Push** and open a **Pull Request**

### Commit Messages

```
feat: add board listing command
fix: handle 401 when token is expired
docs: update configuration examples
test: add tests for markdown-to-adf conversion
```

## Pull Request Guidelines

- Keep PRs focused — one feature or fix per PR
- Update the README if you add a new command or flag
- All CI checks must pass
- Maintainers may request changes — that's normal and healthy

## Reporting Bugs

Use [GitHub Issues](https://github.com/gotexis/lazyjira/issues) with the **Bug Report** template. Include:

- Your Python version (`python3 --version`)
- lazyjira version (`lazyjira --version`)
- Your OS
- Full error output
- Steps to reproduce

## Requesting Features

Use [GitHub Issues](https://github.com/gotexis/lazyjira/issues) with the **Feature Request** template. Explain:

- What problem does this solve?
- How do you currently work around it?
- What would the ideal command look like?

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
