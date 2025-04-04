import pandas as pd
import numpy as np


def create_sample_dataset():
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


def create_na_test_df():
    return pd.DataFrame(
        {
            "A": [1, 2, np.nan, 4],
            "B": [np.nan, np.nan, np.nan, 4],
            "C": [1, 2, 3, 4],
            "D": [np.nan, np.nan, np.nan, np.nan],
        }
    )


def create_unique_test_df():
    return pd.DataFrame(
        {
            "Category": ["A", "B", "A", "C", "B"],
            "Numeric": [1, 2, 2, 3, 3],
            "Empty": [None, None, None, None, None],
            "Mixed": [1, "1", 1.0, "1.0", None],
        }
    )


def create_binary_list_df():
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
