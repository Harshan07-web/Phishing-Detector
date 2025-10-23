import joblib
import pandas as pd
from ..C_a_preprocessing.feature_extraction import extract_features
from ..C_a_preprocessing.txt_cleaner import clean_url

def predict_url(url: str, model_path=r'E:\ML project\Phishing-Detector\D_saved_models\rf_model.pkl'):
    """Predict if a URL is phishing or legitimate."""
    model = joblib.load(model_path)
    cleaned = clean_url(url)
    features = extract_features(cleaned)
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    return "Phishing" if prediction == 1 else "Legitimate"
