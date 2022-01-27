from flask import Flask
from app import view
import os

directory_path = os.environ.get("DIRECTORY_PATH")
directory_name = os.environ.get("DIRECTORY_NAME")

if f"{directory_name}" not in os.listdir("./app"):
    os.mkdir(f"{directory_path}")

def create_app():
    app = Flask(__name__)

    view.init_app(app)

    return app