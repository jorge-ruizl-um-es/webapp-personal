# Allows the directory to become a library from
# which we can import packages

from flask import Flask

# Creates a Flask app
def create_app():
	app = Flask(__name__)

	return app