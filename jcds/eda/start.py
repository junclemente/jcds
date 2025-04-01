from IPython.display import Markdown, display

def eda_guide_markdown():
    md_text = """
# 🧭 EDA Guide Overview

Welcome to your Exploratory Data Analysis journey!  
Follow this structured checklist to deeply understand your dataset and prepare it for modeling.

---

## 📦 Step 0: Import the Data  
Load your dataset into a Pandas DataFrame. For example:  
```python
import pandas as pd
df = pd.read_csv("your_dataset.csv")" \
""" 








# ===========================================
# Inspect data structure

# Data clean:
# missing values
# duplicates
# correct datatypes
# outliers
# fix encoding issues 

# Univariate analysis:
# Numerical: 
# histograms
# KDE plots
# boxplots 

# Categorical:
# value counts
# bar plots

# Bivariate/Multivariate analysis:
# relationship between variables 
# target vs feature (classification vs regression)
# Correlation matrix, heatmaps, pairplots
# Crosstabs for categorical comparison

# Visualizations
