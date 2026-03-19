import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from jcds.utils import deprecated
from jcds.charts.categorical import categorical_barplot as _categorical_barplot


def describe_categorical(series):
    """
    Returns frequency and percentage counts for a categorical variable.

    Parameters
    ----------
    series : pd.Series
        The categorical column to describe.

    Returns
    -------
    pd.DataFrame
        Table with value counts and percentages.

    Docstring generated with assistance from ChatGPT.
    """
    counts = series.value_counts(dropna=False)
    percents = counts / len(series) * 100
    return pd.DataFrame({"Count": counts, "Percent": percents.round(2)})


@deprecated(
        reason="Use jcds.charts.categorical_barplot() instead.",
        version="0.4.0"
)
def plot_categorical(series, title=None, figsize=(10, 6)):
    """Deprecated. Use jcds.charts.categorical_barplot() instead."""
    return _categorical_barplot(series, title=title, figsize=figsize)
