# Main view of the page

from flask import Blueprint, render_template
from app.data import data_esp

lang = Blueprint('lang', __name__)

@lang.route('/')
def select_lang():
	return render_template('select_lang.html', user_data = data_esp)