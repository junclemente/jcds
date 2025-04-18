import pandas as pd
import pandas.testing as pdt
import pytest
from jcds.eda.transform import rename_col, delete_columns, convert_to_int


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



def test_downcast_integer(unique_test_df):
    """Converting a known int column yields the smallest signed int dtype."""
    df2 = convert_to_int(
        unique_test_df, columns=["Numeric"], unsigned=False, inplace=False
    )
    assert isinstance(df2, pd.DataFrame)
    # should downcast to int8
    assert df2["Numeric"].dtype.name == "int8"
    # original fixture still int64
    assert unique_test_df["Numeric"].dtype.name == "int64"


def test_downcast_unsigned(unique_test_df):
    """With unsigned=True, we get an unsigned integer dtype."""
    df2 = convert_to_int(
        unique_test_df, columns=["Numeric"], unsigned=True, inplace=False
    )
    assert df2["Numeric"].dtype.name == "uint8"


def test_default_downcast_all_numeric(unique_test_df):
    """columns=None should downcast all numeric columns (here just 'Numeric')."""
    df2 = convert_to_int(unique_test_df, columns=None, inplace=False)
    assert df2["Numeric"].dtype.name == "int8"
    # non‑numeric columns untouched
    assert df2["Category"].dtype == unique_test_df["Category"].dtype


def test_missing_column_raises(unique_test_df):
    """Specifying a nonexistent column must raise ValueError."""
    with pytest.raises(ValueError) as ei:
        convert_to_int(unique_test_df, columns=["no_such_col"], inplace=False)
    assert "Columns not found" in str(ei.value)


def test_errors_raise_on_bad(mixed_type_df):
    """errors='raise' should bubble up a ValueError for truly unparseable values."""
    with pytest.raises(ValueError):
        convert_to_int(
            mixed_type_df, columns=["more_mixed"], errors="raise", inplace=False
        )


def test_errors_coerce_on_bad(mixed_type_df):
    """errors='coerce' turns bad parses into NaN (and dtype float)."""
    df_coerced = convert_to_int(
        mixed_type_df, columns=["more_mixed"], errors="coerce", inplace=False
    )
    # exactly one bad value ("True") becomes NaN
    assert df_coerced["more_mixed"].isna().sum() == 1
    # coerce yields float type because of NaN
    assert df_coerced["more_mixed"].dtype.kind == "f"


def test_inplace_modification(unique_test_df):
    """inplace=True returns None and mutates the passed DataFrame."""
    df = unique_test_df.copy()
    ret = convert_to_int(df, columns=["Numeric"], inplace=True)
    assert ret is None
    assert df["Numeric"].dtype.name == "int8"
