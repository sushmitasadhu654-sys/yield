from flask import Flask, render_template
from server.config import config_by_name

def create_app(config_name='prod'):
    """Flask application factory."""
    app = Flask(__name__, 
                static_folder='static',
                template_folder='templates')
    
    app.config.from_object(config_by_name[config_name])

    # Register Blueprints
    from server.api.prediction.routes import prediction_bp
    app.register_blueprint(prediction_bp, url_prefix='/api/v1')

    @app.route('/')
    def index():
        """Serve the frontend application."""
        return render_template('index.html')

    return app
