# Gives a page for my personal profile in Spanish

from flask import Blueprint, render_template

spanish = Blueprint('spanish', __name__)

@spanish.route('/my-cv/jorgeruiz/spanish')
def dashboard():
	return render_template('index_esp.html')