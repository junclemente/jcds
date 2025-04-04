import pandas as pd
import numpy as np
import pytest

from jcds import eda
from tests.unit.test_utils import create_sample_dataset, create_na_test_df


@pytest.fixture
def sample_df():
    return create_sample_dataset()


@pytest.fixture
def na_test_df():
    return create_na_test_df()


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


# def test_get_column_types_returns_correct_types(sample_df):
#     col_types = eda.get_column_types(sample_df)
#     expected = {
#         "ID": "int64",
#         "Age": "float64",
#         "Gender": "object",
#         "Income": "float64",
#         "Subscribed": "int64",
#     }
#     assert col_types == expected


# def test_show_missing_counts(sample_df):
#     missing = eda.show_missing(sample_df)
#     assert isinstance(missing, pd.DataFrame)
#     assert missing.loc["Age", "missing_count"] == 1
#     assert missing.loc["Gender", "missing_count"] == 1
#     assert missing.loc["Income", "missing_count"] == 1
