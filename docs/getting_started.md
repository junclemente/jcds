# Getting Started

## Installation

Install directly from GitHub:
```bash
pip install git+https://github.com/junclemente/jcds.git
```

Or install a specific version:
```bash
pip install git+https://github.com/junclemente/jcds.git@v0.3.2
```

## Import Convention
```python
from jcds import eda as jeda
from jcds import reports as jrep
from jcds import transform as jtrf
from jcds import charts as jvis
```

---

## Phase 1: Understand Your Data

The first step in any EDA is getting a high-level summary of your dataset.
```python
# Shape, dtypes, duplicates, ID-like columns
jrep.data_info(df)

# Cardinality — binary, constant, low/high cardinality columns
jrep.data_cardinality(df)

# Missing values, near-constant, mixed types
jrep.data_quality(df)
```

Add `show_columns=True` to any report to include column lists in the output:
```python
jrep.data_info(df, show_columns=True)
```

---

## Phase 2: Find Problems

### Missing Data
```python
# Summary of missing values per column
jeda.show_missing_summary(df)

# Rows with any missing values
jeda.show_null_rows(df)

# Rows missing more than 50% of values
jeda.show_null_rows(df, threshold=0.5)

# Columns with any missing values
jeda.show_null_cols(df)

# Columns missing more than 80% of values
jeda.show_null_cols(df, threshold=0.8)

# Visual heatmap of missing data
jvis.missing_data_heatmap(df)
```

### Outliers
```python
# Outlier count and percentage per column
jeda.show_outlier_summary(df)

# Full outlier report with boxplot grid
jrep.outliers(df)

# Horizontal orientation
jrep.outliers(df, orient="h")
```

### Mixed Types & Column Issues
```python
# Columns with mixed data types
jeda.show_mixed_type_columns(df)

# Constant columns (zero variance)
jeda.show_constantvars(df)

# Near-constant columns (>95% same value)
jeda.show_nearconstvars(df)
```

---

## Phase 3: Clean Your Data

### Column Names
```python
# Standardize column names to snake_case
jtrf.clean_column_names(df, inplace=True)

# Rename a specific column
df = jtrf.rename_column(df, "old_name", "new_name")

# Drop columns
df = jtrf.delete_columns(df, ["col_a", "col_b"])
```

### Data Types
```python
# Convert to string (fixes mixed type columns)
df = jtrf.to_str(df, columns=["material"])

# Convert to integer
df = jtrf.to_int(df, columns=["quantity"])

# Convert to categorical
df = jtrf.to_categorical(df, columns=["region"])

# Convert to datetime
df = jtrf.to_datetime(df, columns=["created_on"])

# Convert to boolean
df = jtrf.to_bool(df, "is_active")
```

---

## Phase 4: Visualize

### Distributions
```python
# Histogram + KDE grid for all numeric columns (default)
jvis.hist_kde(df)

# Individual plots
jvis.hist_kde(df, grid=False)

# Specific columns only
jvis.hist_kde(df, columns=["std_cost", "total_foc_value"])

# Custom grid layout
jvis.hist_kde(df, ncols=2)
```

### Outliers
```python
# Boxplot grid (default)
jvis.outlier_boxplots(df)

# Horizontal orientation
jvis.outlier_boxplots(df, orient="h")

# Individual plots
jvis.outlier_boxplots(df, grid=False)
```

### Categorical
```python
# Bar chart for a categorical column
jvis.categorical_barplot(df["region"])
```

### Correlation
```python
# Correlation heatmap
jvis.correlation_heatmap(df)
```

---

## Phase 5: Reports

One-line reports that combine summary statistics and visuals:
```python
# Full outlier report — summary table + boxplot grid
jrep.outliers(df)

# Categorical variable report
jrep.catvar_report(df)

# Or for specific columns
jrep.catvar_report(df, columns=["region", "material_type"])
```

---

## Notebook Auto-Install Snippet

Use this at the top of any notebook to ensure jcds is always up to date:
```python
import importlib, subprocess, sys

package_name = "jcds"
branch = "main"  # or "develop" for latest

if branch == "develop":
    subprocess.check_call([sys.executable, "-m", "pip", "install",
        "--upgrade", "--force-reinstall",
        f"git+https://github.com/junclemente/jcds.git@{branch}"])
elif importlib.util.find_spec(package_name) is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install",
        f"git+https://github.com/junclemente/jcds.git@{branch}"])
else:
    print(f"'{package_name}' is already installed.")

from jcds import eda as jeda
from jcds import reports as jrep
from jcds import transform as jtrf
from jcds import charts as jvis
```