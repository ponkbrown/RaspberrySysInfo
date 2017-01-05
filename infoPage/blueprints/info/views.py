from flask import Blueprint, render_template
from infoPage.scripts_info import get_info

info = Blueprint('info', __name__, template_folder='templates')


@info.route('/')
def inicio():
    system_info = get_info()
    return render_template('info.html', system_info = system_info)
