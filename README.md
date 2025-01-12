# genpypi

Generate a Python package and publish it to PyPI in less than 1 minute. 

## Installation

You can install `genpypi` using pip: 

```bash
pip install genpypi
```

## Usage

Create a new Python package with all necessary files:

```bash
genpypi create my_package_name
```

This will generate:
- Basic package structure
- setup.py
- GitHub Actions workflow for PyPI publishing
- .gitignore
- README.md

## Publishing to PyPI

1. Create a repository on GitHub
2. Push your code to GitHub
3. Add your PyPI credentials as GitHub secrets:
   - `PYPI_PASSWORD`
4. The GitHub Action will automatically publish your package when you push to main

## License

MIT



