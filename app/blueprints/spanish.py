# Gives a page for my personal profile in Spanish

from flask import Blueprint, render_template
from app.data import data_esp

spanish = Blueprint('spanish', __name__)

@spanish.route('/my-cv/jorgeruiz/spanish')
def main_spa():
	return render_template('index_esp.html', user_data = data_esp)