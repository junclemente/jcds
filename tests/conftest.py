# tests/conftest.py

import pytest
import pandas as pd
import numpy as np
from io import BytesIO
from unittest.mock import MagicMock


@pytest.fixture
def dummy_csv_bytes():
    """Returns CSV content in bytes format (mimics downloaded file)."""
    csv_data = "col1,col2\nval1,val2\nval3,val4"
    return csv_data.encode("utf-8")


@pytest.fixture
def dummy_excel_bytes():
    """Returns Excel file content in bytes format."""
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)
    return buffer.read()


@pytest.fixture
def mock_requests_get(monkeypatch):
    """Patch `requests.get` to return a mocked response object."""

    def _mock(content_bytes, status_code=200):
        mock_response = MagicMock()
        mock_response.content = content_bytes
        mock_response.status_code = status_code

        if status_code >= 400:

            def raise_for_status():
                raise requests.HTTPError(f"Mocked HTTP {status_code} error")

        else:

            def raise_for_status():
                return None

        mock_response.raise_for_status = raise_for_status
        monkeypatch.setattr("requests.get", lambda url: mock_response)
        return mock_response

    return _mock


@pytest.fixture
def sample_df():
    data = {
        "ID": range(1, 11),
        "Age": [25, 32, 47, 51, 38, 29, np.nan, 45, 33, 26],
        "Gender": [
            "Male",
            "Female",
            "Female",
            "Male",
            "Female",
            "Male",
            "Female",
            np.nan,
            "Male",
            "Female",
        ],
        "Income": [
            50000,
            60000,
            55000,
            62000,
            np.nan,
            52000,
            49000,
            58000,
            60000,
            61000,
        ],
        "Subscribed": [1, 0, 1, 1, 0, 0, 1, 0, 1, 1],
    }
    return pd.DataFrame(data)


@pytest.fixture
def na_test_df():
    return pd.DataFrame(
        {
            "A": [1, 2, np.nan, 4],
            "B": [np.nan, np.nan, np.nan, 4],
            "C": [1, 2, 3, 4],
            "D": [np.nan, np.nan, np.nan, np.nan],
        }
    )


@pytest.fixture
def unique_test_df():
    return pd.DataFrame(
        {
            "Category": ["A", "B", "A", "C", "B"],
            "Numeric": [1, 2, 2, 3, 3],
            "Empty": [None, None, None, None, None],
            "Mixed": [1, "1", 1.0, "1.0", None],
        }
    )


@pytest.fixture
def binary_list_df():
    # Create test DataFrame
    df = pd.DataFrame(
        {
            "bin_clean": ["Yes", "No", "Yes", "No"],
            "bin_with_nan": ["Yes", "No", None, "Yes"],
            "not_bin_3vals": ["Yes", "No", "Maybe", "Yes"],
            "not_bin_unique": [1, 2, 3, 4],
            "all_nan": [None, None, None, None],
        }
    )
    return df


@pytest.fixture
def datetime_df():
    return pd.DataFrame(
        {
            "timestamp": [
                "2023-01-01",
                "2023-02-14",
                "2023-03-15",
                "2023-04-22",
                "2023-05-30",
                "2023-06-17",
            ]
        }
    )
