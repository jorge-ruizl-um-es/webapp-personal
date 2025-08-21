# Vista de la aplicación para un usuario sin registrar, 
# página principal

from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/my-cv/jorge')
def index():
	# return render_template('index.html')
	return "Hola Jorge!"