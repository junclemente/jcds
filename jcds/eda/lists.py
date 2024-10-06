import pandas as pd
import numpy as np

def cat_list(dataframe):
    list = dataframe.select_dtypes(include=['category', 'object']).columns.tolist()
    return list

def cont_list(dataframe):
    list = dataframe.select_dtypes(exclude=['category', 'object']).columns.tolist()
    return list