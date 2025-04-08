import pytest
import pandas as pd
from pathlib import Path
from jcds.dataio import save_parquet, load_parquet, save_csv, load_csv


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


def test_load_csv_success_with_multiple_encodings(tmp_path, sample_df):
    """Test that load_csv successfully loads a CSV with non-UTF-8 encoding."""
    filepath = tmp_path / "test.csv"

    # Save with latin1 encoding (common problematic one)
    save_csv(sample_df, filepath, encoding="latin1")

    # Attempt to load without specifying encoding directly
    loaded_df = load_csv(filepath)

    pd.testing.assert_frame_equal(sample_df, loaded_df)


def test_load_csv_fallback_shows_preview(tmp_path, capsys):
    """Test that load_csv shows raw byte preview when it cannot decode the file."""
    filepath = tmp_path / "broken.csv"

    # Write invalid binary content that won't parse into a CSV
    filepath.write_bytes(b"\xff\xfe\x00\x00BAD DATA\n\x81\x82\x83")

    # Patch the encoding list to only try encodings that should fail
    with pytest.raises(ValueError, match="Failed to decode file"):
        load_csv(
            filepath, encodings=["utf-8"]
        )  # Force failure, don't let it try latin1

    captured = capsys.readouterr()
    assert "Could not decode file" in captured.out
    assert "Preview of raw bytes" in captured.out
