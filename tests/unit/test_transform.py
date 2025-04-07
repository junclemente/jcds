import pandas as pd
import pytest
from jcds.eda.transform import rename_col
from tests.unit.test_utils import create_sample_dataset


@pytest.fixture
def sample_df():
    return create_sample_dataset()


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
