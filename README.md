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
pytest tests/unit/test_eda_helpers.py
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

1. Add/update docstrings (Google or NumPy style).
2. Update `mkdocs.yml` and related `.md` files.
3. Preview locally:

```bash
mkdocs serve
```

URL:

```text
http://127.0.0.1:8000/
```

4. Deploy to GitHub Pages:

```bash
mkdocs gh-deploy
```

---

## 📝 Changelog

See [CHANGELOG.md](./CHANGELOG.md) for version history and updates.

---

## 🚀 Release & Changelog Automation

This project uses [`git-cliff`](https://github.com/orhun/git-cliff) with [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) to generate structured changelogs.

### 📐 Commit Message Guide

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

> 📌 Only commits with these tags will be included in the changelog.

---

### 📂 Makefile Commands

- 🔍 Preview changelog:

  ```bash
  make changelog VERSION=0.2.5
  ```

- 💾 Save changelog to `CHANGELOG.md`:

  ```bash
  make changelog-save VERSION=0.2.5
  ```

- 🏷️ Finalize and tag a release:

  ```bash
  make release VERSION=0.2.5
  ```