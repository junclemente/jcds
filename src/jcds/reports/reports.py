import pandas as pd

# from IPython.display import display, HTML
from tabulate import tabulate

from jcds.eda import (
    show_memory_use,
    show_shape,
    show_dimensions,
    show_dupes,
    show_convar,
    show_catvar,
    show_binary_list,
    show_lowcardvars,
    show_constantvars,
    show_nearconstvars,
    show_highcardvars,
    show_datetime_columns,
    show_possible_datetime_columns,
    get_dtype_summary,
    show_mixed_type_columns,
    count_id_like_columns,
    show_missing_summary,
    count_rows_with_any_na,
    count_rows_with_all_na,
    count_total_na,
    count_unique_values,
)

# from jcds.utils.formatting import render_html_block


def data_info(dataframe, show_columns=True):
    """
    Summarize the dataset's shape, memory usage, duplicates, and variable types.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The input dataset.

    show_columns : bool, optional
        Whether to display the list of columns in each category.

    Returns
    -------
    None
        Prints summary information to the console.
    """
    # Threshold constants
    ID_LIKE_COLS_THRESHOLD = 0.95

    print("\nSHAPE:")
    memory_use = show_memory_use(dataframe)
    shape = show_shape(dataframe)
    print(f"There are {shape[0]} rows and {shape[1]} columns ({memory_use:.2f} MB).")

    print("\nDUPLICATES:")
    dupes = show_dupes(dataframe)
    print(f"There are {dupes} duplicated rows.")

    print("\nCOLUMNS/VARIABLES:")

    print("Column dType Summary:")
    dtype_summary = get_dtype_summary(dataframe)
    for key, value in dtype_summary.items():
        if value > 0:
            print(f" * {key}: {value}")

    convar = show_convar(dataframe)
    print(f"There are {len(convar)} numerical (int/float/bool) variables.")
    if show_columns:
        print(f" * Columns: {convar}")

    catvar = show_catvar(dataframe)
    print(f"There are {len(catvar)} categorical (nominal/ordinal) variables.")
    if show_columns:
        print(f" * Columns: {catvar}")

    print("\nDATETIME COLUMNS:")
    dt_cols = show_datetime_columns(dataframe)
    possible_dt_cols = show_possible_datetime_columns(dataframe)
    print(
        f"There are {len(dt_cols)} datetime variables and {len(possible_dt_cols)} possible datetime variables."
    )

    print("\nOTHER COLUMN/VARIABLE INFO:")
    id_like_columns = count_id_like_columns(dataframe, threshold=ID_LIKE_COLS_THRESHOLD)
    print(
        f"ID Like Columns (threshold = {ID_LIKE_COLS_THRESHOLD * 100}%): {id_like_columns}"
    )

    mixed_columns = show_mixed_type_columns(dataframe)
    print(f"Columns with mixed datatypes: {len(mixed_columns)}")
    if show_columns:
        print(f" * Columns: {mixed_columns}")


def data_cardinality(dataframe, show_columns=True):
    """
    Summarizes the cardinality of the columns in the dataset.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The input dataset.

    show_columns : bool, optional
        Whether to display the list of columns in each category.

    Returns
    -------
    None
        Prints summary information to the console.
    """
    # Threshold constants
    NEAR_CONST_THRESHOLD = 0.95
    LOW_CARD_MAX_UNIQUE = 10
    HIGH_CARD_PERCENT_UNIQUE = 90

    print("CARDINALITY REPORT")

    shape = show_shape(dataframe)
    print(f"\nTotal columns analyzed: {shape[1]}")

    print("\n[BINARY COLUMNS]")
    binary_list = show_binary_list(dataframe)
    for key, value in binary_list.items():
        total = len(value)
        print(f"There are {total} {key.replace('_', ' ')}.")
        if show_columns:
            if total > 0:
                print(f" * Columns: {value}")

    print("\n[CONSTANT/NEAR CONSTANT COLUMNS]")
    const_var = show_constantvars(dataframe)
    print(f"There are {len(const_var)} constant columns.")
    if show_columns:
        if len(const_var) > 0:
            print(f" * Columns: {const_var}")

    near_constvar = show_nearconstvars(
        dataframe, threshold=NEAR_CONST_THRESHOLD, verbose=False
    )
    print(
        f"There are {len(near_constvar)} near-constant columns with >= {NEAR_CONST_THRESHOLD * 100:.0f}% of values being the same."
    )
    if show_columns:
        if len(near_constvar) > 0:
            print(f" * Columns: {near_constvar}")

    print("\n[LOW CARDINALITY CATEGORICAL COLUMNS]")
    lowcardvars = show_lowcardvars(
        dataframe, max_unique=LOW_CARD_MAX_UNIQUE, verbose=False
    )
    print(
        f" * There are {len(lowcardvars)} low cardinality columns with <= {LOW_CARD_MAX_UNIQUE} unique values."
    )
    if show_columns:
        print("Columns:")
        for col, n in lowcardvars:
            print(f" * {col}: {n} unique values")

    print("\n[HIGH CARDINALITY CATEGORICAL COLUMNS]")
    highcardvars = show_highcardvars(
        dataframe, percent_unique=HIGH_CARD_PERCENT_UNIQUE, verbose=False
    )
    print(
        f" * There are {len(highcardvars)} high cardinality variables with >={HIGH_CARD_PERCENT_UNIQUE}% unique values."
    )
    if show_columns:
        if len(highcardvars) > 0:
            print(f" * Columns: {highcardvars}")


def data_quality(dataframe, show_columns=True):
    """
    Print a comprehensive data quality report for the given DataFrame.

    This function summarizes key structural and content-based diagnostics to assess
    the cleanliness, consistency, and usability of a dataset. It includes checks for:

    - Overall shape and memory usage
    - Missing values (total, per row, and per column)
    - Duplicate rows
    - Constant and near-constant columns
    - Mixed data types within columns
    - High-cardinality categorical columns

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The input dataset to evaluate.

    show_columns : bool, optional (default=False)
        If True, prints the list of columns associated with each quality issue (e.g. columns with missing values, constants).

    Returns
    -------
    None
        Outputs the report directly to the console.
    """
    NEAR_CONSTANT_COLUMNS_THRESHOLD = 0.95
    HIGH_CARDINALITY_PERCENT = 60
    print("DATA QUALITY REPORT")
    print("====================")

    # shape
    rows, cols, dataframe_size, memory_usage = show_dimensions(dataframe)
    print(f"\n * Total entries (rows * cols): {dataframe_size}")
    print(f" * Memory usage: {memory_usage} MB")
    print(f" * Rows: {rows}")
    print(f" * Columns: {cols}")

    # missing data summary
    print("\nMISSING DATA:")

    total_missing = count_total_na(dataframe)
    print(
        f" * Total entries: {total_missing} missing ({(total_missing / dataframe_size) * 100:.1f}%)"
    )

    # missing rows
    print("\nROWS:")
    print("----------")
    rows_missing_any = count_rows_with_any_na(dataframe)
    rows_missing_all = count_rows_with_all_na(dataframe)
    print(f" * Rows missing any: {rows_missing_any}")
    print(f" * Rows missing all: {rows_missing_all}")

    # duplicate rows
    duplicates = show_dupes(dataframe)
    print(f"\nDUPLICATES: {duplicates}")

    # missing columns
    print("\nCOLUMNS:")
    print("----------------")
    missing_summary = show_missing_summary(dataframe, sort=True, threshold=0.0)
    key_list = list(missing_summary.keys())
    print(f"Columns missing any: {len(missing_summary)}")
    if show_columns and missing_summary:
        for key, value in missing_summary.items():
            print(f"\t'{key}': {value[0]} missing ({value[1]:.1f}%)")
        print(f"Column list: {key_list}")

    # constant columns
    constant_cols = show_constantvars(dataframe)
    print(f"\nCONSTANT: {len(constant_cols)}")
    if show_columns and constant_cols:
        print(f"Column list: {constant_cols}")

    # near constant columns
    near_constant_columns = show_nearconstvars(
        dataframe, threshold=NEAR_CONSTANT_COLUMNS_THRESHOLD, verbose=False
    )
    print(f"\nNEAR CONSTANT: {len(near_constant_columns)}")
    print(f"\t({NEAR_CONSTANT_COLUMNS_THRESHOLD * 100:.0f}% of values are the same)")
    if show_columns and near_constant_columns:
        print(f"\tColumn list: {near_constant_columns}")

    # mixed data types
    mixed_data_columns = show_mixed_type_columns(dataframe)
    print(f"\nMIXED DATATYPES: {len(mixed_data_columns)}")
    if show_columns and mixed_data_columns:
        print(f"\tColumn list: {mixed_data_columns}")

    # high cardinality
    high_card_columns = show_highcardvars(
        dataframe, percent_unique=HIGH_CARDINALITY_PERCENT, verbose=False
    )
    print(f"\nHIGH CARDINALITY: {len(high_card_columns)}")
    print(f"\t({HIGH_CARDINALITY_PERCENT}% >= unique values)")
    if show_columns and high_card_columns:
        for col in high_card_columns:
            print(f"\t* '{col[0]}': {col[1]:.1f}%")

    # outlier detection?


def catvar_report(dataframe, columns=None):
    """
    Display a summary report for categorical variables in a DataFrame.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame to analyze.
    columns : str or list of str or None, optional
        Name of a single categorical column (str), a list of column names (list of str),
        or None to report on all detected categorical columns. Default is None.

    Returns
    -------
    pandas.DataFrame or None
        - If no valid categorical columns are selected, returns an empty DataFrame.
        - Otherwise, prints a report for each column and returns None.

    Notes
    -----
    - Detects categorical columns via `show_catvar(dataframe)`.
    - Computes missing-value stats with `show_missing_summary(dataframe, sort=False, threshold=0.0)`.
    - Computes unique counts and top two modes via `count_unique_values(dataframe, col)`.
    - The report includes, for each column:
        • Non-missing count and missing count (%).
        • Cardinality (number of unique values).
        • Top two modes with their frequencies and percentage of non-missing.
    - Docstring generated with assistance from ChatGPT
    """
    categorical_columns = show_catvar(dataframe)
    columns_missing_values = show_missing_summary(dataframe, sort=False, threshold=0.0)

    if isinstance(columns, str):
        cols = [columns]
    elif isinstance(columns, list):
        cols = columns
    else:
        cols = categorical_columns

    # validate columns
    valid_columns = []
    for c in cols:
        if c in categorical_columns:
            valid_columns.append(c)
    if not valid_columns:
        print("No valid categorical columns selected.")
        return pd.DataFrame()

    total_rows = len(dataframe)

    for col in valid_columns:

        missing_count, pct_missing = columns_missing_values.get(col, (0, 0.0))
        # Calculate non_missing values
        non_missing = total_rows - missing_count
        unique_values = count_unique_values(dataframe, col)
        unique_count = unique_values[col]["unique_count"]
        mode1 = unique_values[col]["top_modes"][0]
        freq1 = mode1[1]
        pct_freq1 = round(mode1[1] / non_missing * 100, 1)
        mode2 = unique_values[col]["top_modes"][1]
        freq2 = mode2[1]
        pct_freq2 = round(mode2[1] / non_missing * 100, 1)

        print(f"\nFeature: '{col}'")
        print(f"===================================================================")
        print(
            f"Total: {non_missing}\t\t\tMissing: {missing_count} ({pct_missing*100}%)\t\t\tCardinality (Unique Values): {unique_count}"
        )
        print(f"Mode 1: {mode1[0]} \t\tFrequency: {freq1} ({pct_freq1}%)")
        print(f"Mode 2: {mode2[0]} \t\tFequency: {freq2} ({pct_freq2}%)")

    print(f"\nTotal rows: {total_rows}")


def outliers(
    dataframe,
    threshold=1.5,
    orient="v",
    export_func=None,
    export_prefix="outlier_report",
):
    """
    Print an outlier summary table and display a boxplot grid for all numeric columns.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The input dataset.
    threshold : float, optional
        IQR multiplier to define outliers. Default is 1.5.
    export_func : callable, optional
        Function to export the boxplot grid e.g. export_fig(fig, filename).
    export_prefix : str, optional
        Prefix for the exported filename. Default is 'outlier_report'.

    Returns
    -------
    None
        Prints summary and renders boxplot grid.
    """
    from jcds.eda import show_outlier_summary
    from jcds.charts import outlier_boxplots

    print("OUTLIER REPORT")
    print("====================")

    summary = show_outlier_summary(dataframe, threshold=threshold)

    total_outliers = summary["outlier_count"].sum()
    cols_with_outliers = (summary["outlier_count"] > 0).sum()

    print(f"\n * Threshold: IQR x {threshold}")
    print(f" * Total outliers detected: {total_outliers}")
    print(f" * Columns with outliers: {cols_with_outliers} / {len(summary)}")

    print("\nOUTLIER SUMMARY:")
    print("----------------")
    print(summary.to_string())

    print("\nBOXPLOT GRID:")
    print("-------------")
    outlier_boxplots(
        dataframe,
        threshold=threshold,
        grid=True,
        orient=orient,
        export_func=export_func,
        export_prefix=export_prefix,
    )


def show_dtypes(dataframe, column=None):
    """
    Display a dtype report for the full dataset or a deep dive into a single column.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The input dataset.
    column : str, optional
        If provided, shows a detailed dtype breakdown for that column.
        If None, shows a dtype summary for the full dataset.

    Returns
    -------
    None
        Prints the report to the console.
    """
    if column is not None:
        # --- Column deep dive ---
        if column not in dataframe.columns:
            print(f"Column '{column}' not found in DataFrame.")
            return

        series = dataframe[column]
        total = len(series)

        print(f"\nDTYPE REPORT: '{column}'")
        print("=" * 40)
        print(f"pandas dtype: {series.dtype}")
        print(f"Total values: {total}")

        # Count by Python type
        type_counts = series.apply(lambda x: type(x).__name__).value_counts()
        print(f"\nValue breakdown by type:")
        for type_name, count in type_counts.items():
            pct = round(count / total * 100, 1)
            print(f"  {type_name:<15} {count:>6} ({pct}%)")

        # Show non-dominant type values
        dominant_type = type_counts.index[0]
        if len(type_counts) > 1:
            for type_name in type_counts.index[1:]:
                mask = series.apply(lambda x: type(x).__name__) == type_name
                offending = series[mask]
                print(f"\n{type_name.upper()} VALUES ({len(offending)}):")
                for idx, val in offending.items():
                    print(f"  row {idx}: {val}")

    else:
        # --- Full dataset overview ---
        print("\nDTYPE REPORT")
        print("=" * 40)
        print(f"Total rows:    {len(dataframe)}")
        print(f"Total columns: {len(dataframe.columns)}")

        # dtype summary
        dtype_summary = get_dtype_summary(dataframe)
        print("\nDTYPE SUMMARY:")
        for key, value in dtype_summary.items():
            if value > 0:
                print(f"  * {key:<12} {value}")

        # column detail
        print(f"\nCOLUMN DETAIL:")
        print(f"  {'Column':<35} {'dtype':<15} {'Mixed'}")
        print(f"  {'-'*60}")

        mixed_cols = show_mixed_type_columns(dataframe)
        for col in dataframe.columns:
            is_mixed = col in mixed_cols
            mixed_label = "YES" if is_mixed else "No"
            print(f"  {col:<35} {str(dataframe[col].dtype):<15} {mixed_label}")

        # mixed type summary
        print(f"\nMIXED TYPE COLUMNS: {len(mixed_cols)}")
        if mixed_cols:
            for col in mixed_cols:
                type_counts = (
                    dataframe[col].apply(lambda x: type(x).__name__).value_counts()
                )
                breakdown = ", ".join(
                    f"{t} ({round(c/len(dataframe)*100, 1)}%)"
                    for t, c in type_counts.items()
                )
                print(f"  * {col}: {breakdown}")
