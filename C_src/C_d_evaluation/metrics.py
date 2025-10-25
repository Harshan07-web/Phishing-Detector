from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report

def evaluate_model(y_true, y_pred, y_proba=None):
    """
    Compute key evaluation metrics for a phishing detection model.

    Args:
        y_true (array-like): True labels.
        y_pred (array-like): Predicted labels (0 or 1).
        y_proba (array-like, optional): Predicted probabilities for positive class.

    Returns:
        dict: Dictionary of metrics.
    """
    metrics = {
        "Accuracy": round(accuracy_score(y_true, y_pred), 4),
        "Precision": round(precision_score(y_true, y_pred), 4),
        "Recall": round(recall_score(y_true, y_pred), 4),
        "F1-Score": round(f1_score(y_true, y_pred), 4)
    }

    # Add ROC-AUC if probabilities provided
    if y_proba is not None:
        try:
            metrics["ROC-AUC"] = round(roc_auc_score(y_true, y_proba), 4)
        except ValueError:
            metrics["ROC-AUC"] = None

    print("\n📊 Model Evaluation Metrics")
    for k, v in metrics.items():
        print(f"{k:10s}: {v}")

    print("\nDetailed Classification Report:\n")
    print(classification_report(y_true, y_pred, target_names=["Legitimate", "Phishing"]))
    
    return metrics
