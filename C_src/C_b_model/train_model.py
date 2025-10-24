# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv(r'D:\phishing Detector\A_data\url_features_extracted1.csv')

df = df.dropna(subset=['ClassLabel'])
df['ClassLabel'] = df['ClassLabel'].astype(int)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

X = df.drop(['URL','ClassLabel'], axis=1)
y = df['ClassLabel']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("Training Accuracy:", model.score(X_train, y_train))
print("Testing Accuracy:", model.score(X_test, y_test))
with open(r'D:\phishing Detector\D_saved_models\phishing_rf.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model saved successfully as 'phishing_model.pkl'")
