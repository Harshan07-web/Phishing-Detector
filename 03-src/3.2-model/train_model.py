from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib


def train_model(x,y):
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(x_train,y_train)
    joblib.dump(model,r"D:\phishing Detector\04-saved-models\rf_model.pkl")
    return model , x_test , y_test