def list_s3_contents(bucket_name):
    """
    Lists the contents (object keys) of a public Amazon S3 bucket using anonymous access.

    Args:
        bucket_name (str): The name of the public S3 bucket to list contents from.

    Returns:
        None. Prints the keys (filenames) of the objects found in the bucket.

    Notes:
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


def s3_file_to_dataframe(bucket_name, file_name, file_type="csv"):
    """
    Downloads a public file from an S3 bucket and loads it into a pandas DataFrame.

    Args:
        bucket_name (str): The name of the public S3 bucket.
        file_name (str): The path to the file within the bucket.
        file_type (str, optional): The type of file to load. Supported values are
            'csv' and 'excel'. Defaults to 'csv'.

    Returns:
        pd.DataFrame or None: The loaded DataFrame if successful, otherwise None.

    Notes:
        - This function assumes the file is publicly accessible via a standard S3 URL.
        - For Excel files, only `.xlsx` is supported.
        - Requires the `requests`, `pandas`, and `io` modules.
        - Prints an error message and returns None if the request fails or the file type is unsupported.
    """
    import requests
    import pandas as pd
    from io import BytesIO

    url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        if file_type == "csv":
            df = pd.read_csv(BytesIO(response.content))
        elif file_type == "excel":
            df = pd.read_excel(BytesIO(response.content))
        else:
            raise ValueError("Unsupported file type. Use 'csv' or 'excel'.")
        return df

    except Exception as e:
        print("Error loading file:", e)
        return None
