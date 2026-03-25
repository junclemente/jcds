import re
import pandas as pd


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


def delete_columns(dataframe, columns_to_drop, inplace=False):
    """
    Drop one or more columns from a pandas DataFrame.

    Parameters
    ----------
    dataframe : pd.DataFrame
    columns_to_drop : list of str
    inplace : bool, optional
        Default is False.

    Returns
    -------
    pd.DataFrame or None
    """
    if inplace:
        dataframe.drop(columns=columns_to_drop, inplace=True)
        return None
    else:
        return dataframe.drop(columns=columns_to_drop)


def clean_column_names(dataframe, inplace=False):
    """
    Clean column names by stripping whitespace, lowercasing, and replacing
    non-alphanumeric characters with underscores. Handles duplicate names
    by appending a numeric suffix.

    Parameters
    ----------
    dataframe : pd.DataFrame
    inplace : bool, optional
        Default is False.

    Returns
    -------
    pd.DataFrame or None
    """
    df = dataframe if inplace else dataframe.copy()
    mapping = {}
    seen = {}
    for col in df.columns:
        new_col = col.strip().lower()
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
