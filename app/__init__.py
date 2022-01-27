from flask import Flask
from app import view


def create_app():
    app = Flask(__name__)

    view.init_app(app)

    return app