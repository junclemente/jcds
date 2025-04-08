import pandas as pd
from typing import Union, List


def create_dt_col(dataframe, datetime_col, col_type="month"):
    """
    Wrapper for create_dt_cols that creates a single datetime-derived column.

    Parameters
    ----------
    dataframe : DataFrame
        The input DataFrame.
    datetime_col : str
        Name of the column containing datetime values.
    col_type : str
        A single datetime component to extract.

    Returns
    -------
    DataFrame
        A copy of the DataFrame with one new datetime feature column added.

    Docstring generated with assistance from ChatGPT.
    """
    return create_dt_cols(dataframe, datetime_col, [col_type])


def create_dt_cols(dataframe, datetime_col, col_types=["month"]):
    """
    Add one or more datetime-derived columns to a DataFrame from a single datetime column.

    Parameters
    ----------
    dataframe : DataFrame
        The input DataFrame.
    datetime_col : str
        Name of the column containing datetime values.
    col_types : str or list of str, default ["month"]
        One or more datetime components to extract. Supported values:
        "year", "month", "day", "weekday", "weekday_name", "weekofyear",
        "quarter", "is_weekend", "dayofyear", "is_month_start", "is_month_end".

    Returns
    -------
    DataFrame
        A copy of the DataFrame with the new datetime feature columns added.

    Raises
    ------
    ValueError
        If the datetime_col is missing or if any component in col_types is unsupported.

    Docstring generated with assistance from ChatGPT.
    """
    supported_types = {
        "year": lambda x: x.dt.year,
        "month": lambda x: x.dt.month,
        "day": lambda x: x.dt.day,
        "weekday": lambda x: x.dt.weekday,
        "weekday_name": lambda x: x.dt.day_name(),
        "weekofyear": lambda x: x.dt.isocalendar().week,
        "quarter": lambda x: x.dt.quarter,
        "is_weekend": lambda x: x.dt.weekday >= 5,
        "dayofyear": lambda x: x.dt.dayofyear,
        "is_month_start": lambda x: x.dt.is_month_start,
        "is_month_end": lambda x: x.dt.is_month_end,
    }

    if datetime_col not in dataframe.columns:
        raise ValueError(f"Column '{datetime_col}' not found in DataFrame.")

    if isinstance(col_types, str):
        col_types = [col_types]

    unsupported = [ct for ct in col_types if ct not in supported_types]
    if unsupported:
        raise ValueError(
            f"Unsupported col_type(s): {unsupported}. Must be one of: {list(supported_types)}"
        )

    dataframe = dataframe.copy()

    if not pd.api.types.is_datetime64_any_dtype(dataframe[datetime_col]):
        try:
            dataframe[datetime_col] = pd.to_datetime(dataframe[datetime_col])
        except Exception as e:
            raise ValueError(f"Could not convert '{datetime_col}' to datetime: {e}")

    for col_type in col_types:
        new_col = f"{datetime_col}_{col_type}"
        dataframe[new_col] = supported_types[col_type](dataframe[datetime_col])

    return dataframe
