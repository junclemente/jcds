import matplotlib.pyplot as plt
import seaborn as sns


def correlation_heatmap(dataframe, method="pearson", title="Correlation Heatmap", figsize=(10, 8)):
    """
    Plots a heatmap of feature correlations.

    Parameters
    ----------
    dataframe : pd.DataFrame
        DataFrame to analyze.
    method : str, optional
        Correlation method ('pearson', 'kendall', 'spearman'). Default is 'pearson'.
    title : str, optional
        Title for the heatmap. Default is 'Correlation Heatmap'.
    figsize : tuple, optional
        Figure size. Default is (10, 8).

    Returns
    -------
    None
    """
    corr = dataframe.corr(method=method)
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", square=True, ax=ax)
    ax.set_title(title)
    plt.tight_layout()
    plt.show()
    plt.close(fig)