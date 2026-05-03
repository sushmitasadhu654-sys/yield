from flask import Blueprint, request, jsonify
from server.services.yield_service import YieldService

prediction_bp = Blueprint('prediction', __name__)

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    """Endpoint for crop yield prediction."""
    data = request.get_json()
    
    if not data:
        return jsonify({'status': 'error', 'message': 'No data provided'}), 400
        
    try:
        predicted_yield = YieldService.predict(data)
        
        return jsonify({
            'status': 'success',
            'data': {
                'predicted_yield': predicted_yield,
                'unit': 'hg/ha'
            }
        }), 200

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@prediction_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'success',
        'message': 'Server is healthy and running'
    }), 200
