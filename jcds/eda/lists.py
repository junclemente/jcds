import pandas as pd
import numpy as np


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
