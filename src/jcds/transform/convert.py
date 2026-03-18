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
    

def to_categorical(dataframe, columns=None, ordered=False, inplace=False):
    """
    Convert one or more columns to pandas Categorical dtype.

    Parameters
    ----------
    dataframe : pd.DataFrame
    columns : list of str or None
        Columns to convert. If None, converts all object/string columns.
    ordered : bool, optional
        Whether the Categorical should be ordered. Default is False.
    inplace : bool, optional
        Default is False.

    Returns
    -------
    pd.DataFrame or None
    """
    df = dataframe if inplace else dataframe.copy()

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


def to_bool(dataframe, columns, true_values=None, false_values=None, errors="raise", inplace=False):
    """
    Convert one or more columns to boolean dtype.

    Parameters
    ----------
    dataframe : pd.DataFrame
    columns : str or list of str
        Columns to convert.
    true_values : list, optional
        Values to interpret as True. Default: ['true', '1', 'yes', 'y', 't']
    false_values : list, optional
        Values to interpret as False. Default: ['false', '0', 'no', 'n', 'f']
    errors : {'raise', 'coerce'}, optional
        Default is 'raise'.
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

    default_true = {"true", "1", "yes", "y", "t"}
    default_false = {"false", "0", "no", "n", "f"}
    trues = set(v.lower() for v in (true_values or default_true))
    falses = set(v.lower() for v in (false_values or default_false))

    for col in cols:
        series = df[col].astype(str).str.strip().str.lower()
        result = pd.Series(pd.NA, index=series.index, dtype="boolean")
        mask_true = series.isin(trues)
        mask_false = series.isin(falses)
        result[mask_true] = True
        result[mask_false] = False
        unknown = ~(mask_true | mask_false)
        if errors == "raise" and unknown.any():
            bad_vals = series[unknown].unique()
            raise ValueError(f"Unrecognized boolean values in column {col}: {bad_vals}")
        df[col] = result

    if not inplace:
        return df


def to_datetime(dataframe, columns, format=None, errors="raise", inplace=False):
    """
    Convert one or more columns to datetime dtype.

    Parameters
    ----------
    dataframe : pd.DataFrame
    columns : str or list of str
        Columns to convert.
    format : str, optional
        Datetime format string.
    errors : {'raise', 'coerce', 'ignore'}, optional
        Default is 'raise'.
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
        df[col] = pd.to_datetime(df[col], format=format, errors=errors)

    return df


def to_object(dataframe, columns, inplace=False):
    """
    Cast one or more columns to object dtype.

    Parameters
    ----------
    dataframe : pd.DataFrame
    columns : list of str
        Columns to convert.
    inplace : bool, optional
        Default is False.

    Returns
    -------
    pd.DataFrame or None
    """
    df = dataframe if inplace else dataframe.copy()

    missing = set(columns) - set(df.columns)
    if missing:
        raise ValueError(f"Columns not found: {missing}")

    for col in columns:
        df[col] = df[col].astype("object")

    if not inplace:
        return df