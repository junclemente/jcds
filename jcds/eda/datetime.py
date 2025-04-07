import pandas as pd


def create_dt_col(
    dataframe: pd.DataFrame, datetime_col: str, col_type: str = "month"
) -> pd.DataFrame:
    """
    Add a new column to the DataFrame derived from a datetime column.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame.
    datetime_col : str
        Name of the column containing datetime values.
    col_type : str, default "month"
        Type of datetime component to extract. Supported values:
        "year", "month", "day", "weekday", "weekday_name", "weekofyear", "quarter",
        "is_weekend", "dayofyear", "is_month_start", "is_month_end".

    Returns
    -------
    pd.DataFrame
        A copy of the DataFrame with the new derived datetime column added.

    Raises
    ------
    ValueError
        If the column doesn't exist or `col_type` is not supported.

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

    if col_type not in supported_types:
        raise ValueError(
            f"Unsupported col_type '{col_type}'. Must be one of: {list(supported_types.keys())}"
        )

    df = dataframe.copy()

    if not pd.api.types.is_datetime64_any_dtype(df[datetime_col]):
        try:
            df[datetime_col] = pd.to_datetime(df[datetime_col])
        except Exception as e:
            raise ValueError(f"Could not convert '{datetime_col}' to datetime: {e}")

    new_col = f"{datetime_col}_{col_type}"
    df[new_col] = supported_types[col_type](df[datetime_col])

    return df
