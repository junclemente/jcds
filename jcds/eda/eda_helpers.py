import pandas as pd

# from IPython.display import Markdown, display

# def eda_guide_markdown():
#     md_text = """
# # 🧭 EDA Guide Overview

# Welcome to your Exploratory Data Analysis journey!
# Follow this structured checklist to deeply understand your dataset and prepare it for modeling.

# ---

# ## 📦 Step 0: Import the Data
# Load your dataset into a Pandas DataFrame. For example:
# ```python
# import pandas as pd
# df = pd.read_csv("your_dataset.csv")" \
# """


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


def show_shape(dataframe):
    return dataframe.shape


def show_dupes(dataframe):
    dupes = dataframe.duplicated()
    return dupes.sum()


def show_catvar(dataframe):
    cat_features = dataframe.select_dtypes(
        include=["category", "object"]
    ).columns.tolist()
    return cat_features


def show_convar(dataframe):
    cont_features = dataframe.select_dtypes(
        exclude=["category", "object"]
    ).columns.tolist()
    return cont_features


def show_lowcardvars(dataframe, max_unique=10):
    print(f"Showing cat var of cardinality <= {max_unique}")
    col_list = []
    cols = show_catvar(dataframe)
    for col in cols:
        count = dataframe[col].nunique()
        if count <= max_unique:
            col_list.append((col, count))
    return col_list


def count_rows_with_any_na(dataframe):
    return dataframe.isna().any(axis=1).sum()


def count_rows_with_all_na(dataframe):
    return dataframe.isna().all(axis=1).sum()


def count_cols_with_any_na(dataframe):
    return dataframe.isna().any(axis=0).sum()


def count_cols_with_all_na(dataframe):
    return dataframe.isna().all(axis=0).sum()


def count_total_na(dataframe):
    return dataframe.isna().sum().sum()


def count_unique_values(dataframe, columns):
    unique_counts = {}
    for col in columns:
        count = dataframe[col].nunique(dropna=False)
        unique_counts[col] = count
    return unique_counts
