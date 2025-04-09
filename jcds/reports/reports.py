from jcds.eda import show_shape, show_dupes


def data_quality(dataframe):
    shape = show_shape(dataframe)
    dupes = show_dupes(dataframe)

    print(f"There are {shape[0]} rows and {shape[1]} columns.")
    print(f"There are {dupes} duplicated rows.")
