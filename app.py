from flask import Flask, request, jsonify
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler globally
try:
    model = joblib.load("yield_model.pkl")
    scaler = joblib.load("scaler.pkl")
    print("Model and Scaler loaded.")
except:
    print("Warning: Model files not found. Deployment will fail on prediction.")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    try:
        year = data['Year']
        rain = data['average_rain_fall_mm_per_year']
        pesticides = data['pesticides_tonnes']
        temp = data['avg_temp']
        crop = data['Item'].lower()

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
        prediction = model.predict(input_df)

        return jsonify({
            'status': 'success',
            'predicted_yield': float(prediction[0]),
            'unit': 'hg/ha'
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'status': 'online', 'project': 'Crop Yield Prediction API'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
