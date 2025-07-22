def list_s3_bucket(bucket_name):
    """
    List the contents (object keys) of a public Amazon S3 bucket using anonymous access.

    Parameters
    ----------
    bucket_name : str
        The name of the public S3 bucket to list contents from.

    Returns
    -------
    None
        Prints the keys (filenames) of the objects found in the bucket.

    Notes
    -----
    - This function uses anonymous (unsigned) access and works only with public buckets.
    - Requires the `boto3` and `botocore` libraries.
    - If the bucket is not public or an error occurs, an error message is printed.

    """

    try:
        import boto3
        from botocore import UNSIGNED
        from botocore.config import Config
    except ImportError as e:
        print("Required library is not installed:", e)
        return

    # create anonymous s3 client
    s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        for obj in response.get("Contents", []):
            print(obj["Key"])
    except Exception as e:
        print("Error accessing bucket:", e)
