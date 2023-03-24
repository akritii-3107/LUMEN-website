# LUMEN-website.wsgi

import sys
import os

# add the project directory to the sys.path
project_home = u'/'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import the Flask app object
from app import app as application

# set the environment variables for Flask
os.environ['FLASK_ENV'] = 'production'
os.environ['FLASK_APP'] = 'app.py'

# define the application callable for WSGI
def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    
    return [b"Hello World from Flask!"]

# run the application
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, application)

