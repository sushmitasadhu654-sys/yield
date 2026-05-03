import os
from server import create_app

# Get configuration name from environment variable, default to 'prod'
config_name = os.getenv('FLASK_CONFIG', 'prod')
app = create_app(config_name)

if __name__ == '__main__':
    # For local development
    app.run(host='0.0.0.0', port=5000)
