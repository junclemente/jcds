# tests/unit/test_s3_utils.py

from jcds.aws.s3_utils import list_s3_bucket


def test_list_s3_bucket_prints_keys(monkeypatch, capsys):
    """Test that list_s3_bucket prints keys for a mock public bucket."""

    # Mock S3 client and its list_objects_v2 method
    class MockS3Client:
        def list_objects_v2(self, Bucket):
            return {"Contents": [{"Key": "file1.csv"}, {"Key": "file2.csv"}]}

    # Patch boto3.client to return our mock S3 client
    monkeypatch.setattr("boto3.client", lambda *args, **kwargs: MockS3Client())

    list_s3_bucket("mock-bucket")
    captured = capsys.readouterr()
    assert "file1.csv" in captured.out
    assert "file2.csv" in captured.out
