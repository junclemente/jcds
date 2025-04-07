import pandas as pd
import numpy as np

def mc_confusion(cm, rnd=5):
    """
    Calculate and return various performance metrics from a confusion matrix.

    Parameters
    ----------
    cm : numpy.ndarray
        Confusion matrix as a NumPy array of any size.
    rnd : int, optional
        Number of decimal places to round the performance metrics. Default is 5.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the following calculated performance metrics for each class:
        - 'Accuracy': Proportion of correct predictions.
        - 'Error rate': Proportion of incorrect predictions.
        - 'Sensitivity (Recall)': True positive rate.
        - 'Specificity': True negative rate.
        - 'Precision': Proportion of true positives among predicted positives.
        - 'F1': Harmonic mean of precision and recall.
        - 'F2': Weighted harmonic mean of precision and recall, favoring recall.
        - 'F0.5': Weighted harmonic mean of precision and recall, favoring precision.

    Examples
    --------
    >>> from sklearn.metrics import confusion_matrix
    >>> import numpy as np
    >>> cm = np.array([[50, 10, 5],
    ...                [5, 35, 5],
    ...                [5, 10, 40]])
    >>> cm_performance(cm)

    Docstring generated with assistance from ChatGPT.
    """

    # Initialize lists to hold metrics for each class
    classes = cm.shape[0]
    metrics = ['Accuracy', 'Error rate', 'Sensitivity (Recall)', 
               'Specificity', 'Precision', 'F1', 'F2', 'F0.5']
    performance_dict = {metric: [] for metric in metrics}

    # Calculate metrics for each class
    for i in range(classes):
        TP = cm[i, i]
        FN = np.sum(cm[i, :]) - TP
        FP = np.sum(cm[:, i]) - TP
        TN = np.sum(cm) - (TP + FP + FN)

        accuracy = (TP + TN) / np.sum(cm)
        error_rate = 1 - accuracy
        sensitivity_recall = TP / (TP + FN) if (TP + FN) != 0 else 0
        specificity = TN / (TN + FP) if (TN + FP) != 0 else 0
        precision = TP / (TP + FP) if (TP + FP) != 0 else 0
        f1 = (2 * precision * sensitivity_recall) / (precision + sensitivity_recall) if (precision + sensitivity_recall) != 0 else 0
        f2 = (5 * precision * sensitivity_recall) / ((4 * precision) + sensitivity_recall) if ((4 * precision) + sensitivity_recall) != 0 else 0
        f05 = (1.25 * precision * sensitivity_recall) / ((0.25 * precision) + sensitivity_recall) if ((0.25 * precision) + sensitivity_recall) != 0 else 0

        performance_dict['Accuracy'].append(accuracy)
        performance_dict['Error rate'].append(error_rate)
        performance_dict['Sensitivity (Recall)'].append(sensitivity_recall)
        performance_dict['Specificity'].append(specificity)
        performance_dict['Precision'].append(precision)
        performance_dict['F1'].append(f1)
        performance_dict['F2'].append(f2)
        performance_dict['F0.5'].append(f05)

    # Convert to DataFrame with classes as columns
    performance_df = pd.DataFrame(performance_dict, 
                                  index=[f'Class {i}' for i in range(classes)])
    performance_df = performance_df.T.round(rnd)  # Transpose and round

    print("Confusion Matrix:")
    print(cm)
    return performance_df
