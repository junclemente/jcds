import pytest
import pandas as pd
from pathlib import Path
from jcds.dataio import save_parquet, load_parquet, save_csv, load_csv
from jcds.dataio.s3_io import read_s3


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


def test_read_s3_csv_success(sample_df, mock_requests_get):
    """Test reading a CSV file from S3 using mocked response."""
    # Convert the sample DataFrame to CSV bytes
    csv_bytes = sample_df.to_csv(index=False).encode("utf-8")

    # Patch requests.get to return a mock response with the CSV content
    mock_requests_get(content_bytes=csv_bytes)

    # Act
    df = read_s3("mock-bucket", "mock-file.csv", file_type="csv")

    # Assert
    pd.testing.assert_frame_equal(df, sample_df)


def test_read_s3_excel_success(dummy_excel_bytes, mock_requests_get):
    """Test reading an Excel file from S3 using mocked response."""
    mock_requests_get(content_bytes=dummy_excel_bytes)

    df = read_s3("mock-bucket", "mock-file.xlsx", file_type="excel")

    # Check for expected shape (from conftest.py)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["A", "B"]


def test_read_s3_unsupported_file_type(mock_requests_get):
    """Test that read_s3 raises ValueError for unsupported file types."""
    mock_requests_get(content_bytes=b"some content")

    with pytest.raises(ValueError, match="Unsupported file type"):
        read_s3("mock-bucket", "mock-file.txt", file_type="txt")


def test_read_s3_request_failure(mock_requests_get):
    """Test that read_s3 returns None on failed request."""
    mock_requests_get(content_bytes=b"", status_code=404)

    df = read_s3("mock-bucket", "nonexistent.csv", file_type="csv")
    assert df is None
