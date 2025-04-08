import pytest
import pandas as pd
from jcds.eda.datetime import create_dt_col, create_dt_cols


def test_create_month_col(datetime_df):
    result = create_dt_col(datetime_df, "timestamp", col_type="month")
    assert "timestamp_month" in result.columns
    assert result["timestamp_month"].tolist() == [1, 2, 3, 4, 5, 6]


def test_create_weekday_name_col(datetime_df):
    result = create_dt_col(datetime_df, "timestamp", col_type="weekday_name")
    assert "timestamp_weekday_name" in result.columns
    assert result["timestamp_weekday_name"].tolist() == [
        "Sunday",
        "Tuesday",
        "Wednesday",
        "Saturday",
        "Tuesday",
        "Saturday",
    ]


def test_create_multiple_components(datetime_df):
    result = create_dt_cols(datetime_df, "timestamp", ["year", "month", "weekday"])
    assert "timestamp_year" in result.columns
    assert "timestamp_month" in result.columns
    assert "timestamp_weekday" in result.columns
    assert result.shape[1] == datetime_df.shape[1] + 3


def test_invalid_col_type(datetime_df):
    with pytest.raises(ValueError, match="Unsupported col_type"):
        create_dt_col(datetime_df, "timestamp", col_type="nonsense")


def test_invalid_col_type_multiple(datetime_df):
    with pytest.raises(ValueError, match="Unsupported col_type"):
        create_dt_cols(datetime_df, "timestamp", ["month", "invalid"])


def test_invalid_datetime_column_name():
    df = pd.DataFrame({"created": ["2023-01-01", "2023-02-01"]})
    with pytest.raises(ValueError, match="Column 'timestamp' not found"):
        create_dt_col(df, "timestamp", "month")


def test_non_datetime_input_conversion():
    df = pd.DataFrame({"timestamp": ["2023-01-01", "2023-02-15"]})
    result = create_dt_col(df, "timestamp", "year")
    assert "timestamp_year" in result.columns
    assert result["timestamp_year"].tolist() == [2023, 2023]
