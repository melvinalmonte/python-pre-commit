# python-pre-commit

1. Install pre-commit: `pip install pre-commit` will install [pre-commit](https://github.com/pre-commit/pre-commit)
2. Add pre-commit to requirements.txt `pip freeze | grep pre-commit >> requirements.txt`
3. Define `.pre-commit-config.yaml` with the hooks you want to include.
4. Execute `pre-commit install` to install git hooks in your .git/ directory similar to that of husky.

## Example using Black and flake8

[Black](https://github.com/psf/black) for formatting (similar to prettier in js) and [flake8](https://flake8.pycqa.org/en/latest/) for PEP8 compliance (similar to eslint for node apps)

## Notes

View .pre-commit-config.yaml for an example of the pre-commit config that will be installed.

View pyproject.toml for an example of a simple Black config.
