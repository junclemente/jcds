import pandas as pd
from jcds.eda import outliers


def test_plot_outlier_boxplots(sample_df):
    try:
        outliers.plot_outlier_boxplots(sample_df)
    except Exception as e:
        pytest.fail(f"plot_outlier_boxplots raised an exception: {e}")


def test_plot_missing_heatmap(sample_df):
    """Test that plot_missing_heatmap runs without error."""
    try:
        outliers.plot_missing_heatmap(sample_df)
    except Exception as e:
        pytest.fail(f"plot_missing_heatmap raised an exception: {e}")