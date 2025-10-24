import joblib
import pandas as pd
from ..C_a_preprocessing.feature_extraction import extract_url_features

def predict_url(url: str, model_path=r'D:\phishing Detector\D_saved_models\rf_model.pkl'):
    model = joblib.load(model_path)
    features = extract_url_features(url) 
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    return "Phishing" if prediction == 1 else "Legitimate"
