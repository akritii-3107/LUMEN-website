# LUMEN-website.wsgi

import sys
import logging
logging.basicConfig(stream=sys.stderr)

# Add your project directory to the sys.path
sys.path.insert(0, "/LUMEN-website/")

# Import the Flask app from the main application file
from app import app as application
application.secret_key = 'lumen2022-23'
