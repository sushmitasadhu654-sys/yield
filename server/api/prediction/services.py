import joblib
import pandas as pd
import numpy as np
import os
from flask import current_app

class PredictionService:
    _model = None
    _scaler = None

    @classmethod
    def load_model(cls):
        """Loads model and scaler if not already loaded."""
        if cls._model is None:
            try:
                model_path = current_app.config.get('MODEL_PATH', 'yield_model.pkl')
                scaler_path = current_app.config.get('SCALER_PATH', 'scaler.pkl')
                
                if os.path.exists(model_path):
                    cls._model = joblib.load(model_path)
                if os.path.exists(scaler_path):
                    cls._scaler = joblib.load(scaler_path)
                    
                print(f"Model and Scaler loaded successfully.")
            except Exception as e:
                print(f"Error loading model: {e}")
                raise e

    @classmethod
    def predict_yield(cls, data):
        """Processes input data and returns prediction."""
        cls.load_model()
        
        if cls._model is None:
            raise Exception("Model file (yield_model.pkl) not found. Please train the model first.")

        # Extract data with defaults
        year = int(data.get('Year', 2024))
        rain = float(data.get('average_rain_fall_mm_per_year', 0))
        pesticides = float(data.get('pesticides_tonnes', 0))
        temp = float(data.get('avg_temp', 0))
        crop = data.get('Item', '').lower()

        # One-Hot Encoding setup
        crop_dict = {
            'Item_Maize': 0,
            'Item_Plantains and others': 0,
            'Item_Potatoes': 0,
            'Item_Rice, paddy': 0,
            'Item_Sorghum': 0,
            'Item_Soybeans': 0,
            'Item_Sweet potatoes': 0,
            'Item_Wheat': 0,
            'Item_Yams': 0
        }

        crop_map = {
            "maize": 'Item_Maize',
            "potatoes": 'Item_Potatoes',
            "rice": 'Item_Rice, paddy',
            "wheat": 'Item_Wheat',
            "sorghum": 'Item_Sorghum',
            "soybeans": 'Item_Soybeans',
            "sweet potatoes": 'Item_Sweet potatoes',
            "yams": 'Item_Yams',
            "plantains": 'Item_Plantains and others'
        }

        if crop in crop_map:
            crop_dict[crop_map[crop]] = 1

        input_data = [[year, rain, pesticides, temp, *crop_dict.values()]]
        
        columns = [
            'Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp',
            'Item_Maize', 'Item_Plantains and others', 'Item_Potatoes', 'Item_Rice, paddy',
            'Item_Sorghum', 'Item_Soybeans', 'Item_Sweet potatoes', 'Item_Wheat', 'Item_Yams'
        ]

        input_df = pd.DataFrame(input_data, columns=columns)
        
        prediction = cls._model.predict(input_df)
        return float(prediction[0])
