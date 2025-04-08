import pandas as pd
from pathlib import Path
from typing import Union


def save_parquet(dataframe: pd.DataFrame, filepath: Union[str, Path], **kwargs) -> None:
    """Save a DataFrame to a Parquet file.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The DataFrame to save.
    filepath : str or Path
        Destination file path.
    **kwargs
        Additional keyword arguments passed to `DataFrame.to_parquet`.

    Notes
    -----
    Automatically creates the parent directory if it doesn't exist.

    Docstring generated with assistance from ChatGPT.
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_parquet(filepath, index=False, **kwargs)


def load_parquet(filepath: Union[str, Path], **kwargs) -> pd.DataFrame:
    """Load a Parquet file into a pandas DataFrame.

    Parameters
    ----------
    filepath : str or Path
        Path to the Parquet file.
    **kwargs
        Additional keyword arguments passed to `pd.read_parquet`.

    Returns
    -------
    pd.DataFrame
        The loaded DataFrame.

    Notes
    -----
    Requires either `pyarrow` or `fastparquet` to be installed.

    Docstring generated with assistance from ChatGPT.
    """
    filepath = Path(filepath)
    return pd.read_parquet(filepath, **kwargs)
