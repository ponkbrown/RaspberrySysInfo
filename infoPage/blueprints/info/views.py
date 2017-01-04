from flask import Blueprint, render_template

info = Blueprint('info', __name__, template_folder='templates')


@info.route('/')
def inicio():
    return render_template('info.html')
