import joblib
import pandas as pd
from ..C_a_preprocessing.feature_extraction import extract_url_features
# --- DELETE THIS LINE ---
# from ..C_a_preprocessing.txt_cleaner import clean_url 

def predict_url(url: str, model_path=r'D:\\phishing Detector\\D_saved_models\\rf_model.pkl'):
    """Predict if a URL is phishing or legitimate."""
    model = joblib.load(model_path)
    
    # --- DELETE THIS LINE ---
    # cleaned = clean_url(url)
    
    # --- USE THE RAW URL INSTEAD ---
    features = extract_url_features(url) 
    
    df = pd.DataFrame([features])


    # features_df is a DataFrame with one row for the URL about to be predicted
    print("FEATURE VECTOR (for debugging):")
    for k, v in df.iloc[0].items():
        print(f"{k}: {v}")


    prediction = model.predict(df)[0]
    return "Phishing" if prediction == 1 else "Legitimate"