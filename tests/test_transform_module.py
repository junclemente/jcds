import pytest
import pandas as pd
from jcds import transform as jtransform


# --- to_int ---
def test_to_int_basic(unique_test_df):
    result = jtransform.to_int(unique_test_df, columns=["Numeric"])
    assert result["Numeric"].dtype.name == "int8"


def test_to_int_missing_column_raises(unique_test_df):
    with pytest.raises(ValueError, match="Columns not found"):
        jtransform.to_int(unique_test_df, columns=["no_such_col"])


# --- to_float ---
def test_to_float_basic(unique_test_df):
    result = jtransform.to_float(unique_test_df, columns=["Numeric"])
    assert result["Numeric"].dtype.kind == "f"


def test_to_float_missing_column_raises(unique_test_df):
    with pytest.raises(ValueError, match="Columns not found"):
        jtransform.to_float(unique_test_df, columns=["no_such_col"])


# --- to_numeric ---
def test_to_numeric_basic(unique_test_df):
    result = jtransform.to_numeric(unique_test_df, columns=["Numeric"])
    assert pd.api.types.is_numeric_dtype(result["Numeric"])


def test_to_numeric_missing_column_raises(unique_test_df):
    with pytest.raises(KeyError):
        jtransform.to_numeric(unique_test_df, columns=["no_such_col"])


# --- to_str ---
def test_to_str_basic(unique_test_df):
    result = jtransform.to_str(unique_test_df, columns=["Numeric"])
    assert result["Numeric"].dtype == object


def test_to_str_missing_column_raises(unique_test_df):
    with pytest.raises(ValueError, match="Columns not found"):
        jtransform.to_str(unique_test_df, columns=["no_such_col"])


# --- to_categorical ---
def test_to_categorical_basic(unique_test_df):
    result = jtransform.to_categorical(unique_test_df, columns=["Category"])
    assert isinstance(result["Category"].dtype, pd.CategoricalDtype)


def test_to_categorical_ordered(unique_test_df):
    result = jtransform.to_categorical(
        unique_test_df, columns=["Category"], ordered=True
    )
    assert result["Category"].dtype.ordered is True


def test_to_categorical_missing_raises(sample_df):
    with pytest.raises(ValueError, match="Columns not found"):
        jtransform.to_categorical(sample_df, columns=["NoCol"])


# --- to_bool ---
def test_to_bool_basic(sample_df):
    result = jtransform.to_bool(sample_df, "Subscribed")
    assert result["Subscribed"].dtype.name == "boolean"


def test_to_bool_missing_column_raises(sample_df):
    with pytest.raises(KeyError):
        jtransform.to_bool(sample_df, "does_not_exist")


# --- to_datetime ---
def test_to_datetime_basic(datetime_df):
    result = jtransform.to_datetime(datetime_df, columns=["timestamp"])
    assert pd.api.types.is_datetime64_any_dtype(result["timestamp"])


def test_to_datetime_missing_raises(sample_df):
    with pytest.raises(KeyError):
        jtransform.to_datetime(sample_df, columns=["no_such_col"])


# --- to_object ---
def test_to_object_basic(unique_test_df):
    df_cat = jtransform.to_categorical(unique_test_df, columns=["Category"])
    result = jtransform.to_object(df_cat, columns=["Category"])
    assert result["Category"].dtype == object


def test_to_object_missing_raises(unique_test_df):
    with pytest.raises(ValueError, match="Columns not found"):
        jtransform.to_object(unique_test_df, columns=["NoCol"])


# --- clean_column_names ---
def test_clean_column_names_basic():
    df = pd.DataFrame(columns=["First Name", "Last Name", "Age"])
    result = jtransform.clean_column_names(df)
    assert list(result.columns) == ["first_name", "last_name", "age"]


def test_clean_column_names_collision():
    df = pd.DataFrame(columns=["First Name", "First  Name", "Age"])
    result = jtransform.clean_column_names(df)
    assert list(result.columns) == ["first_name", "first_name_1", "age"]


# --- rename_column ---
def test_rename_column_basic(sample_df):
    result = jtransform.rename_column(sample_df, "Age", "age")
    assert "age" in result.columns
    assert "Age" not in result.columns


def test_rename_column_missing_raises(sample_df):
    with pytest.raises(ValueError, match="not found"):
        jtransform.rename_column(sample_df, "missing_col", "new_name")


# --- delete_columns ---
def test_delete_columns_basic(sample_df):
    result = jtransform.delete_columns(sample_df, ["Age", "Income"])
    assert "Age" not in result.columns
    assert "Income" not in result.columns


def test_delete_columns_missing_raises(sample_df):
    with pytest.raises(KeyError):
        jtransform.delete_columns(sample_df, ["NotAColumn"])


# --- drop_row ---
def test_drop_row_by_position(sample_df):
    """Should drop row by position."""
    result = jtransform.drop_row(sample_df, 0)
    assert len(result) == len(sample_df) - 1
    assert sample_df.index[0] not in result.index


def test_drop_row_by_label(sample_df):
    """Should drop row by label."""
    label = sample_df.index[0]
    result = jtransform.drop_row(sample_df, label, by="label")
    assert len(result) == len(sample_df) - 1
    assert label not in result.index


def test_drop_row_does_not_mutate_original(sample_df):
    """Should not mutate original DataFrame."""
    original_len = len(sample_df)
    _ = jtransform.drop_row(sample_df, 0)
    assert len(sample_df) == original_len


def test_drop_row_inplace(sample_df):
    """Should modify DataFrame in place and return None."""
    df = sample_df.copy()
    original_len = len(df)
    ret = jtransform.drop_row(df, 0, inplace=True)
    assert ret is None
    assert len(df) == original_len - 1


def test_drop_row_invalid_label_raises(sample_df):
    """Should raise KeyError for invalid label."""
    with pytest.raises(KeyError):
        jtransform.drop_row(sample_df, 9999, by="label")


def test_drop_row_last_row(sample_df):
    """Should correctly drop last row."""
    last_label = sample_df.index[-1]
    result = jtransform.drop_row(sample_df, len(sample_df) - 1)
    assert last_label not in result.index
