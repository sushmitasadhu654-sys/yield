import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'yield_prediction_secret_key')
    MODEL_PATH = os.path.join(os.getcwd(), 'models', 'yield_model.pkl')
    SCALER_PATH = os.path.join(os.getcwd(), 'models', 'scaler.pkl')
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
