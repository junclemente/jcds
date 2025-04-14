from IPython.display import display, HTML
from jcds.eda import (
    show_shape,
    show_dupes,
    show_convar,
    show_catvar,
    show_binary_list,
    show_lowcardvars,
)

# from jcds.utils.formatting import render_html_block


def data_info(dataframe):
    shape = show_shape(dataframe)
    dupes = show_dupes(dataframe)
    convar = show_convar(dataframe)
    catvar = show_catvar(dataframe)
    binary_list = show_binary_list(dataframe)
    lowcardvars = show_lowcardvars(dataframe)

    print(f"There are {shape[0]} rows and {shape[1]} columns.")
    print(f"There are {dupes} duplicated rows.")
    print(f"convar: {convar}")
    print(f"catvar: {catvar}")
    print(f"binaray_list: {binary_list}")
    print(f"lowcardvars {lowcardvars}")


# def data_quality(dataframe):
#     shape = show_shape(dataframe)
#     dupes = show_dupes(dataframe)

#     print(f"There are {shape[0]} rows and {shape[1]} columns.")
#     print(f"There are {dupes} duplicated rows.")
