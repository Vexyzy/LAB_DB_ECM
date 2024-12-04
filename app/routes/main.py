from flask import Blueprint, render_template

MAIN = Blueprint('main', __name__)

@MAIN.route('/index')
@MAIN.route('/')
def index():
    return render_template('main/index.html')