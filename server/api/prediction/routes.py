from flask import Blueprint
from server.api.prediction.controllers import PredictionController

prediction_bp = Blueprint('prediction', __name__)

# Define routes and map them to controller methods
prediction_bp.route('/predict', methods=['POST'])(PredictionController.predict)
prediction_bp.route('/health', methods=['GET'])(PredictionController.health)
