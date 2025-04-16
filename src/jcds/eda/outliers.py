import pandas as pd


def detect_outliers_iqr(dataframe, threshold=1.5, return_mask=False):
    """
    Detect outliers in numeric columns using the IQR method.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame.
    threshold : float, optional
        The IQR multiplier to determine outlier bounds. Default is 1.5.
    return_mask : bool, optional
        If True, returns a boolean mask DataFrame of the same shape as input
        indicating outlier positions. If False, returns a summary count per column.

    Returns
    -------
    dict or pd.DataFrame
        If return_mask is False: a dict {column: count of outliers}
        If return_mask is True: a DataFrame with boolean values (True = outlier)
    """
    numeric_cols = dataframe.select_dtypes(include="number").columns
    outlier_counts = {}
    outlier_mask = pd.DataFrame(False, index=dataframe.index, columns=dataframe.columns)

    for col in numeric_cols:
        Q1 = dataframe[col].quantile(0.25)
        Q3 = dataframe[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - threshold * IQR
        upper = Q3 + threshold * IQR

        is_outlier = (dataframe[col] < lower) | (dataframe[col] > upper)
        outlier_mask[col] = is_outlier

        if not return_mask:
            outlier_counts[col] = int(is_outlier.sum())

    return outlier_mask if return_mask else outlier_counts
