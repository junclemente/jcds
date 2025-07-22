import pandas as pd
from jcds.eda import outliers


def test_plot_outlier_boxplots(sample_df):
    try:
        outliers.plot_outlier_boxplots(sample_df)
    except Exception as e:
        pytest.fail(f"plot_outlier_boxplots raised an exception: {e}")
