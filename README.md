# jcds Library

**jcds** is a personal collection of reusable functions for data science and analysis tasks.  
It’s designed to make your workflow faster and more consistent when working with data in Jupyter notebooks.

## How to Use

You can import this library directly into your Jupyter notebook using [`httpimport`](https://pypi.org/project/httpimport/):

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
