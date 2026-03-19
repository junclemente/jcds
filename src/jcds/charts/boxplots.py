import matplotlib.pyplot as plt 
import seaborn as sns 

from jcds.eda.inspect import show_convar, show_binary_list


def outlier_boxplots(dataframe, threshold=1.5, figsize=(14, 5)):
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