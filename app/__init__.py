from flask import Flask, request
from app.exc.email_error import EmailError
from app.exc.not_found_error import NotFoundError
from app.exc.wrong_keys_error import WrongKeysError
from app.exc.attribute_error import AttributeError
from app.modules.user_handler import list_users, access_json_file, delete_user_by_id, update_user_by_id, filter_user_by_id
import os

app = Flask(__name__)

directory_path = os.environ.get("DIRECTORY_PATH")
directory_name = os.environ.get("DIRECTORY_NAME")

if f"{directory_name}" not in os.listdir("./app"):
    os.mkdir(f"{directory_path}")

@app.get("/user")
def get_users_list():
    return list_users()

@app.get("/user/<int:id>")
def filter_user(id):
    try:
        return filter_user_by_id(id)
    except NotFoundError as e:
        return e.message
    
@app.post("/user")
def post_users():
    new_user_data = request.get_json()
    return access_json_file(new_user_data)

@app.delete("/user/<int:id>")
def delete_users(id):
    try:
        return delete_user_by_id(id)
    except NotFoundError as e:
        return e.message

@app.patch("/user/<int:id>")
def update_user(id):
    new_user_data = request.get_json()
    try:
        return update_user_by_id(new_user_data, id)
    except NotFoundError as e:
        return e.message
    except WrongKeysError as e:
        return e.message
    except AttributeError as err:
        return err.message
    except EmailError as err:
        return err.message