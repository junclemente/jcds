from IPython.display import display, HTML
from jcds.eda import (
    show_shape,
    show_dupes,
    show_convar,
    show_catvar,
    show_binary_list,
    show_lowcardvars,
    show_highcardvars,
    show_datetime_columns, 
    show_possible_datetime_columns, 
    get_dtype_summary
)

# from jcds.utils.formatting import render_html_block


def data_info(dataframe, show_columns=False):
    print("\nSHAPE:")
    shape = show_shape(dataframe)
    print(f"There are {shape[0]} rows and {shape[1]} columns.")

    print("\nDUPLICATES:")
    dupes = show_dupes(dataframe)
    print(f"There are {dupes} duplicated rows.")


    print("\nCOLUMNS/VARIABLES:")

    convar = show_convar(dataframe)
    print(f"There are {len(convar)} numerical (continuous) variables.")
    if show_columns:
        print(f"\tColumns: {convar}")

    catvar = show_catvar(dataframe)
    print(f"There are {len(catvar)} categorical (nominal/ordinal) variables.")
    if show_columns: 
        print(f"\tColumns: {catvar}")

    print("\nDATETIME COLUMNS:")
    dt_cols = show_datetime_columns(dataframe)
    print(f"There are {len(dt_cols)} datetime variables.")

    possible_dt_cols = show_possible_datetime_columns(dataframe) 
    print(f"There could be {len(possible_dt_cols)} possible datetime variables.")


def data_cardinality(dataframe, show_columns=False):
    
    print("CARDINALITY:")
    binary_list = show_binary_list(dataframe)
    for key, value in binary_list.items():
        total = len(value)
        print(f"{key}: {total} columns")
        if show_columns:
            print(f"\tColumns: {value}")

    lowcardvars = show_lowcardvars(dataframe)
    print(f"\tThere are {len(lowcardvars)} low cardinality variables.")
    if show_columns:
        print(f"\tColumns: {lowcardvars}")

    highcardvars = show_highcardvars(dataframe)
    print(f"\tThere are {len(highcardvars)} high cardinality variables.")
    if show_columns:
        print(f"\tColumns: {highcardvars}")


# def data_quality(dataframe):
#     shape = show_shape(dataframe)
#     dupes = show_dupes(dataframe)

#     print(f"There are {shape[0]} rows and {shape[1]} columns.")
#     print(f"There are {dupes} duplicated rows.")
