import matplotlib.pyplot as plt 
import seaborn as sns 

def missing_data_heatmap(dataframe, figsize=(12, 10), cmap="viridis", title = "Missing Data Heatmap", xlabel = "Columns", ylabel = "Rows"): 
    """
    Plots a heatmap of missing values across the DataFrame.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input DataFrame.
    figsize : tuple, optional
        Figure size. Default is (12, 10).
    cmap : str, optional
        Colormap for the heatmap. Default is 'viridis'.
    title : str, optional
        Title of the plot. Default is 'Missing Data Heatmap'.
    xlabel : str, optional
        Label for the x-axis. Default is 'Columns'.
    ylabel : str, optional
        Label for the y-axis. Default is 'Rows'.

    Returns
    -------
    None
    """
    fig, ax = plt.subplots(figsize=figsize) 
    sns.heatmap(dataframe.isnull(), cbar=False, cmap=cmap, ax=ax) 
    ax.set_title(title, fontsize=14) 
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout() 
    plt.show() 
    plt.close(fig) 
