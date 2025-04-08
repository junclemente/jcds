import pandas as pd
from jcds.dataio import save_parquet, load_parquet


def test_parquet_save_and_load_roundtrip(sample_df, tmp_path):
    """Test saving and loading a Parquet file preserves DataFrame content and dtypes."""
    filepath = tmp_path / "test.parquet"

    save_parquet(sample_df, filepath)
    loaded_df = load_parquet(filepath)

    pd.testing.assert_frame_equal(sample_df, loaded_df)


def test_save_parquet_creates_nested_directories(sample_df, tmp_path):
    """Test that save_parquet creates intermediate directories if they don't exist."""
    nested_path = tmp_path / "nested" / "path" / "data.parquet"

    save_parquet(sample_df, nested_path)

    assert nested_path.exists()
    loaded_df = load_parquet(nested_path)
    pd.testing.assert_frame_equal(sample_df, loaded_df)
