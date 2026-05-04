from flask import request, jsonify
from server.api.prediction.services import PredictionService

class PredictionController:
    @staticmethod
    def predict():
        """Handle prediction request."""
        data = request.get_json()
        
        if not data:
            return jsonify({'status': 'error', 'message': 'No input data provided'}), 400
            
        try:
            predicted_value = PredictionService.predict_yield(data)
            
            return jsonify({
                'status': 'success',
                'data': {
                    'prediction': round(predicted_value, 2),
                    'unit': 'hg/ha'
                }
            }), 200

        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500

    @staticmethod
    def health():
        """Handle health check."""
        return jsonify({
            'status': 'success',
            'message': 'Prediction module is operational'
        }), 200
