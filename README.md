# jcds Library

[![Latest Release](https://img.shields.io/github/v/release/junclemente/jcds?label=release)](https://github.com/junclemente/jcds/releases)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**jcds** is a personal collection of reusable functions for data science and analysis tasks.  
It’s designed to make your workflow faster and more consistent when working with data in Jupyter notebooks.

--- 
## How to Use

### Install with `pip`

This library can be installed with `pip` which will also install the required dependencies.  
To install the latest version, use the following command:

```bash
pip install git+https://github.com/junclemente/jcds.git
```

To install a specific version (e.g., `v0.2.1`), add the version tag at the end:

```bash
pip install git+https://github.com/junclemente/jcds.git@v0.2.1
```

Or install from the `develop` branch (not recommended):

```bash
pip install git+https://github.com/junclemente/jcds.git@develop
```

### Optional: AWS Support

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

## Branching Info

When specifying the `ref` in `httpimport.github_repo()`, use one of the following:

- `develop` - Actively evolving. This may contain breaking changes as new features are added or modified.
- Versioned tags (e.g., `0.1.0`, `0.2.0`) - Stable and locked. These will not change and are safe for reproducibility.

**Recommended:** Use a versioned branch to ensure your code doesn't break when updates are pushed to `develop`.

# help()

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

## Versions

See [CHANGELOG.md](./CHANGELOG.md) for a list of version history and updates.
