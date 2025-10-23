import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(train_data: pd.DataFrame, labels: pd.Series, save_path='model.pkl'):
    """Train and save phishing detection model."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(train_data, labels)
    joblib.dump(model, save_path)
    print(f"✅ Model trained and saved at {save_path}")
