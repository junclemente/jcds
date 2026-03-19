import math
import matplotlib.pyplot as plt
import seaborn as sns

from jcds.eda.inspect import show_convar, show_binary_list


def outlier_boxplots(
    dataframe,
    threshold=1.5,
    figsize=(6, 4),
    grid=True,
    ncols=3,
    grid_figsize=None,
    orient="v",  # "v" for vertical, "h" for horizontal
    export_func=None,
    export_prefix="boxplot",
):
    """
    Plots boxplots for numeric (non-binary) columns with potential outliers.

    Parameters
    ----------
    dataframe : pd.DataFrame
    threshold : float, optional
        IQR multiplier to define outliers. Default is 1.5.
    figsize : tuple, optional
        Figure size per plot in individual mode. Default is (6, 4).
    grid : bool, optional
        If True, plots all columns in a single grid figure. Default is True.
    ncols : int, optional
        Number of columns in grid mode. Default is 3.
    grid_figsize : tuple, optional
        Figure size for grid mode. Auto-calculated if not provided.
    export_func : callable, optional
        Function to export figures e.g. export_fig(fig, filename).
    export_prefix : str, optional
        Prefix for exported filenames. Default is 'boxplot'.

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

    if not grid:
        # --- Individual mode ---
        for col in outlier_cols:
            label = col.replace("_", " ").title()

            fig, ax = plt.subplots(figsize=figsize)
            if orient == "h":
                sns.boxplot(x=dataframe[col], ax=ax)
                ax.set_xlabel(label, fontsize=9)
                ax.set_ylabel("")
            else:
                sns.boxplot(y=dataframe[col], ax=ax)
                ax.set_ylabel(label, fontsize=9)
                ax.set_xlabel("")
            ax.set_title(f"Boxplot of {label}", fontsize=12)
            ax.set_ylabel(label)
            plt.tight_layout()

            if export_func:
                export_func(fig, f"{export_prefix}_{col}")

            plt.show()
            plt.close(fig)

    else:
        # --- Grid mode ---
        num_cols = len(outlier_cols)
        nrows = math.ceil(num_cols / ncols)

        if grid_figsize is None:
            grid_figsize = (ncols * 5, nrows * 4)

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=grid_figsize)
        axes = axes.flatten() if num_cols > 1 else [axes]

        for ax, col in zip(axes, outlier_cols):
            label = col.replace("_", " ").title()
            if orient == "h":
                sns.boxplot(x=dataframe[col], ax=ax)
                ax.set_xlabel(label, fontsize=9)
                ax.set_ylabel("")
            else:
                sns.boxplot(y=dataframe[col], ax=ax)
                ax.set_ylabel(label, fontsize=9)
                ax.set_xlabel("")
            ax.set_title(label, fontsize=10)
            ax.set_ylabel(label, fontsize=9)

        for ax in axes[num_cols:]:
            ax.set_visible(False)

        plt.tight_layout()

        if export_func:
            export_func(fig, f"{export_prefix}_grid")

        plt.show()
        plt.close(fig)
