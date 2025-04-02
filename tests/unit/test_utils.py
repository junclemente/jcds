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
