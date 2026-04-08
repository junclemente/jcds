import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


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


def cat_barplots(
    df,
    columns=None,
    max_unique=20,
    top_n=10,
    orient="h",
    grid=True,
    ncols=3,
    figsize=(6, 4),
    grid_figsize=None,
    export_func=None,
    export_prefix="cat_barplot",
):
    """
    Plots bar charts for categorical columns.

    Parameters
    ----------
    df : pd.DataFrame
    columns : list, optional
        Columns to plot. Defaults to all categorical columns with <= max_unique unique values.
    max_unique : int, optional
        Maximum unique values to include a column. Default is 20.
    top_n : int, optional
        Number of top values to show per column. Default is 10.
    orient : str, optional
        'h' for horizontal (default), 'v' for vertical bars.
    grid : bool, optional
        If True, plots all columns in a single grid figure. Default is True.
    ncols : int, optional
        Number of columns in grid mode. Default is 3.
    figsize : tuple, optional
        Figure size per plot in individual mode. Default is (6, 4).
    grid_figsize : tuple, optional
        Figure size for grid mode. Auto-calculated if not provided.
    export_func : callable, optional
        Function to export figures e.g. export_fig(fig, filename).
    export_prefix : str, optional
        Prefix for exported filenames. Default is 'cat_barplot'.

    Returns
    -------
    None
    """
    # determine columns
    if columns is None:
        cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
        columns = [c for c in cat_cols if df[c].nunique() <= max_unique]

    if not columns:
        print("No categorical columns found within the cardinality threshold.")
        return

    if not grid:
        # --- Individual mode ---
        for col in columns:
            label = col.replace("_", " ").title()
            counts = df[col].value_counts(dropna=False).head(top_n)

            fig, ax = plt.subplots(figsize=figsize)

            if orient == "h":
                sns.barplot(x=counts.values, y=counts.index.astype(str), ax=ax)
                ax.set_xlabel("Count")
                ax.set_ylabel("")
            else:
                sns.barplot(x=counts.index.astype(str), y=counts.values, ax=ax)
                ax.set_xlabel("")
                ax.set_ylabel("Count")
                ax.tick_params(axis="x", rotation=45)

            ax.set_title(f"Distribution of {label}", fontsize=12)
            plt.tight_layout()

            if export_func:
                export_func(fig, f"{export_prefix}_{col}")

            plt.show()
            plt.close(fig)

    else:
        # --- Grid mode ---
        nrows = math.ceil(len(columns) / ncols)

        if grid_figsize is None:
            grid_figsize = (ncols * 5, nrows * 4)

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=grid_figsize)
        axes = axes.flatten() if len(columns) > 1 else [axes]

        for i, col in enumerate(columns):
            label = col.replace("_", " ").title()
            counts = df[col].value_counts(dropna=False).head(top_n)
            ax = axes[i]

            if orient == "h":
                sns.barplot(x=counts.values, y=counts.index.astype(str), ax=ax)
                ax.set_xlabel("Count", fontsize=8)
                ax.set_ylabel("")
            else:
                sns.barplot(x=counts.index.astype(str), y=counts.values, ax=ax)
                ax.set_xlabel("")
                ax.set_ylabel("Count", fontsize=8)
                ax.tick_params(axis="x", rotation=45)

            ax.set_title(label, fontsize=10)

        for j in range(i + 1, len(axes)):
            axes[j].set_visible(False)

        plt.tight_layout()

        if export_func:
            export_func(fig, f"{export_prefix}_grid")

        plt.show()
        plt.close(fig)
