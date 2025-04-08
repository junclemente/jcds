# jcds Library

[![Latest Release](https://img.shields.io/github/v/release/junclemente/jcds?label=release)](https://github.com/junclemente/jcds/releases)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docs](https://img.shields.io/badge/docs-online-blue)](https://junclemente.github.io/jcds)

**jcds** is a modular Python library designed to support reproducible workflows in data science and exploratory data analysis (EDA).  
It provides a curated collection of functions for inspecting, transforming, and accessing tabular data from local and cloud sources, with particular emphasis on usability within Jupyter notebooks.

This project originated during my time as a graduate student in the **MSADS (Master of Science in Applied Data Science)** program at the [University of San Diego](https://www.sandiego.edu/engineering/graduate/ms-applied-data-science.php).  
I often ran into repetitive tasks — inspecting nulls, handling encodings, wrangling column names, or working with messy CSVs and S3-hosted files — across multiple class and capstone projects.  
To address these real-world pain points, I began building **jcds** as a personal toolkit grounded in **DRY (Don't Repeat Yourself)** principles — and have been pair programming alongside **Generative AI** to refine and expand it throughout my learning journey.

> **Compatible with Python 3.7 and above. Developed and tested on Python 3.10.**

---

## How to Use

### Install with `pip`

#### Quick Install

This installs the latest version of the library and all core dependencies.

```bash
pip install git+https://github.com/junclemente/jcds.git
```

#### Specific Version

To install a specific version (e.g., `v0.2.1`), add the version tag at the end:

```bash
pip install git+https://github.com/junclemente/jcds.git@v0.2.1
```

#### Develop Branch

Or install from the `develop` branch (not recommended):

```bash
pip install git+https://github.com/junclemente/jcds.git@develop
```

#### Optional: AWS Support

If you plan to use the `aws` module (for working with AWS S3, etc.), you'll need to install with the optional `aws` dependencies:

```bash
pip install git+https://github.com/junclemente/jcds.git@v0.2.1[aws]
```

This will install:

- `boto3`
- `botocore`

These dependencies are only required if you need to use the AWS module.

---

### Import with `httpimport`

You can also import this library directly into your Jupyter notebook using [`httpimport`](https://pypi.org/project/httpimport/):

```python
import httpimport

with httpimport.github_repo('junclemente', 'jcds', ref='<branch>'):
    import jcds as jcds
```

You can also import specific submodules as needed:

```python
import jcds.eda as eda
```

### Minimal Usage Example

```python
import pandas as pd
import jcds.eda as jeda

df = pd.read_csv('data.csv')
```

## Branching Info

When specifying the `ref` in `httpimport.github_repo()`, use one of the following:

- `develop` - Actively evolving. This may contain breaking changes as new features are added or modified.
- Versioned tags (e.g., `0.1.0`, `0.2.0`) - Stable and locked. These will not change and are safe for reproducibility.

**Recommended:** Use a versioned branch to ensure your code doesn't break when updates are pushed to `develop`.

## Help System

Each **subpackage** in the `jcds` library includes a `help()` function that lists all **public functions** available within.

### Global help -- across all submodules

```python
import jcds
jcds.help() # List all functions in the jcds library (aws, eda, etc...)
```

### Subpackage-specific help

```python
import jcds.eda
jcds.eda.help() # List all functions in the jcds.eda package

import jcds.aws as jaws
jaws.help() # List all functions in the jcds.aws package
```

### To view documentation for a specific function:

```python
jcds.eda.help('dqr_cat') # Shows the docstring for the function 'dqr_cat`
```

## Testing

This project uses `pytest` for unit testing.

To run all tests:

```bash
pytest
```

To run a specific test file:

```bash
pytest tests/unit/test_eda_helpers.py
```

Fixtures and sample test datasets are defined in `tests/unit/test_utils.py`.

Test coverage:

```bash
pytest --cov=jcds --cov-report=term
```

## Documentation

**Documentation:** [https://junclemente.github.io/jcds](https://junclemente.github.io/jcds)


This project uses [MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/) and [mkdocstrings](https://mkdocstrings.github.io/).

### 🔄 Updating the Docs

1. Make sure all public functions and modules have proper docstrings (Google or NumPy style recommended).
2. If you add or rename modules, update `mkdocs.yml` and corresponding `.md` files in the `docs/` folder.
3. Preview docs locally:

   ```bash
   mkdocs serve
   ```
    This starts a local dev server at: 
    ```cpp
    http://127.0.0.1:8000/
    ``` 
    Any changes make to the Markdown files, Python docstrings, or theme settings will auto-reload. 
4. To deploy to GitHub Pages:
    ```bash
    mkdocs gh-deploy
    ```
    Make sure `site_url` and `repo_url` are set correctly in the `mkdocs.yml`. 

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for a list of version history and updates.
