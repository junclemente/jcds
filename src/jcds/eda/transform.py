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

    Notes
    -----
    Docstring generated with assistance from ChatGPT
    """
    if oldname not in dataframe.columns:
        raise ValueError(f"Column '{oldname}' not found in DataFrame.")
    return dataframe.rename(columns={oldname: newname})
