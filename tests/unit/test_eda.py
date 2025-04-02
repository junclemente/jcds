import pandas as pd
import numpy as np
import pytest

from jcds import eda
from tests.unit.test_utils import create_sample_dataset


@pytest.fixture
def sample_df():
    return create_sample_dataset()


def test_show_shape_returns_correct_shape(sample_df):
    rows, cols = eda.show_shape(sample_df)
    assert rows == 5
    assert cols == 3


def test_get_column_types_returns_correct_types(sample_df):
    col_types = eda.get_column_types(sample_df)
    expected_types = {
        "name": "object",
        "age": "int64",
        "score": "float64",
    }
    assert col_types == expected_types


def test_show_missing_returns_zero_for_clean_data(sample_df):
    missing = eda.show_missing(sample_df)
    assert isinstance(missing, pd.DataFrame)
    assert missing["missing_count"].sum() == 0
