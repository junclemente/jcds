import pandas as pd
from pathlib import Path
from typing import Union, Optional


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


def save_csv(dataframe: pd.DataFrame, filepath: Union[str, Path], **kwargs) -> None:
    """Save a DataFrame to a CSV file.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The DataFrame to save.
    filepath : str or Path
        Destination file path.
    **kwargs
        Additional keyword arguments passed to `DataFrame.to_csv`.

    Notes
    -----
    Automatically creates the parent directory if it doesn't exist.
    Uses `index=False` by default unless overridden.

    Docstring generated with assistance from ChatGPT.
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # Default to index=False if not explicitly passed
    if "index" not in kwargs:
        kwargs["index"] = False

    dataframe.to_csv(filepath, **kwargs)


def load_csv(
    filepath: Union[str, Path],
    encodings: Optional[list[str]] = None,
    preview_bytes: int = 300,
    **kwargs,
) -> pd.DataFrame:
    """Attempt to load a CSV using multiple encodings. If all fail, preview raw bytes.

    Parameters
    ----------
    filepath : str or Path
        Path to the CSV file.
    encodings : list of str, optional
        List of encodings to try. Defaults to common ones.
    preview_bytes : int
        Number of bytes to show if loading fails (for debugging).
    **kwargs
        Additional arguments passed to `pd.read_csv`.

    Returns
    -------
    pd.DataFrame
        Loaded DataFrame.

    Raises
    ------
    UnicodeDecodeError
        If no encoding successfully loads the file.

    Notes
    -----
    Docstring generated with assistance from ChatGPT.
    """
    filepath = Path(filepath)
    encodings = encodings or ["utf-8", "utf-8-sig", "latin1", "ISO-8859-1", "cp1252"]

    for encoding in encodings:
        try:
            dataframe = pd.read_csv(filepath, encoding=encoding, **kwargs)
            print(f"[jcds] Loaded CSV with encoding: {encoding}")
            return dataframe
        except UnicodeDecodeError:
            print(f"[jcds] Failed to load with encoding: {encoding}")
            continue
        except Exception as e:
            print(f"[jcds] Unexpected error with encoding '{encoding}': {e}")
            continue

    print(f"[jcds] ❌ Could not decode file: {filepath}")
    print(f"[jcds] Preview of raw bytes:")

    try:
        with open(filepath, "rb") as f:
            raw = f.read(preview_bytes)
            print(raw.decode("latin1", errors="replace"))  # fallback preview
    except Exception as e:
        print(f"[jcds] Also failed to read raw bytes: {e}")

    raise ValueError(
        f"[jcds] Failed to decode file {filepath} with encodings {encodings}. "
        "See preview above for troubleshooting."
    )
