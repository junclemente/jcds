import pandas


def rename_col(dataframe, oldname, newname):
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
