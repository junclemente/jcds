import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics 


def plot_roc(y_test, y_pred, model_name):
    fpr, tpr, _ = metrics.roc_curve(y_test, y_pred)
    auc = round(metrics.roc_auc_score(y_test, y_pred), 4)
    label = f"{model_name}, AUC={auc}"
    # return(fpr, tpr, label)
    plt.plot(fpr, tpr, label = label)
