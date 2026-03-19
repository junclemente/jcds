import matplotlib.pyplot as plt
import seaborn as sns


def categorical_barplot(series, title=None, figsize=(10, 6)):
    """
    Plots a bar chart for a categorical variable.

    Parameters
    ----------
    series : pd.Series
        The categorical column to plot.
    title : str, optional
        Title for the plot.
    figsize : tuple, optional
        Figure size. Default is (10, 6).

    Returns
    -------
    None
    """
    counts = series.value_counts(dropna=False)
    fig, ax = plt.subplots(figsize=figsize)
    sns.barplot(x=counts.index.astype(str), y=counts.values, ax=ax)
    plt.xticks(rotation=45, ha="right")
    ax.set_title(title or f"Distribution of {series.name}")
    ax.set_xlabel(series.name)
    ax.set_ylabel("Count")
    plt.tight_layout()
    plt.show()
    plt.close(fig)