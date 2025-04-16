import pandas as pd
import pandas.api.types as ptypes

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


def show_memory_use(dataframe):
    """
    Returns memory usage of the dataframe in megabytes (MB)
    """
    memory_usage = dataframe.memory_usage(deep=True).sum()
    # convert from bytes to megabytes
    memory_usage = memory_usage / 1024**2
    return float(memory_usage)


def show_shape(dataframe):
    """
    Return the shape (number of rows and columns) of the given DataFrame.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.

    Returns
    -------
    tuple of int
        A tuple containing the number of rows and columns in the DataFrame.

    """
    return dataframe.shape


def show_dupes(dataframe):
    """
    Return the number of duplicate rows in the given DataFrame.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.

    Returns
    -------
    int
        The count of duplicated rows in the DataFrame.

    """
    dupes = dataframe.duplicated()
    return dupes.sum()


def show_catvar(dataframe):
    """
    Identify and return a list of categorical variables in the DataFrame.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.

    Returns
    -------
    list of str
        A list of column names that have categorical or object data types.

    """
    cat_features = dataframe.select_dtypes(
        include=["category", "object"]
    ).columns.tolist()
    return cat_features


def show_convar(dataframe):
    """
    Identify and return a list of continuous (non-categorical) variables in the DataFrame.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.

    Returns
    -------
    list of str
        A list of column names that are not of categorical or object data types.

    """

    cont_features = dataframe.select_dtypes(
        exclude=["category", "object"]
    ).columns.tolist()
    return cont_features


def show_lowcardvars(dataframe, max_unique=10, verbose=False):
    """
    Return a list of categorical variables with unique values less than or equal to the specified threshold.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.
    max_unique : int, optional
        The maximum number of unique values allowed for a variable to be considered low cardinality. Default is 10.
    verbose : bool, optional
        Whether to print a summary message (default is False).
    Returns
    -------
    list of tuple
        A list of tuples where each tuple contains the column name and the number of unique values.

    """
    if verbose:
        print(f"Categorical variables with cardinality <= {max_unique}")
    col_list = []
    cols = show_catvar(dataframe)
    for col in cols:
        count = dataframe[col].nunique()
        if count <= max_unique:
            col_list.append((col, count))
    return col_list


def show_constantvars(dataframe, verbose=False):
    """
    Identify columns with only one unique value (including NaNs).

    Parameters
    ----------
    dataframe : pd.DataFrame
    verbose : bool, optional
        Whether to print a summary message (default is False).
    Returns
    -------
    list of str
        Column names that are constant.
    """
    if verbose:
        print("Columns (only one unique value)")
    col_list = []
    for col in dataframe.columns:
        if dataframe[col].nunique(dropna=False) == 1:
            col_list.append(col)
    return col_list


def show_nearconstvars(dataframe, threshold=0.95, verbose=False):
    """
    Finds columns where a single value makes up more than `threshold` proportion of the data.

    Parameters
    ----------
    df : pd.DataFrame
        The input dataframe.
    threshold : float, optional
        The proportion above which a column is considered near-constant (default is 0.95).
    verbose : bool, optional
        Whether to print a summary message (default is False).

    Returns
    -------
    List[str]
        List of column names that are near-constant.
    """
    if verbose:
        print(f"Columns with cardinality <= {threshold*100:.1f}% ")

    near_constant = []
    for col in dataframe.columns:
        top_freq = dataframe[col].value_counts(normalize=True, dropna=False).values[0]
        if top_freq >= threshold:
            near_constant.append(col)

    return near_constant


def show_highcardvars(dataframe, percent_unique=90, verbose=False):
    """
    Identify categorical columns with high cardinality (>= percent_unique).

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame.
    percent_unique : float, optional
        Minimum % of unique values (vs. total rows) to consider high-cardinality.
    verbose : bool, optional
        Whether to print a summary message (default is False).
    Returns
    -------
    list of tuples
        List of (column name, percent unique) tuples.

    Docstring generated with assistance from ChatGPT.
    """
    if verbose:
        print(f"Cateogrical variables with cardinality >= {percent_unique}%")

    col_list = []
    total_rows = show_shape(dataframe)[0]
    cat_cols = show_catvar(dataframe)
    for col in cat_cols:
        count = dataframe[col].nunique()
        percent = (count / total_rows) * 100
        if percent >= percent_unique:
            col_list.append((col, percent))
    return col_list


def show_binary_list(dataframe, dropna=True):
    """
    Identify binary columns in a DataFrame, optionally considering missing values.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.
    dropna : bool, optional
        If True, NaN values are excluded when determining binary columns. Default is True.

    Returns
    -------
    dict
        A dictionary with two keys:
            - "binary_columns": list of column names that contain exactly two unique non-null values.
            - "binary_with_nan": list of column names that have two unique non-null values and also include NaNs.

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
    Count the number of rows in the DataFrame that contain at least one missing (NaN) value.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.

    Returns
    -------
    int
        The number of rows with at least one NaN value.

    """

    return dataframe.isna().any(axis=1).sum()


def count_rows_with_all_na(dataframe):
    """
    Count the number of rows in the DataFrame where all values are missing (NaN).

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.

    Returns
    -------
    int
        The number of rows where every column is NaN.

    """

    return dataframe.isna().all(axis=1).sum()


def count_cols_with_any_na(dataframe):
    """
    Count the number of columns in the DataFrame that contain at least one missing (NaN) value.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.

    Returns
    -------
    int
        The number of columns with at least one NaN value.

    """

    return dataframe.isna().any(axis=0).sum()


def count_cols_with_all_na(dataframe):
    """
    Count the number of columns in the DataFrame where all values are missing (NaN).

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.

    Returns
    -------
    int
        The number of columns where every row is NaN.

    """

    return dataframe.isna().all(axis=0).sum()


def count_total_na(dataframe):
    """
    Calculate the total number of missing (NaN) values in the entire DataFrame.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.

    Returns
    -------
    int
        The total count of NaN values in the DataFrame.

    """

    return dataframe.isna().sum().sum()


def count_unique_values(dataframe, columns):
    """
    Count the number of unique values in the specified columns of a DataFrame, including NaNs.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.
    columns : list of str
        A list of column names for which to count unique values.

    Returns
    -------
    dict
        A dictionary where each key is a column name and the value is the count of unique entries, including NaNs.

    """

    unique_counts = {}
    for col in columns:
        count = dataframe[col].nunique(dropna=False)
        unique_counts[col] = count
    return unique_counts


def show_datetime_columns(dataframe):
    """
    Identify columns with datetime-like data types.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame.

    Returns
    -------
    list of str
        A list of column names whose dtype is datetime64[ns] or similar.
    """
    dt_cols = []
    for col in dataframe.columns:
        col_dtype = dataframe[col].dtype
        if pd.api.types.is_datetime64_any_dtype(col_dtype):
            dt_cols.append(col)
    return dt_cols


def show_possible_datetime_columns(dataframe, sample_size=5):
    """
    Identify object columns that may contain datetime-like strings.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame.
    sample_size : int
        Number of values to sample for date parsing test.

    Returns
    -------
    list of str
        Columns that appear to contain datetime-like strings.
    """
    possible_date_cols = []

    for col in dataframe.select_dtypes(include="object").columns:
        sample_values = dataframe[col].dropna().head(sample_size)
        parse_attempts = sample_values.apply(
            lambda x: pd.to_datetime(x, errors="coerce")
        )
        success_ratio = parse_attempts.notna().mean()
        if success_ratio >= 0.8:  # 80% of values parse as dates
            possible_date_cols.append(col)

    return possible_date_cols


def show_mixed_type_columns(df):
    mixed_cols = []
    for col in df.columns:
        types = df[col].map(type).nunique()
        if types > 1:
            mixed_cols.append(col)
    return mixed_cols


def count_id_like_columns(dataframe, threshold=0.95):
    """
    Count number of columns with high uniqueness (e.g., IDs).
    """
    total_rows = show_shape(dataframe)[0]
    return sum(
        dataframe[col].nunique() / total_rows >= threshold for col in dataframe.columns
    )


def get_dtype_summary(dataframe):
    """
    Returns a dictionary summarizing the count of common data types.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame.

    Returns
    -------
    dict
        Keys are data types (as strings), values are column counts.
    """
    type_counts = {
        "object": 0,
        "int": 0,
        "float": 0,
        "bool": 0,
        "category": 0,
        "datetime": 0,
        "other": 0,
    }

    for col in dataframe.columns:
        dtype = dataframe[col].dtype

        if ptypes.is_bool_dtype(dtype):
            type_counts["bool"] += 1
        elif ptypes.is_integer_dtype(dtype):
            type_counts["int"] += 1
        elif ptypes.is_float_dtype(dtype):
            type_counts["float"] += 1
        elif isinstance(dtype, pd.CategoricalDtype):
            type_counts["category"] += 1
        elif ptypes.is_datetime64_any_dtype(dtype):
            type_counts["datetime"] += 1
        elif ptypes.is_object_dtype(dtype):
            type_counts["object"] += 1
        else:
            type_counts["other"] += 1

    return type_counts


def show_missing_summary(dataframe, sort=True, threshold=0.0):
    """
    Summarize missing values in the DataFrame.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame.
    sort : bool, optional
        If True, sorts the result by descending missing count. Default is True.
    threshold : float, optional
        Minimum percentage (0–100) of missing values to include a column. Default is 0.0.

    Returns
    -------
    dict
        A dictionary where keys are column names and values are tuples of
        (missing count, percent missing), filtered by the threshold.
    """
    null_counts = dataframe.isnull().sum()
    null_counts = null_counts[null_counts > 0]
    total_rows = len(dataframe)

    summary = {}
    for col, count in null_counts.items():
        pct = (count / total_rows) * 100
        if pct >= threshold:
            summary[col] = (int(count), round(pct, 1))

    if sort:
        summary = dict(sorted(summary.items(), key=lambda x: x[1][0], reverse=True))

    return summary
