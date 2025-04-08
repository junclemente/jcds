import pytest
from jcds.eda.datetime import create_dt_col


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


def test_invalid_datetime_column_name():
    import pandas as pd

    df = pd.DataFrame({"created": ["2023-01-01", "2023-02-01"]})
    with pytest.raises(ValueError, match="Column 'timestamp' not found"):
        create_dt_col(df, "timestamp", "month")


def test_invalid_col_type(datetime_df):
    with pytest.raises(ValueError, match="Unsupported col_type"):
        create_dt_col(datetime_df, "timestamp", col_type="nonsense")
