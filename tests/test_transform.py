import pandas as pd
import pandas.testing as pdt
import pytest
from jcds.eda.transform import rename_col, delete_columns


def test_rename_existing_column(sample_df):
    sample_df["old_name"] = sample_df.pop("Gender")

    result = rename_col(sample_df, "old_name", "new_name")

    assert "new_name" in result.columns
    assert "old_name" not in result.columns
    pd.testing.assert_series_equal(
        result["new_name"], sample_df["old_name"], check_names=False
    )


def test_rename_column_does_not_mutate_original(sample_df):
    sample_df["old_name"] = sample_df.pop("Gender")
    _ = rename_col(sample_df, "old_name", "new_name")

    assert "old_name" in sample_df.columns or "Gender" in sample_df.columns
    assert "new_name" not in sample_df.columns


def test_rename_missing_column_raises_error(sample_df):
    with pytest.raises(ValueError, match="Column 'missing_col' not found"):
        rename_col(sample_df, "missing_col", "new_name")


def test_delete_columns_returns_new_dataframe(sample_df):
    # non‑inplace drop: returns a new DF, original untouched
    df = sample_df
    result = delete_columns(df, ["Age", "Income"], inplace=False)

    # original still has all columns
    assert set(df.columns) == {"ID", "Age", "Gender", "Income", "Subscribed"}

    # result has dropped the two columns
    assert isinstance(result, pd.DataFrame)
    assert set(result.columns) == {"ID", "Gender", "Subscribed"}
    assert result.shape == (10, 3)


def test_delete_columns_inplace(sample_df):
    # inplace drop: modifies the fixture
    df = sample_df
    ret = delete_columns(df, ["Age", "Income"], inplace=True)

    # returns None when inplace
    assert ret is None

    # fixture DataFrame now missing those columns
    assert set(df.columns) == {"ID", "Gender", "Subscribed"}


def test_delete_no_columns_returns_copy(missing_data_df):
    # dropping an empty list should return a copy with identical columns
    df = missing_data_df
    result = delete_columns(df, [], inplace=False)

    assert list(result.columns) == list(df.columns)
    # ensure it's a new object
    assert result is not df
    pdt.assert_frame_equal(result, df)


def test_delete_all_columns(empty_col_df):
    # dropping the only column yields a DataFrame with zero columns
    df = empty_col_df
    result = delete_columns(df, ["Empty"], inplace=False)

    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == []
    # same number of rows, zero columns
    assert result.shape[0] == df.shape[0]
    assert result.shape[1] == 0


def test_delete_columns_raises_keyerror(sample_df):
    # attempting to drop a non-existent column raises KeyError
    with pytest.raises(KeyError):
        delete_columns(sample_df, ["NotAColumn"], inplace=False)
