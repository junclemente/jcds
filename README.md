# 📦 jcds (Python Library)

[![Latest Release](https://img.shields.io/github/v/release/junclemente/jcds?label=release)](https://github.com/junclemente/jcds/releases)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Build Status](https://github.com/junclemente/jcds/actions/workflows/python-app.yml/badge.svg)
[![Docs](https://img.shields.io/badge/docs-online-blue)](https://junclemente.github.io/jcds/)

**jcds** is a modular Python library (hosted in the [jcds-lib](https://github.com/junclemente/jcds) repository) designed to support reproducible workflows in data science and exploratory data analysis (EDA).  
It provides a curated collection of functions for inspecting, transforming, and accessing tabular data from local and cloud sources, with particular emphasis on usability within Jupyter notebooks.

📚 This project originated during my time as a graduate student in the **MSADS (Master of Science in Applied Data Science)** program at the [University of San Diego](https://www.sandiego.edu/engineering/graduate/ms-applied-data-science.php).  
I often ran into repetitive tasks — inspecting nulls, handling encodings, wrangling column names, or working with messy CSVs and S3-hosted files — across multiple class and capstone projects.  
To address these real-world pain points, I began building **jcds** as a personal toolkit grounded in **DRY (Don't Repeat Yourself)** principles — and have been pair programming alongside **Generative AI 🤖** to refine and expand it throughout my learning journey.

> ✅ **Compatible with Python 3.7 and above. Developed and tested on Python 3.10.**

---

## 🔧 How to Use

### 📥 Install with `pip`

#### ⚡ Quick Install

```bash
pip install git+https://github.com/junclemente/jcds.git
```

#### 📌 Specific Version

```bash
pip install git+https://github.com/junclemente/jcds.git@v0.2.1
```

#### 🧪 Develop Branch (unstable)

```bash
pip install git+https://github.com/junclemente/jcds.git@develop
```

#### ☁️ Optional: AWS Support

```bash
pip install git+https://github.com/junclemente/jcds.git@v0.2.1[aws]
```

Installs:

- `boto3`
- `botocore`

---

### 📓 Auto-install in Jupyter Notebooks

If you're using `jcds` in a Jupyter notebook, add this snippet at the top of your notebook to automatically install it if it's not already present:
```python
import importlib
import subprocess
import sys

package_name = "jcds"
branch = "main"  # change to "develop" for latest dev version

if branch == "develop":
    print(f"Installing latest '{package_name}' from '{branch}' branch...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install",
        "--upgrade", "--force-reinstall",
        f"git+https://github.com/junclemente/jcds.git@{branch}",
    ])
elif importlib.util.find_spec(package_name) is None:
    print(f"'{package_name}' not found. Installing from GitHub...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install",
        f"git+https://github.com/junclemente/jcds.git@{branch}",
    ])
else:
    print(f"'{package_name}' is already installed.")

from jcds import eda as jeda
from jcds import reports as jrep
from jcds import transform as jtrf
from jcds import charts as jvis
```

> 💡 Set `branch = "develop"` to always pull the latest development version. Switch to `branch = "main"` or a version tag like `branch = "v0.3.0"` for stable use.

---

### 🌐 Import with `httpimport`

Use [`httpimport`](https://pypi.org/project/httpimport/) directly in Jupyter:

```python
import httpimport

with httpimport.github_repo('junclemente', 'jcds', ref='<branch>'):
    import jcds as jcds
```

You can also import specific submodules:

```python
import jcds.eda as eda
```

---

### 🧪 Minimal Usage Example

```python
import pandas as pd
import jcds.eda as jeda

df = pd.read_csv('data.csv')
```

---

### 📓 More Examples

See the EDA workflow notebook:

- [examples/eda_workflow.ipynb](./examples/eda_workflow.ipynb)

---

## 🌿 Branching Info

When specifying the `ref` in `httpimport.github_repo()`:

- `develop` – Actively evolving 🚧
- `0.x.x` – Stable and reproducible ✅

> 🔒 Recommended: Use a versioned tag for reproducibility.

---

## 🆘 Help System

Each subpackage has a built-in `help()` function.

### 🌍 Global help

```python
import jcds
jcds.help()
```

### 📁 Subpackage-specific help

```python
import jcds.eda
jcds.eda.help()

import jcds.aws as jaws
jaws.help()
```

### 🔎 Function-level help

```python
jcds.eda.help('dqr_cat')
```

---

## 🧪 Testing

This project uses `pytest`.

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_eda_helpers.py
```

Measure test coverage:

```bash
pytest --cov=jcds --cov-report=term
```

---

## 📚 Documentation

📄 [jcds documentation](https://junclemente.github.io/jcds)

Built with:

- [MkDocs](https://www.mkdocs.org/)
- [Material theme](https://squidfunk.github.io/mkdocs-material/)
- [mkdocstrings](https://mkdocstrings.github.io/)

### 🔁 Updating the Docs

1. **Update or Add Docstrings**
   - Use [NumPy](https://numpydoc.readthedocs.io/en/latest/format.html) or Google-style docstrings in your `.py` files.
   - These serve as the foundation for manual documentation or future automated doc generation.

2. **Edit Markdown Files**
   - Update existing `.md` files or create new ones in the `docs/` folder.
   - Update `mkdocs.yml` to reflect new pages or sections in the sidebar.

3. **Preview Locally**
   Run the following command to launch a local web server:

```bash
mkdocs serve
```

Then open the URL:

```text
http://127.0.0.1:8000/
```

4. Deploy to GitHub Pages:

```bash
mkdocs gh-deploy
```
This will:

Build the site

Push it to the gh-pages branch

Automatically publish at:
https://<your-username>.github.io/<repo-name>/

---

## 📝 Changelog

See [CHANGELOG.md](./CHANGELOG.md) for version history and updates.

---

### 📐 Commit Message Guide

This project follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specifications:


| Type       | Description                        | Example                                      |
|------------|------------------------------------|----------------------------------------------|
| `feat`     | New feature                        | `feat: add data_info report to jcds.reports` |
| `fix`      | Bug fix                            | `fix: handle NaN values in datetime parser`  |
| `chore`    | Maintenance                        | `chore: update Makefile for git-cliff`       |
| `docs`     | Documentation only                 | `docs: update README with usage examples`    |
| `style`    | Formatting, no logic change        | `style: reformat eda.py with black`          |
| `refactor` | Code refactor                      | `refactor: simplify logic in show_dupes()`   |
| `test`     | Add or update tests                | `test: add tests for aws.s3_io.read_s3()`    |
| `ci`       | CI/CD config changes               | `ci: update GitHub Actions workflow`         |

Used for consistent history and release tracking. 

---

## 🌿 Branch & Release Workflow

This project uses **squash merge** from `develop` → `main` to keep a clean commit history.

### After every PR merge into `main`:

After merging, reset `develop` to match `main`:
```bash
git checkout develop
git reset --hard origin/main
git push origin develop --force-with-lease
```

> ⚠️ This is required after every merge because squash merge creates a new commit on `main` that `develop` doesn't recognize.

### General flow:

1. Do all work on `develop`
2. Open PR: `develop` → `main`
3. Squash and merge
4. Reset `develop` to `main` (steps above)
5. Tag and publish release