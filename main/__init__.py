from flask import Flask
from .ui import ui_blueprint


def create_flask_app():
    app = Flask(__name__)
    app.register_blueprint(ui_blueprint, url_prefix = "/")    
    return app

