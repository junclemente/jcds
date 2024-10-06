import pandas as pd
import numpy as np

def get_cat_list(dataframe):
    list = dataframe.select_dtypes(include=['category', 'object']).columns.tolist()
    return list

def get_cont_list(dataframe):
    list = dataframe.select_dtypes(exclude=['category', 'object']).columns.tolist()
    return list