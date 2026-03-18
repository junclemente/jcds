import pandas as pd
from jcds.eda import outliers
from jcds import charts 


def test_plot_outlier_boxplots(sample_df):
    try:
        outliers.plot_outlier_boxplots(sample_df)
    except Exception as e:
        pytest.fail(f"plot_outlier_boxplots raised an exception: {e}")


def test_outlier_boxplots(sample_df):
    try:
        charts.outlier_boxplots(sample_df)
    except Exception as e:
        pytest.fail(f"charts.outlier_boxplots raised an exception: {e}")


def test_missing_data_heatmap_charts(sample_df):
    """Test that charts.plot_missing_heatmap runs without error."""
    try:
        charts.missing_data_heatmap(sample_df)
    except Exception as e:
        pytest.fail(f"charts.plot_missing_heatmap raised an exception: {e}")