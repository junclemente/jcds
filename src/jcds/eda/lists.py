import pandas as pd
from jcds.utils import print_code_line, deprecated



@deprecated(
        reason="This is being replaced by show_catvar()",
        version="0.3.0"
)
def get_cat_list(dataframe):
    """
    Return a list of categorical column names or the subset of the DataFrame containing only categorical columns.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The DataFrame to analyze.
    return_names : bool
        If True, returns a list of column names. If False, returns a DataFrame slice.

    Returns
    -------
    list of str or pd.DataFrame
        Categorical column names if `return_names` is True, or a DataFrame containing only categorical columns if False.

    """

    cat_list = dataframe.select_dtypes(include=["category", "object"]).columns.tolist()
    return cat_list

@deprecated(
        reason="This is being replaced by show_contvar()", 
        version="0.3.0"
)
def get_cont_list(dataframe):
    """
    Return a list of continuous (non-categorical) column names or the subset of the DataFrame containing only continuous columns.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The DataFrame to analyze.
    return_names : bool
        If True, returns a list of column names. If False, returns a DataFrame slice.

    Returns
    -------
    list of str or pd.DataFrame
        Continuous column names if `return_names` is True, or a DataFrame containing only continuous columns if False.

    """

    cont_list = dataframe.select_dtypes(exclude=["category", "object"]).columns.tolist()
    return cont_list


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
