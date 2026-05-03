from flask import Flask, jsonify
from server.config import config_by_name

def create_app(config_name='prod'):
    """Flask application factory."""
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Register Blueprints
    from server.routes import prediction_bp
    app.register_blueprint(prediction_bp, url_prefix='/api/v1')

    @app.route('/')
    def index():
        return jsonify({
            'message': 'Welcome to Crop Yield Prediction API',
            'endpoints': {
                'predict': '/api/v1/predict (POST)',
                'health': '/api/v1/health (GET)'
            }
        })

    return app
