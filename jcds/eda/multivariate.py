import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def correlation_matrix(dataframe, method="pearson"):
    """
    Returns the correlation matrix for numeric features.

    Parameters
    ----------
    dataframe : pd.DataFrame
        DataFrame to analyze.
    method : str
        Correlation method ('pearson', 'kendall', 'spearman').

    Returns
    -------
    pd.DataFrame
        Correlation matrix.
    """
    return dataframe.corr(method=method)


def plot_correlation_heatmap(dataframe, method="pearson", title="Correlation Heatmap"):
    """
    Plots a heatmap of feature correlations.

    Parameters
    ----------
    dataframe : pd.DataFrame
        DataFrame to analyze.
    method : str
        Correlation method ('pearson', 'kendall', 'spearman').
    title : str
        Title for the heatmap.

    Returns
    -------
    None
    """
    corr = dataframe.corr(method=method)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", square=True)
    plt.title(title)
    plt.tight_layout()
    plt.show()
