import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics


# def plot_roc(y_test, y_pred, model_name):
#     fpr, tpr, _ = metrics.roc_curve(y_test, y_pred)
#     auc = round(metrics.roc_auc_score(y_test, y_pred), 4)
#     label = f"{model_name}, AUC={auc}"
#     # return(fpr, tpr, label)
#     plt.plot(fpr, tpr, label = label)


def plot_roc(y_true, y_score, model_name=None, ax=None, show=True):
    """
    Plot the ROC curve for a given model.

    Parameters
    ----------
    y_true : array-like
        True binary labels.
    y_score : array-like
        Predicted scores or probabilities (not hard labels).
    model_name : str, optional
        Name of the model for the legend label.
    ax : matplotlib.axes.Axes, optional
        Axis to plot on. If None, a new figure and axis will be created.
    show : bool
        Whether to call `plt.show()`. Set to False when plotting multiple curves.

    Returns
    -------
    float
        The computed AUC (Area Under the Curve) score.

    """

    fpr, tpr, _ = metrics.roc_curve(y_true, y_score)
    auc = round(metrics.roc_auc_score(y_true, y_score), 4)
    label = f"{model_name or 'Model'}, AUC={auc}"

    if ax is None:
        fig, ax = plt.subplots()

    ax.plot(fpr, tpr, label=label)
    ax.plot([0, 1], [0, 1], "k--", alpha=0.3)  # diagonal reference line
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("ROC Curve")
    ax.legend(loc="lower right")

    if show:
        plt.show()

    return auc
