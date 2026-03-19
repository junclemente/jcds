import pandas as pd
from jcds.utils import print_code_line, deprecated


def list_unique_values(dataframe, column):
    """
    Print the unique values in one or more specified columns of a DataFrame and display the corresponding code snippet.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame.
    column : str or list of str
        The column name or list of column names to inspect for unique values.

    Returns
    -------
    None
        This function prints output to the console and does not return a value.

    """
    display_code = f'DataFrame["{column}"].unique().tolist()'
    print_code_line(display_code)

    if isinstance(column, list):
        for col in column:
            print(f"Unique values in '{col}':")
            print(dataframe[col].unique().tolist())
            print("---")
    else:
        print(f"Unique values in '{column}':")
        print(dataframe[column].unique().tolist())
