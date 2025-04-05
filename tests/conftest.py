# tests/conftest.py

import pytest
import pandas as pd
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
        mock_response.raise_for_status = lambda: None
        monkeypatch.setattr("requests.get", lambda url: mock_response)
        return mock_response
    return _mock
