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
    """
    Returns the shape (number of rows and columns) of the given DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.

    Returns:
    tuple: A tuple containing the number of rows and columns in the DataFrame.

    Docstring generated by ChatGPT.
    """
    return dataframe.shape


def show_dupes(dataframe):
    """
    Returns the number of duplicate rows in the given DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.

    Returns:
    int: The count of duplicated rows in the DataFrame.

    Docstring generated by ChatGPT.
    """
    dupes = dataframe.duplicated()
    return dupes.sum()


def show_catvar(dataframe):
    """
    Identifies and returns a list of categorical variables in the DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.

    Returns:
    list: A list of column names that have categorical or object data types.

    Docstring generated by ChatGPT.
    """
    cat_features = dataframe.select_dtypes(
        include=["category", "object"]
    ).columns.tolist()
    return cat_features


def show_convar(dataframe):
    """
    Identifies and returns a list of continuous (non-categorical) variables in the DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.

    Returns:
    list: A list of column names that are not of categorical or object data types.

    Docstring generated by ChatGPT.
    """
    cont_features = dataframe.select_dtypes(
        exclude=["category", "object"]
    ).columns.tolist()
    return cont_features


def show_lowcardvars(dataframe, max_unique=10):
    """
    Returns a list of categorical variables with unique values less than or equal to the specified threshold.

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.
    max_unique (int): The maximum number of unique values allowed for a variable to be considered low cardinality. Default is 10.

    Returns:
    list: A list of tuples where each tuple contains the column name and the number of unique values.

    Docstring generated by ChatGPT.
    """
    print(f"Showing cat var of cardinality <= {max_unique}")
    col_list = []
    cols = show_catvar(dataframe)
    for col in cols:
        count = dataframe[col].nunique()
        if count <= max_unique:
            col_list.append((col, count))
    return col_list


def show_binary_list(dataframe, dropna=True):
    """
    Identifies binary columns in a DataFrame, optionally considering missing values.

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.
    dropna (bool): If True, NaN values are excluded when determining binary columns. Default is True.

    Returns:
    dict: A dictionary with two keys:
        - "binary_columns": list of columns that contain exactly two unique non-null values.
        - "binary_with_nan": list of columns that have two unique non-null values and also include NaNs.

    Docstring generated by ChatGPT.
    """
    binary_cols = []
    binary_with_nan = []
    for col in dataframe.columns:
        unique_vals = dataframe[col].unique()
        unique_vals_no_nan = pd.Series(unique_vals).dropna().unique()

        if len(unique_vals_no_nan) == 2:
            if pd.isna(unique_vals).any():
                binary_with_nan.append(col)
            else:
                binary_cols.append(col)

    return {"binary_columns": binary_cols, "binary_with_nan": binary_with_nan}


def count_rows_with_any_na(dataframe):
    """
    Counts the number of rows in the DataFrame that contain at least one missing (NaN) value.

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.

    Returns:
    int: The number of rows with at least one NaN value.

    Docstring generated by ChatGPT.
    """
    return dataframe.isna().any(axis=1).sum()


def count_rows_with_all_na(dataframe):
    """
    Counts the number of rows in the DataFrame where all values are missing (NaN).

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.

    Returns:
    int: The number of rows where every column is NaN.

    Docstring generated by ChatGPT.
    """
    return dataframe.isna().all(axis=1).sum()


def count_cols_with_any_na(dataframe):
    """
    Counts the number of columns in the DataFrame that contain at least one missing (NaN) value.

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.

    Returns:
    int: The number of columns with at least one NaN value.

    Docstring generated by ChatGPT.
    """
    return dataframe.isna().any(axis=0).sum()


def count_cols_with_all_na(dataframe):
    """
    Counts the number of columns in the DataFrame where all values are missing (NaN).

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.

    Returns:
    int: The number of columns where every row is NaN.

    Docstring generated by ChatGPT.
    """
    return dataframe.isna().all(axis=0).sum()


def count_total_na(dataframe):
    """
    Calculates the total number of missing (NaN) values in the entire DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.

    Returns:
    int: The total count of NaN values in the DataFrame.

    Docstring generated by ChatGPT.
    """
    return dataframe.isna().sum().sum()


def count_unique_values(dataframe, columns):
    """
    Counts the number of unique values in the specified columns of a DataFrame, including NaNs.

    Parameters:
    dataframe (pd.DataFrame): The input pandas DataFrame.
    columns (list): A list of column names for which to count unique values.

    Returns:
    dict: A dictionary where each key is a column name and the value is the count of unique entries, including NaNs.

    Docstring generated by ChatGPT.
    """
    unique_counts = {}
    for col in columns:
        count = dataframe[col].nunique(dropna=False)
        unique_counts[col] = count
    return unique_counts
