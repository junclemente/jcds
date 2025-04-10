import pandas as pd 
from jcds.eda import multivariate


def test_correlation_matrix_returns_dataframe(sample_df):
    numeric_cols = sample_df.select_dtypes(include="number")
    corr = multivariate.correlation_matrix(numeric_cols)
    assert isinstance(corr, pd.DataFrame)
    assert "Age" in corr.columns
    assert "Income" in corr.columns


def test_plot_correlation_heatmap_runs_without_error(sample_df):
    multivariate.plot_correlation_heatmap(sample_df[["Age", "Income"]])
