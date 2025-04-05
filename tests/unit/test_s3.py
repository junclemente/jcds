import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from io import BytesIO

from jcds.aws.s3 import list_s3_contents, s3_file_to_dataframe


@patch("boto3.client")
def test_list_s3_contents_success(mock_boto_client, capsys):
    # Mock S3 client and response
    mock_s3 = MagicMock()
    mock_s3.list_objects_v2.return_value = {
        "Contents": [{"Key": "file1.csv"}, {"Key": "file2.csv"}]
    }
    mock_boto_client.return_value = mock_s3

    list_s3_contents("dummy-bucket")

    captured = capsys.readouterr()
    assert "file1.csv" in captured.out
    assert "file2.csv" in captured.out
    mock_s3.list_objects_v2.assert_called_once_with(Bucket="dummy-bucket")


@patch("requests.get")
def test_s3_file_to_dataframe_csv(mock_get):
    # Mock CSV response
    csv_data = b"col1,col2\nval1,val2"
    mock_response = MagicMock()
    mock_response.content = csv_data
    mock_response.status_code = 200
    mock_response.raise_for_status = lambda: None
    mock_get.return_value = mock_response

    df = s3_file_to_dataframe("dummy-bucket", "file.csv", file_type="csv")
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]["col1"] == "val1"


@patch("requests.get")
def test_s3_file_to_dataframe_excel(mock_get):
    # Mock Excel response
    excel_df = pd.DataFrame({"A": [1], "B": [2]})
    buffer = BytesIO()
    excel_df.to_excel(buffer, index=False)
    buffer.seek(0)

    mock_response = MagicMock()
    mock_response.content = buffer.read()
    mock_response.status_code = 200
    mock_response.raise_for_status = lambda: None
    mock_get.return_value = mock_response

    df = s3_file_to_dataframe("dummy-bucket", "file.xlsx", file_type="excel")
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]["A"] == 1


@patch("requests.get")
def test_s3_file_to_dataframe_invalid_type(mock_get, capsys):
    df = s3_file_to_dataframe("dummy-bucket", "file.txt", file_type="txt")
    captured = capsys.readouterr()
    assert df is None
    assert "Unsupported file type" in captured.out or "Error loading file" in captured.out
