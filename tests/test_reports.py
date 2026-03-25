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


# --- show_dtypes ---
def test_show_dtypes_full_dataset_runs(sample_df):
    """Should run without error on full dataset."""
    jrep.show_dtypes(sample_df)


def test_show_dtypes_full_dataset_shows_mixed(capsys):
    """Should flag mixed type columns in full dataset mode."""
    df = pd.DataFrame(
        {
            "clean": [1, 2, 3],
            "mixed": [1, "one", 1.0],
        }
    )
    jrep.show_dtypes(df)
    captured = capsys.readouterr()
    assert "MIXED TYPE COLUMNS" in captured.out
    assert "mixed" in captured.out


def test_show_dtypes_full_dataset_no_mixed(capsys, sample_df):
    """Should show 0 mixed type columns for clean dataset."""
    jrep.show_dtypes(sample_df)
    captured = capsys.readouterr()
    assert "MIXED TYPE COLUMNS: 0" in captured.out


def test_show_dtypes_column_runs(sample_df):
    """Should run without error on a single column."""
    jrep.show_dtypes(sample_df, column="Gender")


def test_show_dtypes_column_shows_breakdown(capsys):
    """Should show type breakdown for a mixed column."""
    df = pd.DataFrame(
        {
            "mixed": [1, "one", 1.0, None],
        }
    )
    jrep.show_dtypes(df, column="mixed")
    captured = capsys.readouterr()
    assert "DTYPE REPORT: 'mixed'" in captured.out
    assert "Value breakdown by type" in captured.out


def test_show_dtypes_column_not_found(capsys, sample_df):
    """Should print error message for missing column."""
    jrep.show_dtypes(sample_df, column="nonexistent")
    captured = capsys.readouterr()
    assert "not found" in captured.out


def test_show_dtypes_column_shows_offending_values(capsys):
    """Should show offending non-dominant type values."""
    df = pd.DataFrame(
        {
            "mixed": ["a", "b", "c", 999],
        }
    )
    jrep.show_dtypes(df, column="mixed")
    captured = capsys.readouterr()
    assert "999" in captured.out


def test_show_dtypes_full_shows_all_columns(capsys, sample_df):
    """Should list all columns in the detail section."""
    jrep.show_dtypes(sample_df)
    captured = capsys.readouterr()
    for col in sample_df.columns:
        assert col in captured.out
