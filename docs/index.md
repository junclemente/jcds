# Welcome to jcds 🧪

**jcds** is a personal collection of reusable Python functions for data science workflows, built to save time and reduce repetition in Jupyter notebooks.

It provides:
- 🔎 Quick EDA tools (like `quick_report` and `long_report`)
- 📊 Helpers for working with categorical and continuous variables
- 🧹 Utilities for inspecting, cleaning, and summarizing data
- ☁️ Optional AWS integration for working with S3
- 🧪 Well-tested functions using `pytest`

---

## 🚀 Quick Start

### 1. Installation

Install the latest version directly from GitHub:

```bash
pip install git+https://github.com/junclemente/jcds.git
```

Or with AWS extras: 
```bash
pip install git+https://github.com/junclemente/jcds.git[aws]
``` 

## Basic Example
```python
import pandas as pd
import jcds.eda as eda 

df = pd.read_csv("your_dataset.csv")
duplicates = jeda.show_dupes(df)
print(duplicates)

unique_values_list = jeda.count_unique_values(df, ['col1', 'col2', 'col3'])
print(unique_values_list)

unique_values_column = jeda.count_unique_values(df, 'col')
print(unique_values_column)

```
Check out the [API Reference](api.md) to explore all available functions.
