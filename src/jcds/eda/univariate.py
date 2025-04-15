import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


def plot_categorical(series, title=None):
    """
    Plots a bar chart for a categorical variable.

    Parameters
    ----------
    series : pd.Series
        The categorical column to plot.
    title : str, optional
        Title for the plot.

    Returns
    -------
    None
    """
    counts = series.value_counts(dropna=False)
    sns.barplot(x=counts.index.astype(str), y=counts.values)
    plt.xticks(rotation=45)
    plt.title(title or f"Distribution of {series.name}")
    plt.xlabel(series.name)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
