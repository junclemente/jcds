from IPython.display import display, HTML
from jcds.eda import (
    show_memory_use,
    show_shape,
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

    print("\nLOW CARDINALITY CATEGORICAL COLUMNS]")
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
    print("DATA QUALITY REPORT")

    shape = show_shape(dataframe)
    dupes = show_dupes(dataframe)

    print(f"There are {shape[0]} rows and {shape[1]} columns.")
    print(f"There are {dupes} duplicated rows.")
