# Gives a page for my personal profile in Spanish

from flask import Blueprint

spanish = Blueprint('spanish', __name__)

@spanish.route('/my-cv/jorgeruiz/spanish')
def dashboard():
	return 'Spanish Dashboard'