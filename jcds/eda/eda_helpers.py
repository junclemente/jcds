import pandas as pd
from jcds.utils import print_code_line

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


# def show_dtypes(dataframe):
#     # Get features not labeled as categorical
#     cat_features = dataframe.select_dtypes(
#         include=["category", "object"]
#     ).columns.tolist()
#     # Get features labeled as categorical
#     cont_features = dataframe.select_dtypes(
#         exclude=["category", "object"]
#     ).columns.tolist()
#     return


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
            col_list.append(col)
    return col_list
