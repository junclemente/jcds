# tests/test_reports.py
import pytest
import pandas as pd
import numpy as np
import matplotlib

matplotlib.use("Agg")  # non-interactive backend for testing
from jcds import reports as jrep


@pytest.fixture
def outlier_df():
    """DataFrame with known outliers for testing."""
    return pd.DataFrame(
        {
            "col_a": [1, 2, 3, 4, 5, 100],  # 100 is an outlier
            "col_b": [10, 20, 30, 40, 50, 60],  # no outliers
            "col_c": [1, 1, 1, 1, 1, 1000],  # 1000 is an outlier
        }
    )


# --- outliers report ---
def test_outliers_runs_without_error(outlier_df):
    """Should run without error."""
    jrep.outliers(outlier_df)


def test_outliers_custom_threshold(outlier_df):
    """Should accept custom threshold."""
    jrep.outliers(outlier_df, threshold=3.0)


def test_outliers_horizontal_orient(outlier_df):
    """Should run without error with horizontal orientation."""
    jrep.outliers(outlier_df, orient="h")


def test_outliers_vertical_orient(outlier_df):
    """Should run without error with vertical orientation."""
    jrep.outliers(outlier_df, orient="v")


def test_outliers_export_func_called(outlier_df):
    """Should call export_func when provided."""
    calls = []

    def mock_export(fig, name):
        calls.append(name)

    jrep.outliers(outlier_df, export_func=mock_export)
    assert len(calls) == 1
    assert calls[0] == "outlier_report_grid"


def test_outliers_custom_export_prefix(outlier_df):
    """Should use custom export_prefix."""
    calls = []

    def mock_export(fig, name):
        calls.append(name)

    jrep.outliers(outlier_df, export_func=mock_export, export_prefix="test")
    assert calls[0] == "test_grid"
