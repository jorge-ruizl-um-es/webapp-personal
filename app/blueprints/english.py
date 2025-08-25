# Gives a page for my personal profile in English

from flask import Blueprint, render_template
from app.data import data_eng

english = Blueprint('english', __name__)

@english.route('/my-cv/jorgeruiz/english')
def main_eng():
	return render_template('index_eng.html', user_data=data_eng)