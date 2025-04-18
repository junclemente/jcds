# tests/test_transform.py
import pytest
import pandas as pd
import pandas.testing as pdt
from pandas.api.types import is_categorical_dtype
from jcds.eda.transform import (
    rename_column,
    delete_columns,
    convert_to_int,
    convert_to_categorical,
    convert_to_object,
)


# --- rename_column tests ---
def test_rename_existing_column(sample_df):
    # attach a new column name from existing
    df = sample_df.copy()
    df["old_name"] = df.pop("Gender")
    result = rename_column(df, "old_name", "new_name")
    assert "new_name" in result.columns
    assert "old_name" not in result.columns


def test_rename_does_not_mutate_original(sample_df):
    df = sample_df.copy()
    df["old_name"] = df.pop("Gender")
    _ = rename_column(df, "old_name", "new_name")
    # original df still has old_name
    assert "old_name" in df.columns
    assert "new_name" not in df.columns


def test_rename_missing_column_raises(sample_df):
    with pytest.raises(ValueError, match="Column 'missing_col' not found"):
        rename_column(sample_df, "missing_col", "new_name")


# --- delete_columns tests ---
def test_delete_columns_returns_new_dataframe(sample_df):
    df = sample_df.copy()
    result = delete_columns(df, ["Age", "Income"], inplace=False)
    # original unchanged
    assert set(df.columns) == {"ID", "Age", "Gender", "Income", "Subscribed"}
    # result dropped correctly
    assert set(result.columns) == {"ID", "Gender", "Subscribed"}


def test_delete_columns_inplace(sample_df):
    df = sample_df.copy()
    ret = delete_columns(df, ["Age", "Income"], inplace=True)
    assert ret is None
    assert set(df.columns) == {"ID", "Gender", "Subscribed"}


def test_delete_no_columns_returns_copy(missing_data_df):
    df = missing_data_df
    result = delete_columns(df, [], inplace=False)
    assert list(result.columns) == list(df.columns)
    assert result is not df
    pdt.assert_frame_equal(result, df)


def test_delete_all_columns(empty_col_df):
    df = empty_col_df
    result = delete_columns(df, ["Empty"], inplace=False)
    assert list(result.columns) == []
    assert result.shape[0] == df.shape[0]


def test_delete_columns_raises_keyerror(sample_df):
    with pytest.raises(KeyError):
        delete_columns(sample_df, ["NotAColumn"], inplace=False)


# --- convert_to_int tests ---
def test_downcast_integer(unique_test_df):
    df2 = convert_to_int(
        unique_test_df, columns=["Numeric"], unsigned=False, inplace=False
    )
    assert df2["Numeric"].dtype.name == "int8"
    # original unchanged
    assert unique_test_df["Numeric"].dtype.name == "int64"


def test_downcast_unsigned(unique_test_df):
    df2 = convert_to_int(
        unique_test_df, columns=["Numeric"], unsigned=True, inplace=False
    )
    assert df2["Numeric"].dtype.name == "uint8"


def test_default_downcast_all_numeric(unique_test_df):
    df2 = convert_to_int(unique_test_df, columns=None, inplace=False)
    assert df2["Numeric"].dtype.name == "int8"
    assert df2["Category"].dtype == unique_test_df["Category"].dtype


def test_convert_to_int_missing_column_raises(unique_test_df):
    with pytest.raises(ValueError, match="Columns not found"):
        convert_to_int(unique_test_df, columns=["no_such_col"], inplace=False)


def test_errors_raise_on_bad(mixed_type_df):
    with pytest.raises(ValueError):
        convert_to_int(
            mixed_type_df, columns=["more_mixed"], errors="raise", inplace=False
        )


def test_errors_coerce_on_bad(mixed_type_df):
    dfc = convert_to_int(
        mixed_type_df, columns=["more_mixed"], errors="coerce", inplace=False
    )
    assert dfc["more_mixed"].isna().sum() == 1
    assert dfc["more_mixed"].dtype.kind == "f"


def test_convert_to_int_inplace(unique_test_df):
    df = unique_test_df.copy()
    ret = convert_to_int(df, columns=["Numeric"], inplace=True)
    assert ret is None
    assert df["Numeric"].dtype.name == "int8"


# --- convert_to_categorical tests ---
def test_default_convert_to_categorical(unique_test_df):
    df2 = convert_to_categorical(unique_test_df, columns=None, inplace=False)
    for col in ["Category", "Empty", "Mixed"]:
        assert is_categorical_dtype(df2[col].dtype), f"{col} not categorical"
    assert df2["Numeric"].dtype == unique_test_df["Numeric"].dtype


def test_ordered_convert_to_categorical(unique_test_df):
    df2 = convert_to_categorical(
        unique_test_df, columns=["Category"], ordered=True, inplace=False
    )
    dtype = df2["Category"].dtype
    assert is_categorical_dtype(dtype)
    assert dtype.ordered is True


def test_convert_to_categorical_missing_raises(sample_df):
    with pytest.raises(ValueError, match="Columns not found"):
        convert_to_categorical(sample_df, columns=["NoCol"], inplace=False)


def test_convert_to_categorical_inplace(unique_test_df):
    df = unique_test_df.copy()
    ret = convert_to_categorical(df, columns=["Category"], inplace=True)
    assert ret is None
    assert is_categorical_dtype(df["Category"].dtype)


# --- convert_to_object tests ---
def test_convert_to_object_after_categorical(unique_test_df):
    df_cat = convert_to_categorical(unique_test_df, columns=["Category"], inplace=False)
    df_obj = convert_to_object(df_cat, columns=["Category"], inplace=False)
    assert df_obj["Category"].dtype == object


def test_convert_to_object_missing_raises(unique_test_df):
    with pytest.raises(ValueError, match="Columns not found"):
        convert_to_object(unique_test_df, columns=["NoCol"], inplace=False)


def test_convert_to_object_inplace(unique_test_df):
    df_cat = convert_to_categorical(unique_test_df, columns=["Category"], inplace=False)
    ret = convert_to_object(df_cat, columns=["Category"], inplace=True)
    assert ret is None
    assert df_cat["Category"].dtype == object
