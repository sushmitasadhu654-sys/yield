import pandas as pd
import os
import sys

# Add root directory to path to import src
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.model import YieldModel

def predict_yield():
    # Load model wrapper
    model_wrapper = YieldModel()
    if not model_wrapper.load(os.path.join("models", "yield_model.pkl"), 
                              os.path.join("models", "scaler.pkl")):
        print("Error: Model files not found. Please run 'python scripts/train_pipeline.py' first.")
        return

    print("--- Crop Yield Prediction ---")
    try:
        year = int(input("Enter Year: "))
        rain = float(input("Enter Average Rainfall (mm/year): "))
        pesticides = float(input("Enter Pesticides (tonnes): "))
        temp = float(input("Enter Average Temperature: "))
        crop = input("Enter Crop (Maize, Potatoes, Rice, Wheat, Sorghum, Soybeans, Sweet potatoes, Yams, Plantains): ").lower()
    except ValueError:
        print("Invalid input. Please enter numeric values where expected.")
        return

    # One-Hot Encoding setup (Consistent with preprocessing.py)
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

    feature_cols = [
        'Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp',
        'Item_Maize', 'Item_Plantains and others', 'Item_Potatoes', 'Item_Rice, paddy',
        'Item_Sorghum', 'Item_Soybeans', 'Item_Sweet potatoes', 'Item_Wheat', 'Item_Yams'
    ]

    # Create input row
    input_row = {col: 0 for col in feature_cols}
    input_row['Year'] = year
    input_row['average_rain_fall_mm_per_year'] = rain
    input_row['pesticides_tonnes'] = pesticides
    input_row['avg_temp'] = temp
    
    if crop in crop_map:
        input_row[crop_map[crop]] = 1
    else:
        print(f"Warning: '{crop}' not recognized. Using default features.")

    input_df = pd.DataFrame([input_row])

    # Predict
    prediction = model_wrapper.model.predict(input_df)

    print("\n" + "="*30)
    print(f"🌾 Predicted Crop Yield: {prediction[0]:.2f} hg/ha")
    print("="*30)

if __name__ == "__main__":
    predict_yield()
