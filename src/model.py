from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib
import os

class YieldModel:
    def __init__(self, n_estimators=100, random_state=42):
        self.model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)
        self.scaler = StandardScaler()

    def train(self, X_train, y_train):
        # The notebook used scaled data for some models, 
        # but for RF it usually works fine without. 
        # However, to be consistent with the professional structure, 
        # we'll save a scaler for future-proofing or if we switch back to Linear/KNN.
        self.scaler.fit(X_train)
        self.model.fit(X_train, y_train)

    def save(self, model_path, scaler_path):
        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)
        print(f"Model saved to {model_path}")
        print(f"Scaler saved to {scaler_path}")

    def load(self, model_path, scaler_path):
        if os.path.exists(model_path) and os.path.exists(scaler_path):
            self.model = joblib.load(model_path)
            self.scaler = joblib.load(scaler_path)
            return True
        return False
