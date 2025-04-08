import pandas as pd
import requests
from io import BytesIO


def read_s3(bucket_name: str, file_name: str, file_type: str = "csv") -> pd.DataFrame:
    """Download a public file from an S3 bucket and load it into a pandas DataFrame.

    Parameters
    ----------
    bucket_name : str
        The name of the public S3 bucket.
    file_name : str
        The path to the file within the bucket.
    file_type : str, optional
        The type of file to load. Supported values are 'csv' and 'excel'. Defaults to 'csv'.

    Returns
    -------
    pd.DataFrame or None
        The loaded DataFrame if successful, otherwise None.

    Notes
    -----
    - This function assumes the file is publicly accessible via a standard S3 URL.
    - For Excel files, only `.xlsx` is supported.
    - Requires the `requests`, `pandas`, and `io` modules.
    - Prints an error message and returns None if the request fails or the file type is unsupported.

    Docstring generated with assistance from ChatGPT.
    """
    url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        if file_type == "csv":
            dataframe = pd.read_csv(BytesIO(response.content))
        elif file_type == "excel":
            dataframe = pd.read_excel(BytesIO(response.content))
        else:
            raise ValueError("Unsupported file type. Use 'csv' or 'excel'.")
        return dataframe

    except ValueError:
        raise  # Let unsupported type errors propagate for testing

    except Exception as e:
        print(f"[jcds] Error loading file from S3: {e}")
        return None
