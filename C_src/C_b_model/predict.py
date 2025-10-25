import joblib
import pandas as pd
from ..C_a_preprocessing.feature_extraction import extract_url_features

# --- Load the model once globally for performance ---
MODEL_PATH = r"D:\phishing Detector\D_saved_models\rf_model.pkl"
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"[ERROR] Could not load model: {e}")

def predict_url(url: str):
    """
    Predict whether the given URL is phishing or legitimate.
    
    Returns:
        tuple: (result_label: str, result_code: int, features: dict)
    """
    if model is None:
        raise RuntimeError("Model not loaded. Check model path and permissions.")

    # --- Step 1: Extract features ---
    features = extract_url_features(url)
    df = pd.DataFrame([features])

    # --- Step 2: Make prediction ---
    prediction = model.predict(df)[0]

    # --- Step 3: Return formatted results ---
    result_label = "Phishing" if prediction == 1 else "Legitimate"
    result_code = int(prediction)

    return result_label, result_code, features
