import pandas as pd


def to_int(dataframe, columns=None, unsigned=False, errors="raise", inplace=False):
    """
    Cast one or more columns to the smallest integer dtype.

    Parameters
    ----------
    dataframe : pd.DataFrame
    columns : list of str or None
        Columns to convert. If None, converts all numeric columns.
    unsigned : bool, optional
        If True, downcast to unsigned int. Default is False.
    errors : {'raise', 'coerce'}, optional
        How to handle non-convertible values. Default is 'raise'.
    inplace : bool, optional
        If True, modify in place. Default is False.

    Returns
    -------
    pd.DataFrame or None
    """
    df = dataframe if inplace else dataframe.copy()

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


def to_float(dataframe, columns, errors="raise", inplace=False):
    """
    Cast one or more columns to float dtype.

    Parameters
    ----------
    dataframe : pd.DataFrame
    columns : str or list of str
        Columns to convert.
    errors : {'raise', 'coerce', 'ignore'}, optional
        How to handle non-convertible values. Default is 'raise'.
    inplace : bool, optional
        If True, modify in place. Default is False.

    Returns
    -------
    pd.DataFrame or None
    """
    df = dataframe if inplace else dataframe.copy()
    cols = [columns] if isinstance(columns, str) else list(columns)

    missing = set(cols) - set(df.columns)
    if missing:
        raise ValueError(f"Columns not found in DataFrame: {missing}")

    for col in cols:
        df[col] = pd.to_numeric(df[col], errors=errors, downcast="float")

    if not inplace:
        return df


def to_numeric(dataframe, columns, errors="raise", downcast=None, inplace=False):
    """
    Convert one or more columns to numeric dtype.

    Parameters
    ----------
    dataframe : pd.DataFrame
    columns : str or list of str
        Columns to convert.
    errors : {'raise', 'coerce', 'ignore'}, optional
        Default is 'raise'.
    downcast : {'integer', 'signed', 'unsigned', 'float'}, optional
    inplace : bool, optional
        Default is False.

    Returns
    -------
    pd.DataFrame or None
    """
    df = dataframe if inplace else dataframe.copy()
    cols = [columns] if isinstance(columns, str) else list(columns)

    missing = set(cols) - set(df.columns)
    if missing:
        raise KeyError(f"Columns not found in DataFrame: {missing}")

    for col in cols:
        df[col] = pd.to_numeric(df[col], errors=errors, downcast=downcast)

    return df


def to_str(dataframe, columns, inplace=False):
    """
    Convert one or more columns to string dtype.

    Parameters
    ----------
    dataframe : pd.DataFrame
    columns : str or list of str
        Columns to convert.
    inplace : bool, optional
        Default is False.

    Returns
    -------
    pd.DataFrame or None
    """
    df = dataframe if inplace else dataframe.copy()
    cols = [columns] if isinstance(columns, str) else list(columns)

    missing = set(cols) - set(df.columns)
    if missing:
        raise ValueError(f"Columns not found in DataFrame: {missing}")

    for col in cols:
        df[col] = df[col].astype(str)

    if not inplace:
        return df