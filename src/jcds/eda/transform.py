import pandas


def rename_column(dataframe, oldname, newname):
    """
    Rename a column in a pandas DataFrame.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame containing the column to rename.
    oldname : str
        The current name of the column to be renamed.
    newname : str
        The new name for the column.

    Returns
    -------
    pandas.DataFrame
        A new DataFrame with the specified column renamed.

    Raises
    ------
    ValueError
        If `oldname` is not found in `dataframe.columns`.
    """
    if oldname not in dataframe.columns:
        raise ValueError(f"Column '{oldname}' not found in DataFrame.")
    return dataframe.rename(columns={oldname: newname})


def delete_columns(dataframe, columns_to_drop, inplace=False):
    """
    Drop one or more columns from a pandas DataFrame.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame from which to drop columns.
    columns_to_drop : list[str]
        A list of column names to remove.
    inplace : bool, default False
        If True, drop the columns in place and modify `dataframe` directly.
        If False, return a new DataFrame with the columns removed.

    Returns
    -------
    pandas.DataFrame or None
        If `inplace=False`, returns a new DataFrame with the specified columns removed.
        If `inplace=True`, returns None and modifies `dataframe` in place.

    Raises
    ------
    KeyError
        If any name in `columns_to_drop` is not found in `dataframe.columns`,
        unless `errors="ignore"` is passed to the underlying `drop`.

    Notes
    -----
    - When `inplace=True`, this function does not return the DataFrame; it returns None.
    - To ignore missing column names instead of raising, you could call:
      `dataframe.drop(columns=columns_to_drop, inplace=inplace, errors="ignore")`.
    - Docstring generated with assistance from ChatGPT
    """
    if inplace:
        dataframe.drop(columns=columns_to_drop, inplace=True)
        return None
    else:
        return dataframe.drop(columns=columns_to_drop)


import pandas as pd


def convert_to_int(
    dataframe: pd.DataFrame,
    columns: list[str] | None = None,
    unsigned: bool = False,
    errors: str = "raise",
    inplace: bool = False,
) -> pd.DataFrame | None:
    """
    Cast one or more columns to the smallest integer dtype that can hold the data.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame containing columns to convert.
    columns : list[str] or None, default None
        List of column names to convert. If None, all numeric columns will be downcast.
    unsigned : bool, default False
        If True, downcast to unsigned integer dtypes; otherwise to signed integer dtypes.
    errors : {'raise', 'coerce'}, default 'raise'
        How to handle non‑integer‑convertible values:
        - 'raise': throw an exception
        - 'coerce': set invalid parsing to NaN
    inplace : bool, default False
        If True, modify `dataframe` in place and return None.
        If False, work on a copy and return the new DataFrame.

    Returns
    -------
    pandas.DataFrame or None
        A new DataFrame with downcasted integer columns if `inplace=False`,
        or None if `inplace=True` (the original DataFrame is modified).

    Raises
    ------
    ValueError
        If any name in `columns` is not found in `dataframe.columns`.

    Notes
    -----
    - Internally uses `pd.to_numeric(..., downcast=...)` to automatically pick
      the tightest integer dtype (e.g., int8, Int16, UInt32).
    - To silently ignore bad conversions, use `errors='coerce'`.
    - Docstring generated with assistance from ChatGPT
    """
    # Decide whether to work on a copy or in-place
    df = dataframe if inplace else dataframe.copy()

    # Determine target columns
    if columns is None:
        cols = df.select_dtypes(include="number").columns
    else:
        missing = set(columns) - set(df.columns)
        if missing:
            raise ValueError(f"Columns not found in DataFrame: {missing}")
        cols = columns

    kind = "unsigned" if unsigned else "integer"
    for col in cols:
        df[col] = pd.to_numeric(df[col], downcast=kind, errors=errors)

    if not inplace:
        return df


def convert_to_categorical(
    dataframe: pd.DataFrame,
    columns: list[str] | None = None,
    ordered: bool = False,
    inplace: bool = False,
) -> pd.DataFrame | None:
    """
    Convert one or more columns to pandas Categorical dtype.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame containing columns to convert.
    columns : list[str] or None, default None
        List of column names to convert. If None, all object‐ or string‐
        typed columns will be converted.
    ordered : bool, default False
        Whether the resulting Categorical should be ordered.
    inplace : bool, default False
        If True, modify `dataframe` in place and return None.
        If False, return a new DataFrame with the conversions applied.

    Returns
    -------
    pandas.DataFrame or None
        New DataFrame if `inplace=False`, or None if `inplace=True`.

    Raises
    ------
    ValueError
        If any name in `columns` isn’t found in `dataframe.columns`.

    Notes
    -----
    Uses `Series.astype('category')` under the hood; ordering only applies
    if you need to compare categories (e.g., for sorting or inequalities).
    """
    df = dataframe if inplace else dataframe.copy()

    # pick target cols
    if columns is None:
        cols = df.select_dtypes(include=["object", "string"]).columns
    else:
        missing = set(columns) - set(df.columns)
        if missing:
            raise ValueError(f"Columns not found: {missing}")
        cols = columns

    for col in cols:
        df[col] = df[col].astype(pd.CategoricalDtype(ordered=ordered))

    if not inplace:
        return df


def convert_to_object(
    dataframe: pd.DataFrame, columns: list[str], inplace: bool = False
) -> pd.DataFrame | None:
    """
    Cast one or more columns to the generic Python object dtype.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame containing columns to convert.
    columns : list[str]
        List of column names to convert to object.
    inplace : bool, default False
        If True, modify `dataframe` in place and return None.
        If False, return a new DataFrame with the conversions applied.

    Returns
    -------
    pandas.DataFrame or None
        New DataFrame if `inplace=False`, or None if `inplace=True`.

    Raises
    ------
    ValueError
        If any name in `columns` isn’t found in `dataframe.columns`.

    Notes
    -----
    Converting to “object” is rarely needed for strings—consider using
    pandas’ `StringDtype()` for better missing‐value support. This exists
    mainly for legacy interoperability.
    """
    df = dataframe if inplace else dataframe.copy()

    missing = set(columns) - set(df.columns)
    if missing:
        raise ValueError(f"Columns not found: {missing}")

    for col in columns:
        df[col] = df[col].astype("object")

    if not inplace:
        return df
