from IPython.display import display, HTML
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
)

# from jcds.utils.formatting import render_html_block


def data_info(dataframe, show_columns=False):
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


def data_cardinality(dataframe, show_columns=False):
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


def data_quality(dataframe, show_columns=False):

    NEAR_CONSTANT_COLUMNS_THRESHOLD = 0.95
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
    rows_missing_any = count_rows_with_any_na(dataframe)
    rows_missing_all = count_rows_with_all_na(dataframe)
    print(f" * Rows missing any: {rows_missing_any}")
    print(f" * Rows missing all: {rows_missing_all}")

    # duplicate rows
    duplicates = show_dupes(dataframe)
    print(f"\nDUPLICATES: {duplicates}")

    # missing columns
    print("\nCOLUMNS:")
    missing_summary = show_missing_summary(dataframe, sort=True, threshold=0.0)
    key_list = list(missing_summary.keys())
    print(f"Columns missing any: {len(missing_summary)}")
    if show_columns and missing_summary:
        for key, value in missing_summary.items():
            print(f"\t{key}: {value[0]} missing ({value[1]:.1f}%)")
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
        print(f"Column list: {near_constant_columns}")

    # mixed data types
    mixed_data_columns = show_mixed_type_columns(dataframe)
    print(f"\nMIXED DATATYPES: {len(mixed_data_columns)}")
    if show_columns and mixed_data_columns:
        print(f"Column list: {mixed_data_columns}")

    # high cardinality

    # outlier detection?
