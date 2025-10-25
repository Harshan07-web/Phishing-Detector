import joblib
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def evaluate_model(model_path, test_data_path):
    """
    Evaluate the trained model using test dataset and return metrics.
    """
    # Load model and test data
    model = joblib.load(model_path)
    data = pd.read_csv(test_data_path)

    X = data.drop(['id',"CLASS_LABEL"], axis=1)
    y_true = data["CLASS_LABEL"]

    # Predict
    y_pred = model.predict(X)

    # Metrics
    accuracy = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred, output_dict=True)
    cm = confusion_matrix(y_true, y_pred).tolist()  # list for JSON compatibility

    return {
        "accuracy": round(accuracy * 100, 2),
        "precision": round(report["weighted avg"]["precision"], 3),
        "recall": round(report["weighted avg"]["recall"], 3),
        "f1_score": round(report["weighted avg"]["f1-score"], 3),
        "confusion_matrix": cm,
    }
