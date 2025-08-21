# Allows the directory to become a library from
# which we can import packages

from flask import Flask

# Creates a Flask app
def create_app():
	app = Flask(__name__)

	from app.blueprints.main import main
	app.register_blueprint(main)

	from app.blueprints.spanish import spanish
	app.register_blueprint(spanish)

	return app