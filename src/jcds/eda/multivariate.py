import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from jcds.utils import deprecated
from jcds.charts.correlation import correlation_heatmap as _correlation_heatmap


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

@deprecated(
        reason="Use jcds.charts.correlation_heatmap() instead.",
        version="0.4.0"
)
def plot_correlation_heatmap(dataframe, method="pearson", title="Correlation Heatmap", figsize=(10, 8)):
    """Deprecated. Use jcds.charts.correlation_heatmap() instead."""
    return _correlation_heatmap(dataframe, method=method, title=title, figsize=figsize)
