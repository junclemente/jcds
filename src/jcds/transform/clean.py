import re
import pandas as pd
from jcds.utils import deprecated


def rename_column(dataframe, oldname, newname):
    """
    Rename a column in a pandas DataFrame.

    Parameters
    ----------
    dataframe : pd.DataFrame
    oldname : str
    newname : str

    Returns
    -------
    pd.DataFrame
    """
    if oldname not in dataframe.columns:
        raise ValueError(f"Column '{oldname}' not found in DataFrame.")
    return dataframe.rename(columns={oldname: newname})


def drop_columns(dataframe, columns_to_drop, inplace=False):
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
        If any name in `columns_to_drop` is not found in `dataframe.columns`.
    """
    if inplace:
        dataframe.drop(columns=columns_to_drop, inplace=True)
        return None
    else:
        return dataframe.drop(columns=columns_to_drop)


@deprecated(reason="Use drop_columns() instead.", version="0.4.0")
def delete_columns(dataframe, columns_to_drop, inplace=False):
    """Deprecated. Use drop_columns() instead."""
    return drop_columns(dataframe, columns_to_drop, inplace=inplace)


@deprecated(reason="Use drop_columns() instead.", version="0.4.0")
def delete_columns(dataframe, columns_to_drop, inplace=False):
    """
    Deprecated. Use drop_columns() instead.
    """
    if inplace:
        dataframe.drop(columns=columns_to_drop, inplace=True)
        return None
    else:
        return dataframe.drop(columns=columns_to_drop)


def standardize_column_names(dataframe, inplace=False):
    """
    Standardize DataFrame column names to snake_case.

    Strips whitespace, lowercases, and replaces non-alphanumeric
    characters with underscores. Handles column name collisions
    by appending a numeric suffix.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Input DataFrame.
    inplace : bool, optional
        If True, modify in place. Default is False.

    Returns
    -------
    pandas.DataFrame
        DataFrame with standardized column names.
    """
    df = dataframe if inplace else dataframe.copy()
    mapping = {}
    seen = {}
    for col in df.columns:
        new_col = col.strip()
        new_col = new_col.lower()
        new_col = re.sub(r"[^0-9a-z]+", "_", new_col)
        new_col = re.sub(r"__+", "_", new_col).strip("_")
        if new_col in seen:
            seen[new_col] += 1
            new_col = f"{new_col}_{seen[new_col]}"
        else:
            seen[new_col] = 0
        mapping[col] = new_col
    df.rename(columns=mapping, inplace=True)
    return df


@deprecated(reason="Use standardize_column_names() instead.", version="0.4.0")
def clean_column_names(dataframe, inplace=False):
    """Deprecated. Use standardize_column_names() instead."""
    return standardize_column_names(dataframe, inplace=inplace)


def drop_row(dataframe, row, by="position", inplace=False):
    """
    Drop a single row from a DataFrame.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame.
    row : int
        Row to drop. If by='position', uses iloc index. If by='label', uses index label.
    by : str, optional
        'position' (default) uses positional index, 'label' uses index label.
    inplace : bool, optional
        If True, modifies the DataFrame in place. Default is False.

    Returns
    -------
    pd.DataFrame or None
        New DataFrame with row dropped if inplace=False, else None.
    """
    if by == "position":
        label = dataframe.index[row]
    else:
        label = row

    if label not in dataframe.index:
        raise KeyError(f"Row label '{label}' not found in DataFrame index.")

    if inplace:
        dataframe.drop(index=label, inplace=True)
        return None
    else:
        return dataframe.drop(index=label)
