
from flask import Blueprint
from flask import render_template


calc = Blueprint('calc', __name__, template_folder='templates')

@calc.route('/')
def index():
    return render_template('calculate/index.html')

