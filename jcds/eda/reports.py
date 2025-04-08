import pandas as pd
import numpy as np

from jcds.utils import deprecated


def dqr_cont(dataframe):
    """
    Generate a data quality report for continuous features in a given DataFrame.

    This function calculates and prints the following metrics for each feature in the provided list:
    - Total count of non-missing values
    - Total count of missing values
    - Percentage of missing values
    - Cardinality (number of unique values)
    - Descriptive statistics (mean, standard deviation, min, max)

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame containing the data to be analyzed.
    list_of_features : list of str
        The list of column names (features) for which the data quality report is generated.

    Returns
    -------
    None
        This function prints the data quality report to the console.

    Docstring generated with assistance from ChatGPT.
    """

    # Initialize variables
    round_to = 2
    list_feature_name = []
    list_count = []
    list_missing = []
    list_percent = []
    list_cardinality = []

    # Create list of non-categorical values
    list_of_features = dataframe.select_dtypes(
        exclude=["category", "object"]
    ).columns.tolist()

    # Total rows
    total_rows = dataframe.shape[0]

    if len(list_of_features) == 0:
        print("This dataset does not have any non-categorical features.")
        return

    print("The non-categorical features are: ")
    print(list_of_features)

    for feature in list_of_features:
        # Get stats for each feature
        total_count = dataframe[feature].count()
        total_missing = dataframe[feature].isnull().sum()
        percent_missing = total_missing / total_rows * 100
        cardinality = len(dataframe[feature].unique())

        # Append result to variables
        list_feature_name.append(feature)
        list_count.append(total_count)
        list_missing.append(total_missing)
        list_percent.append(np.round(percent_missing, round_to))
        list_cardinality.append(cardinality)

    # Create dataframe
    data = {
        "Feature": list_feature_name,
        "Count": list_count,
        "Missing": list_missing,
        "% missing": list_percent,
        "Cardinality": list_cardinality,
    }
    df = pd.DataFrame(data)

    # Get descriptive statistics and transpose
    stats = np.round(dataframe[list_of_features].describe(), round_to)
    transposed_stats = stats.T

    # Print results
    print("Data Quality for Continous Features")
    print(f"Total Features: {len(list_of_features)} / {total_rows} rows")
    display(df)

    print("\n")
    print("Descriptive Stats")
    display(transposed_stats)

    return


def dqr_cat(dataframe):
    """
    Generate a data quality report for categorical features in a given DataFrame.

    This function calculates and prints the following metrics for each feature in the provided list:
    - Total count of non-missing values
    - Total count of missing values
    - Percentage of missing values
    - Cardinality (number of unique values)
    - Mode 1 (most frequent value), its frequency, and percentage
    - Mode 2 (second most frequent value), its frequency, and percentage
    - Descriptive statistics for each feature

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame containing the data to be analyzed.
    list_of_features : list of str
        The list of column names (features) for which the data quality report is generated.

    Returns
    -------
    None
        This function prints the data quality report to the console.

    Docstring generated with assistance from ChatGPT.
    """

    # Initialize variables
    round_to = 2
    list_feature_name = []
    list_count = []
    list_missing = []
    list_percent = []
    list_cardinality = []
    list_mode1 = []
    list_mode1_freq = []
    list_mode1_perc = []
    list_mode2 = []
    list_mode2_freq = []
    list_mode2_perc = []

    # Create list of non-categorical values
    list_of_features = dataframe.select_dtypes(
        include=["category", "object"]
    ).columns.tolist()

    # Total rows
    total_rows = dataframe.shape[0]

    if len(list_of_features) == 0:
        print("This dataset does not have any categorical columns.")
        return

    print("The categorical features are: ")
    print(list_of_features)

    for feature in list_of_features:

        total_count = dataframe[feature].count()
        total_missing = dataframe[feature].isnull().sum()
        percent_missing = np.round(total_missing / total_rows * 100, round_to)
        cardinality = len(dataframe[feature].unique())

        # Use value counts to get modes
        results = dataframe[feature].value_counts()
        # Calculate mode
        mode1_name = results.index[0]
        mode1_count = results.iloc[0]
        mode1_percent = np.round((mode1_count / total_count) * 100, round_to)

        # Initialize mode 2 variables
        mode2_name = None
        mode2_count = 0
        mode2_percent = 0.0

        # Calculate 2nd mode if it exists
        if len(results) > 1:
            mode2_name = results.index[1]
            mode2_count = results.iloc[1]
            mode2_percent = np.round((mode2_count / total_count) * 100, round_to)

        # Append results to lists
        list_feature_name.append(feature)
        list_count.append(total_count)
        list_missing.append(total_missing)
        list_percent.append(percent_missing)
        list_cardinality.append(cardinality)
        list_mode1.append(mode1_name)
        list_mode1_freq.append(mode1_count)
        list_mode1_perc.append(mode1_percent)
        list_mode2.append(mode2_name)
        list_mode2_freq.append(mode2_count)
        list_mode2_perc.append(mode2_percent)

    # Create dataframes
    data = {
        "Feature": list_feature_name,
        "Count": list_count,
        "Missing": list_missing,
        "% Missing": list_percent,
        "Cardinality": list_cardinality,
    }

    data_mode1 = {
        "Feature": list_feature_name,
        "Mode 1": list_mode1,
        "Mode 1 Freq.": list_mode1_freq,
        "Mode 1 %": list_mode1_perc,
    }

    data_mode2 = {
        "Feature": list_feature_name,
        "Mode 2": list_mode2,
        "Mode 2 Freq.": list_mode2_freq,
        "Mode 2 %": list_mode2_perc,
    }

    df = pd.DataFrame(data)
    df1 = pd.DataFrame(data_mode1)
    df2 = pd.DataFrame(data_mode2)

    # Get descriptive statistics and transpose
    stats = dataframe[list_of_features].describe(include="object")
    transposed_stats = stats.T

    # Print results
    print("Data Quality Report for Categorical Features")
    print(f"Total features: {len(list_of_features)} / {total_rows} rows")
    print("============================================")
    print("Stats")
    print("-----")
    display(df)

    print("\n")
    print("Mode 1")
    print("------")
    display(df1)

    print("\n")
    print("Mode 2")
    print("------")
    display(df2)

    print("\n")
    print("Descriptive Stats")
    print("-----------------")
    display(transposed_stats)

    return


@deprecated(
    reason="This will be replaced with a new function.",
    version="0.3.0",
)
def quick_report(dataframe):
    """
    Generate a quick summary report of a pandas DataFrame, including shape, missing value statistics, and memory usage.

    This function prints:
    - Total number of columns and rows
    - Number and percentage of rows that are entirely missing
    - Number and percentage of columns that have any missing values
    - Total number of missing values in the dataset
    - Output of `DataFrame.info()` with memory usage (`deep=True`)

    Notes
    -----
    - Categorical and continuous feature identification is performed but not displayed.
    - Missing value calculations are rounded to two decimal places.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame to analyze.

    Returns
    -------
    None
        This function prints the summary report to the console.

    Docstring generated with assistance from ChatGPT.
    """

    ROUND = 2
    # Get features not labeled as categorical
    cat_features = dataframe.select_dtypes(
        include=["category", "object"]
    ).columns.tolist()
    # Get features labeled as categorical
    cont_features = dataframe.select_dtypes(
        exclude=["category", "object"]
    ).columns.tolist()
    # Get shape, total rows and cols
    total_rows = dataframe.shape[0]
    total_cols = dataframe.shape[1]
    # Count/% rows that are missing values
    rows_with_all_na = dataframe.isna().all(axis=1).sum()
    percent_na_rows = np.round(rows_with_all_na / total_rows * 100, ROUND)
    # Count/% cols that are missing values
    cols_with_na = dataframe.isna().any(axis=0).sum()
    percent_na_cols = np.round(cols_with_na / total_cols * 100, ROUND)
    total_na = dataframe.isna().sum().sum()

    print("============================================")
    print("Quick Report - info(memory_usage='deep')")
    print(f"Total cols: {total_cols}")
    print(f"Rows missing all values: {rows_with_all_na} ({percent_na_rows}%)")
    print(f"Total Rows: {total_rows}")
    print(f"Cols with missing values: {cols_with_na} ({percent_na_cols}%)")
    print(f"Total missing values in dataset: {total_na}")
    print("============================================")


@deprecated(
    reason="This will be replaced with a new function.",
    version="0.3.0",
)
def long_report(dataframe):
    """
    Generate a detailed summary report of a pandas DataFrame, including shape, missing value statistics,
    and a breakdown of categorical and continuous features with their unique value counts.

    This function prints:
    - Total number of columns and rows
    - Number and percentage of rows that are entirely missing
    - Number and percentage of columns with any missing values
    - Total number of missing values in the dataset
    - Count of categorical and continuous features
    - For each categorical and continuous feature: number of unique values

    Notes
    -----
    - Categorical features are detected based on 'object' and 'category' dtypes.
    - Continuous features include all other non-categorical dtypes.
    - Missing value percentages are rounded to two decimal places.
    - A placeholder for `.info(memory_usage='deep')` is printed but not executed.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame to analyze.

    Returns
    -------
    None
        This function prints the detailed summary report to the console.

    Docstring generated with assistance from ChatGPT.
    """

    ROUND = 2
    # Get features not labeled as categorical
    cat_features = dataframe.select_dtypes(
        include=["category", "object"]
    ).columns.tolist()
    # Get features labeled as categorical
    cont_features = dataframe.select_dtypes(
        exclude=["category", "object"]
    ).columns.tolist()
    # Get shape, total rows and cols
    total_rows = dataframe.shape[0]
    total_cols = dataframe.shape[1]
    # Count/% rows that are missing values
    rows_with_all_na = dataframe.isna().all(axis=1).sum()
    percent_na_rows = np.round(rows_with_all_na / total_rows * 100, ROUND)
    # Count/% cols that are missing values
    cols_with_na = dataframe.isna().any(axis=0).sum()
    percent_na_cols = np.round(cols_with_na / total_cols * 100, ROUND)
    total_na = dataframe.isna().sum().sum()

    print("============================================")
    print("Quick Report - info(memory_usage='deep')")
    print(f"Total cols: {total_cols}")
    print(f"Rows missing all values: {rows_with_all_na} ({percent_na_rows}%)")
    print(f"Total Rows: {total_rows}")
    print(f"Cols with missing values: {cols_with_na} ({percent_na_cols}%)")
    print(f"Total missing values in dataset: {total_na}")
    print("============================================")
    print(f"Categorical features: {len(cat_features)}")
    for cat in cat_features:
        num_unique = dataframe[cat].unique()
        print(f"- {cat}: {len(num_unique)} unique values")
    print("============================================")
    print(f"Continuous features: {len(cont_features)}")
    for cont in cont_features:
        num_unique = dataframe[cont].unique()
        print(f"- {cont}: {len(num_unique)} unique values")

    # info = dataframe.info(memory_usage='deep')
    # display(info)
    return


def display_all_col_head(dataframe, head=5):
    """
    Display the first few rows of a DataFrame with all columns visible.

    Temporarily adjusts the pandas display settings to ensure all columns are shown, regardless of the total number,
    and uses IPython's `display()` function for clean notebook output.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The DataFrame to display.
    head : int, optional
        The number of rows to show from the top of the DataFrame. Defaults to 5.

    Notes
    -----
    - Temporarily sets the pandas display option to show all columns.
    - Uses IPython's `display()` function for cleaner notebook output.

    Returns
    -------
    None
        This function prints to the notebook interface and does not return a value.

    Docstring generated with assistance from ChatGPT.
    """

    with pd.option_context("display.max_columns", None):
        display(dataframe.head(head))

    return
