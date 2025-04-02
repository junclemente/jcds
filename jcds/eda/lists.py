import pandas as pd
from jcds.utils import print_code_line


def get_cat_list(dataframe):
    """
    Returns a list of categorical column names or the subset of the DataFrame
    containing only categorical columns.

    Args:
        dataframe (pd.DataFrame): The DataFrame to analyze.
        return_names (bool): If True, returns a list of column names.
                             If False, returns a DataFrame slice.

    Returns:
        list or pd.DataFrame: Categorical column names or DataFrame with categorical columns.
    """
    cat_list = dataframe.select_dtypes(include=["category", "object"]).columns.tolist()
    return cat_list


def get_cont_list(dataframe):
    """
    Returns a list of continuous (non-categorical) column names or the subset of the DataFrame
    containing only continuous columns.

    Args:
        dataframe (pd.DataFrame): The DataFrame to analyze.
        return_names (bool): If True, returns a list of column names.
                             If False, returns a DataFrame slice.

    Returns:
        list or pd.DataFrame: Continuous column names or DataFrame with continuous columns.
    """
    cont_list = dataframe.select_dtypes(exclude=["category", "object"]).columns.tolist()
    return cont_list


def list_unique_values(dataframe, column):
    display_code = f'DataFrame["{column}"].unique()'
    print_code_line(display_code)
    display(dataframe[column].unique())
