# src/jcds/charts/distributions.py

import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def hist_kde(
    df: pd.DataFrame,
    columns: list = None,
    figsize: tuple = (7, 4),
    grid: bool = True,
    ncols: int = 3,
    grid_figsize: tuple = None,
    export_func=None,
    export_prefix: str = "hist_kde",
) -> None:
    """
    Plots histogram with KDE overlay for numerical columns.

    Parameters
    ----------
    df : pd.DataFrame
    columns : list, optional
        Columns to plot. Defaults to all numerical columns.
    figsize : tuple, optional
        Figure size per plot in individual mode. Default is (7, 4).
    grid : bool, optional
        If True, plots all columns in a single grid figure. Default is False.
    ncols : int, optional
        Number of columns in grid mode. Default is 3.
    grid_figsize : tuple, optional
        Figure size for grid mode. Auto-calculated if not provided.
    export_func : callable, optional
        Function to export figures e.g. export_fig(fig, filename).
    export_prefix : str, optional
        Prefix for exported filenames. Default is 'hist_kde'.
    """
    if columns is None:
        columns = df.select_dtypes(include="number").columns.tolist()

    if not grid:
        # --- Individual mode ---
        for col in columns:
            label = col.replace("_", " ").title()

            fig, ax = plt.subplots(figsize=figsize)

            sns.histplot(
                data=df,
                x=col,
                bins="auto",
                stat="density",
                alpha=0.65,
                edgecolor="white",
                kde=False,
                ax=ax,
            )

            sns.kdeplot(
                data=df,
                x=col,
                linewidth=2,
                warn_singular=False,
                ax=ax,
            )

            ax.set_title(f"Distribution of {label}", fontsize=12)
            ax.set_xlabel(label)
            ax.set_ylabel("Density")
            ax.tick_params(axis="x", rotation=45)
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
        axes = axes.flatten()

        for i, col in enumerate(columns):
            label = col.replace("_", " ").title()
            ax = axes[i]

            sns.histplot(
                data=df,
                x=col,
                bins="auto",
                stat="density",
                alpha=0.65,
                edgecolor="white",
                kde=False,
                ax=ax,
            )

            sns.kdeplot(
                data=df,
                x=col,
                linewidth=2,
                warn_singular=False,
                ax=ax,
            )

            ax.set_title(f"Distribution of {label}", fontsize=10)
            ax.set_xlabel(label, fontsize=9)
            ax.set_ylabel("Density", fontsize=9)
            ax.tick_params(axis="x", rotation=45)

        # Hide any unused axes
        for j in range(i + 1, len(axes)):
            axes[j].set_visible(False)

        plt.tight_layout()

        if export_func:
            export_func(fig, f"{export_prefix}_grid")

        plt.show()
        plt.close(fig)
