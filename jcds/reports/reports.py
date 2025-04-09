from eda.inspect import show_shape, show_dupes


def df_info(dataframe):
    df_shape = show_shape(dataframe)
    df_dupes = show_dupes(dataframe)

    display(f"There are {df_shape[0]} rows and {df_shape[1]} columns.")
    display(f"The dataset contains {df_dupes} duplicated rows.")
