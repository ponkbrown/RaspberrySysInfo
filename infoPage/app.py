from flask import Flask

from infoPage.blueprints.info import info

def create_app():
    '''
    Crea la aplicacción de flask usando el patron fabrica
    '''

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(info)

    return app
