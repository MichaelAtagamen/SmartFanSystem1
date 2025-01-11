import os
import sys

# Add your project directory to the system path
sys.path.insert(0, '/var/www/FlaskApp')

# Import your Flask application
from FlaskApp import app as application

# Ensure the application runs in the correct environment (if applicable)
os.environ['FLASK_ENV'] = 'production'


