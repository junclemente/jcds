# tests/test_charts.py
import pytest
import pandas as pd
import numpy as np
import matplotlib

matplotlib.use("Agg")  # non-interactive backend for testing
from jcds import charts


@pytest.fixture
def num_df():
    return pd.DataFrame(
        {
            "col_a": [1.0, 2.0, 3.0, 4.0, 5.0],
            "col_b": [10.0, 20.0, 30.0, 40.0, 50.0],
            "cat_col": ["a", "b", "a", "b", "a"],  # should be ignored
        }
    )


# --- hist_kde individual mode ---
def test_hist_kde_runs_all_numeric(num_df):
    """Should run without error on all numeric columns."""
    charts.hist_kde(num_df, grid=False)


def test_hist_kde_runs_specific_columns(num_df):
    """Should run without error on specified columns."""
    charts.hist_kde(num_df, columns=["col_a"], grid=False)


def test_hist_kde_ignores_non_numeric(num_df):
    """Should only plot numeric columns when no columns specified."""
    charts.hist_kde(num_df, grid=False)


def test_hist_kde_custom_figsize(num_df):
    """Should accept custom figsize without error."""
    charts.hist_kde(num_df, columns=["col_a"], figsize=(10, 6), grid=False)


def test_hist_kde_export_func_called(num_df):
    """Should call export_func for each column in individual mode."""
    calls = []

    def mock_export(fig, name):
        calls.append(name)

    charts.hist_kde(
        num_df, columns=["col_a", "col_b"], export_func=mock_export, grid=False
    )
    assert len(calls) == 2
    assert "hist_kde_col_a" in calls
    assert "hist_kde_col_b" in calls


def test_hist_kde_custom_prefix(num_df):
    """Should use custom export_prefix in filenames in individual mode."""
    calls = []

    def mock_export(fig, name):
        calls.append(name)

    charts.hist_kde(
        num_df,
        columns=["col_a"],
        export_func=mock_export,
        export_prefix="test",
        grid=False,
    )
    assert calls[0] == "test_col_a"


# --- hist_kde grid mode ---
def test_hist_kde_grid_runs(num_df):
    """Grid mode should run without error."""
    charts.hist_kde(num_df, grid=True)


def test_hist_kde_grid_custom_ncols(num_df):
    """Grid mode should accept custom ncols."""
    charts.hist_kde(num_df, grid=True, ncols=2)


def test_hist_kde_grid_custom_figsize(num_df):
    """Grid mode should accept custom grid_figsize."""
    charts.hist_kde(num_df, grid=True, grid_figsize=(12, 8))


def test_hist_kde_grid_export_func_called(num_df):
    """Grid mode should call export_func once with '_grid' suffix."""
    calls = []

    def mock_export(fig, name):
        calls.append(name)

    charts.hist_kde(num_df, grid=True, export_func=mock_export)
    assert len(calls) == 1
    assert calls[0] == "hist_kde_grid"


def test_hist_kde_grid_custom_prefix(num_df):
    """Grid mode should use custom export_prefix."""
    calls = []

    def mock_export(fig, name):
        calls.append(name)

    charts.hist_kde(num_df, grid=True, export_func=mock_export, export_prefix="test")
    assert calls[0] == "test_grid"


# --- outlier_boxplots grid mode ---
def test_outlier_boxplots_grid_runs(num_df):
    """Grid mode should run without error."""
    charts.outlier_boxplots(num_df, grid=True)


def test_outlier_boxplots_individual_runs(num_df):
    """Individual mode should run without error."""
    charts.outlier_boxplots(num_df, grid=False)


def test_outlier_boxplots_grid_custom_ncols(num_df):
    """Grid mode should accept custom ncols."""
    charts.outlier_boxplots(num_df, grid=True, ncols=2)


def test_outlier_boxplots_grid_custom_figsize(num_df):
    """Grid mode should accept custom grid_figsize."""
    charts.outlier_boxplots(num_df, grid=True, grid_figsize=(12, 8))


def test_outlier_boxplots_individual_custom_figsize(num_df):
    """Individual mode should accept custom figsize."""
    charts.outlier_boxplots(num_df, grid=False, figsize=(8, 5))


def test_outlier_boxplots_grid_export_func_called(num_df):
    """Grid mode should call export_func once with '_grid' suffix."""
    calls = []

    def mock_export(fig, name):
        calls.append(name)

    charts.outlier_boxplots(num_df, grid=True, export_func=mock_export)
    assert len(calls) == 1
    assert calls[0] == "boxplot_grid"


def test_outlier_boxplots_individual_export_func_called(num_df):
    """Individual mode should call export_func for each column."""
    calls = []

    def mock_export(fig, name):
        calls.append(name)

    charts.outlier_boxplots(num_df, grid=False, export_func=mock_export)
    assert len(calls) == 2


def test_outlier_boxplots_custom_prefix(num_df):
    """Should use custom export_prefix."""
    calls = []

    def mock_export(fig, name):
        calls.append(name)

    charts.outlier_boxplots(
        num_df, grid=True, export_func=mock_export, export_prefix="test"
    )
    assert calls[0] == "test_grid"
