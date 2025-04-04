import pandas as pd
import numpy as np
import pytest

from jcds import eda
from tests.unit.test_utils import (
    create_sample_dataset,
    create_na_test_df,
    create_unique_test_df,
    create_binary_list_df,
)


@pytest.fixture
def sample_df():
    return create_sample_dataset()


@pytest.fixture
def na_test_df():
    return create_na_test_df()


@pytest.fixture
def unique_test_df():
    return create_unique_test_df()


@pytest.fixture
def binary_list_df():
    return create_binary_list_df()


def test_show_shape_returns_correct_shape(sample_df):
    rows, cols = eda.show_shape(sample_df)
    assert rows == 10
    assert cols == 5


def test_show_dupes_returns_zero_for_clean_samples(sample_df):
    assert eda.show_dupes(sample_df) == 0


def test_show_catvar_returns_object_columns(sample_df):
    cat_vars = eda.show_catvar(sample_df)
    assert "Gender" in cat_vars
    assert "Age" not in cat_vars
    assert isinstance(cat_vars, list)


def test_show_convar_returns_numerical_columns(sample_df):
    con_vars = eda.show_convar(sample_df)
    assert "ID" in con_vars
    assert "Subscribed" in con_vars
    assert "Gender" not in con_vars
    assert isinstance(con_vars, list)


def test_show_lowcardvars_filters_by_cardinality():
    df = pd.DataFrame(
        {
            "City": ["NY", "LA", "SF", "NY", "LA"],
            "State": ["NY", "CA", "CA", "NY", "CA"],
            "Zip": ["10001", "90001", "94101", "10001", "90001"],
            "ID": [1, 2, 3, 4, 5],
        }
    )

    result = eda.show_lowcardvars(df, max_unique=3)
    assert isinstance(result, list)
    assert ("City", 3) in result
    assert ("State", 2) in result
    assert ("Zip", 3) in result
    assert not any(col for col in result if col[0] == "ID")  # Not a cat var


def test_count_rows_with_any_na(na_test_df):
    assert eda.count_rows_with_any_na(na_test_df) == 4


def test_count_rows_with_all_na(na_test_df):
    assert eda.count_rows_with_all_na(na_test_df) == 0


def test_count_cols_with_any_na(na_test_df):
    assert eda.count_cols_with_any_na(na_test_df) == 3


def test_count_cols_with_all_na(na_test_df):
    assert eda.count_cols_with_all_na(na_test_df) == 1


def test_count_total_na(na_test_df):
    assert eda.count_total_na(na_test_df) == 8


def test_count_unique_values_basic():
    df = pd.DataFrame(
        {
            "Category": ["A", "B", "A", "C", "B"],
            "Numeric": [1, 2, 2, 3, 3],
        }
    )
    result = eda.count_unique_values(df, ["Category", "Numeric"])
    assert result["Category"] == 3
    assert result["Numeric"] == 3


def test_count_unique_values_with_empty_column():
    df = pd.DataFrame({"Empty": [None, None, None, None]})
    result = eda.count_unique_values(df, ["Empty"])
    assert result["Empty"] == 1  # NaNs included with dropna=False


def test_count_unique_values_with_mixed_types():
    df = pd.DataFrame({"Mixed": [1, "1", 1.0, "1.0", None]})
    result = eda.count_unique_values(df, ["Mixed"])
    assert result["Mixed"] == 4  # 1, "1", 1.0, "1.0", None


def test_show_binary_list(binary_list_df):
    result = eda.show_binary_list(binary_list_df)

    # Structure checks
    assert isinstance(result, dict)
    assert "binary_columns" in result
    assert "binary_with_nan" in result

    # Content checks
    expected_binary = {"bin_clean"}
    expected_binary_with_nan = {"bin_with_nan"}

    assert set(result["binary_columns"]) == expected_binary
    assert set(result["binary_with_nan"]) == expected_binary_with_nan

    # Ensure non-binary cols are not falsely included
    excluded = {"not_bin_3vals", "not_bin_unique", "all_nan"}
    combined_results = set(result["binary_columns"]) | set(result["binary_with_nan"])
    assert excluded.isdisjoint(
        combined_results
    ), "Non-binary columns should not appear in the result"
