# Gives a page for my personal profile in English

from flask import Blueprint, render_template

english = Blueprint('english', __name__)

@english.route('/my-cv/jorgeruiz/english')
def main_eng():
	return render_template('index_eng.html')