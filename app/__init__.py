from flask import Flask
from app import routes
import os

directory_path = os.getenv("DIRECTORY_PATH")
directory_name = os.getenv("DIRECTORY_NAME")

if f"{directory_name}" not in os.listdir("./app"):
    os.mkdir(f"{directory_path}")

def create_app():
    app = Flask(__name__)

    routes.init_app(app)

    return app