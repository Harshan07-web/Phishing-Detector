import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_true, y_pred, labels=None, title="Confusion Matrix", show_plot=True):
    """
    Generate and display a confusion matrix for model predictions.

    Args:
        y_true (list or array): True labels.
        y_pred (list or array): Predicted labels.
        labels (list): Optional label names. Defaults to ['Legitimate', 'Phishing'].
        title (str): Title for the plot.
        show_plot (bool): Whether to display the plot immediately.

    Returns:
        matrix (ndarray): Confusion matrix array.
    """
    if labels is None:
        labels = ['Legitimate', 'Phishing']

    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.title(title)
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.tight_layout()

    if show_plot:
        plt.show()

    return cm
