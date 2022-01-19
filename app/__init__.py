from flask import Flask, request
from app.modules.user_handler import list_users, access_json_file
import os

app = Flask(__name__)

directory_path = os.environ.get("DIRECTORY_PATH")
directory_name = os.environ.get("DIRECTORY_NAME")

if f"{directory_name}" not in os.listdir("./app"):
    os.mkdir(f"{directory_path}")

@app.get("/user")
def get_users_list():
    return list_users()
    
@app.post("/user")
def post_users():
    new_user_data = request.get_json()
    return access_json_file(new_user_data)