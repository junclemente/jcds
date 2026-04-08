# Welcome to jcds 🧪

**jcds** is a modular Python library for data science workflows, built to save time
and reduce repetition in Jupyter notebooks.

It provides:
- 🔎 EDA tools for inspecting, profiling, and summarizing DataFrames
- 📊 Visualization via `jcds.charts` (`jvis`)
- 🔄 Data transformation via `jcds.transform` (`jtrf`)
- 🧹 Reports for data quality, cardinality, outliers, and missing data
- ☁️ Optional AWS integration for working with S3
- 🧪 160+ tests using `pytest`

---

## 🚀 Quick Start

### 1. Installation

Install the latest version directly from GitHub:
```bash
pip install git+https://github.com/junclemente/jcds.git
```

Or a specific version:
```bash
pip install git+https://github.com/junclemente/jcds.git@v0.3.2
```

Or with AWS extras:
```bash
pip install git+https://github.com/junclemente/jcds.git[aws]
```

### 2. Basic Example
```python
import pandas as pd
from jcds import eda as jeda
from jcds import reports as jrep
from jcds import transform as jtrf
from jcds import charts as jvis

df = pd.read_csv("your_dataset.csv")

# Clean column names
jtrf.clean_column_names(df, inplace=True)

# Understand your data
jrep.data_info(df)
jrep.data_quality(df)
jrep.data_cardinality(df)

# Visualize missing data and outliers
jvis.missing_data_heatmap(df)
jrep.outliers(df)
```

---

## 📚 Documentation

- [Getting Started](getting_started.md) — EDA workflow guide organized by phase
- [API Reference](api.md) — Full auto-generated function documentation
- [Changelog](changelog.md) — Version history and release notes