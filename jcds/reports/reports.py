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
    id_like_columns = count_id_like_columns(dataframe)
    print(f"ID Like Columns: {id_like_columns}")

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
    print("CARDINALITY:")

    print("\nBINARY COLUMNS:")
    binary_list = show_binary_list(dataframe)
    for key, value in binary_list.items():
        total = len(value)
        print(f"There are {total} {key}.")
        if show_columns:
            if total > 0:
                print(f" * Columns: {value}")

    print("\nCONSTANT VARIABLES:")
    const_var = show_constantvars(dataframe)
    print(f"There are {len(const_var)} constant columns.")
    if show_columns:
        if len(const_var) > 0:
            print(f" * Columns: {const_var}")

    print("\nLOW CARDINALITY: ")
    lowcardvars = show_lowcardvars(dataframe)
    print(f" * There are {len(lowcardvars)} low cardinality variables.")
    if show_columns:
        print(f" * Columns: {lowcardvars}")

    print("\nHIGH CARDINALITY: ")
    highcardvars = show_highcardvars(dataframe)
    print(f" * There are {len(highcardvars)} high cardinality variables.")
    if show_columns:
        if len(highcardvars) > 0:
            print(f" * Columns: {highcardvars}")


def data_card2(dataframe, show_columns=False):
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
    print("CARDINALITY REPORT")

    # BINARY COLUMNS
    print("\n-- BINARY COLUMNS --")
    binary_list = show_binary_list(dataframe)
    for key, cols in binary_list.items():
        total = len(cols)
        print(f"There are {total} {key.replace('_', ' ')}.")
        if show_columns and total > 0:
            print(" • Columns:", cols)

    # CONSTANT COLUMNS
    print("\n-- CONSTANT VARIABLES --")
    const_var = show_constantvars(dataframe)
    print(f"There are {len(const_var)} constant columns.")
    if show_columns and const_var:
        print(" • Columns:", const_var)

    # LOW CARDINALITY
    print("\n-- LOW CARDINALITY CATEGORICAL --")
    lowcardvars = show_lowcardvars(dataframe)
    print(f"Found {len(lowcardvars)} categorical variables with ≤ 10 unique values.")
    if show_columns and lowcardvars:
        for col, n in lowcardvars:
            print(f" • {col}: {n} unique values")

    # HIGH CARDINALITY
    print("\n-- HIGH CARDINALITY CATEGORICAL --")
    highcardvars = show_highcardvars(dataframe)
    print(f"Found {len(highcardvars)} categorical variables with ≥ 90% unique values.")
    if show_columns and highcardvars:
        print(" • Columns:", highcardvars)


# def data_quality(dataframe):
#     shape = show_shape(dataframe)
#     dupes = show_dupes(dataframe)

#     print(f"There are {shape[0]} rows and {shape[1]} columns.")
#     print(f"There are {dupes} duplicated rows.")
