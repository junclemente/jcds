from jcds.eda.inspect import show_convar, show_binary_list
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def detect_outliers_iqr(dataframe, threshold=1.5, return_mask=False):
    """
    Detect outliers in numeric (non-binary) columns using the IQR method.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame.
    threshold : float, optional
        The IQR multiplier to determine outlier bounds. Default is 1.5.
    return_mask : bool, optional
        If True, returns a boolean mask DataFrame. If False, returns outlier counts.

    Returns
    -------
    dict or pd.DataFrame
        If return_mask is False: a dict {column: count of outliers}
        If return_mask is True: a DataFrame with boolean values (True = outlier)
    """
    numeric_cols = show_convar(dataframe)
    binary_info = show_binary_list(dataframe)
    binary_cols = binary_info["binary_columns"] + binary_info["binary_with_nan"]

    # filter out binary cols
    outlier_cols = []
    for col in numeric_cols:
        if col not in binary_cols:
            outlier_cols.append(col)

    outlier_counts = {}
    outlier_mask = pd.DataFrame(False, index=dataframe.index, columns=dataframe.columns)

    for col in outlier_cols:
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


def plot_outlier_boxplots(dataframe, threshold=1.5, figsize=(14, 5)):
    """
    Plots boxplots for numeric (non-binary) columns with potential outliers.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame.
    threshold : float, optional
        IQR multiplier to define outliers. Default is 1.5.
    figsize : tuple
        Size of the figure.

    Returns
    -------
    None
    """
    numeric_cols = show_convar(dataframe)
    binary_info = show_binary_list(dataframe)
    binary_cols = binary_info["binary_columns"] + binary_info["binary_with_nan"]

    outlier_cols = [col for col in numeric_cols if col not in binary_cols]

    if not outlier_cols:
        print("No numeric (non-binary) columns available for boxplot.")
        return

    num_cols = len(outlier_cols)
    ncols = min(3, num_cols)
    nrows = (num_cols + ncols - 1) // ncols

    fig, axes = plt.subplots(
        nrows=nrows, ncols=ncols, figsize=(figsize[0], figsize[1] * nrows)
    )
    axes = axes.flatten() if num_cols > 1 else [axes]

    for ax, col in zip(axes, outlier_cols):
        sns.boxplot(y=dataframe[col], ax=ax)
        ax.set_title(col)

    for ax in axes[num_cols:]:
        ax.axis("off")

    plt.tight_layout()
    plt.show()
