# Allows the directory to become a library from
# which we can import packages

from flask import Flask

# Creates a Flask app
def create_app():
	app = Flask(__name__)

	# Integrate blueprints for different routes
	from app.blueprints.select_lang import lang
	app.register_blueprint(lang)

	from app.blueprints.english import english
	app.register_blueprint(english)

	from app.blueprints.spanish import spanish
	app.register_blueprint(spanish)

	return app