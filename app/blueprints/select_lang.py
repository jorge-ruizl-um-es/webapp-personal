# Main view of the page

from flask import Blueprint, render_template

lang = Blueprint('lang', __name__)

@lang.route('/')
def select_lang():
	return render_template('select_lang.html')