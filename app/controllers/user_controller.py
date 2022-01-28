from flask import jsonify
import os
from json import dump, load
# from app.exc.attribute_error import AttributeError
from app.exc.email_error import EmailError
from app.exc.not_found_error import NotFoundError

filename_database = os.environ.get("FILE_BASE")
directory_path = os.environ.get("DIRECTORY_PATH")

datainitial = {"data": []}

def increment_id():
    dados = load_json_file_data()
    user_list = dados.get("data")
    return user_list[-1]["id"] + 1 if len(user_list) != 0 else 1

def load_json_file_data():
    try:
        with open(f"{directory_path}{filename_database}", "r") as json_file:
            dados = load(json_file)
    except:
        with open(f"{directory_path}{filename_database}", "w") as json_file:
            dump(datainitial, json_file, indent=4)
        with open(f"{directory_path}{filename_database}", "r") as json_file:
            dados = load(json_file)
    return dados

def post_new_user(new_user_data):
    dados = load_json_file_data()
    user_list = dados.get("data")

    if next((item for item in user_list if item["email"] == new_user_data["email"]), None) != None:
        raise EmailError
    
    user_list.append(new_user_data)

    with open(f"{directory_path}{filename_database}", "w") as json_file:
        dump(dados, json_file, indent=4)
    return jsonify(new_user_data)

def filter_user_by_id(id):
    dados = load_json_file_data()
    user_list = dados.get("data")

    if len(user_list) == 0:
        raise NotFoundError
    
    data_filtered = None

    for item in user_list:
        if item["id"] == id:
            data_filtered = item
            return jsonify(data_filtered), 200
    
    if not data_filtered:
        raise NotFoundError

def delete_user_by_id(id):
    dados = load_json_file_data()
    user_list = dados.get("data")

    if len(user_list) == 0:
        raise NotFoundError

    data_to_be_deleted = None

    for index, item in enumerate(user_list):
        if item["id"] == id:
            data_to_be_deleted = item
            user_list.pop(index)
            with open(f"{directory_path}{filename_database}", "w") as json_file:
                dump(dados, json_file, indent=4)
            return jsonify(data_to_be_deleted), 200
    
    if not data_to_be_deleted:
        raise NotFoundError
    

def update_user_by_id(new_data, id):
    dados = load_json_file_data()
    list_of_users = dados_json["data"]

    if new_data.get("email"):
        new_email = new_data.get("email").lower()
        if next((item for item in list_of_users if item["email"] == new_email), None) != None:
            raise EmailError

    if len(list_of_users) == 0:
        raise NotFoundError
    
    array_of_valid_keys = ["name", "email"]
    array_of_entry_to_update_keys = new_data.keys()
    array_of_wrong_keys = []

    for key in array_of_entry_to_update_keys:
        if key not in array_of_valid_keys:
            array_of_wrong_keys.append(key)

    if len(array_of_wrong_keys) != 0:
        raise WrongKeysError(array_of_wrong_keys)

    for item in list_of_users:
        if item["id"] == id:
            if new_data.get("name") and type(new_data.get("name")) is str:
                item["name"] = new_data["name"].title()
            if new_data.get("email") and type(new_data.get("email")) is str:
                item["email"] = new_data["email"].lower()
            if new_data.get("name") and type(new_data.get("name")) is not str:
                raise AttributeError
            if new_data.get("email") and type(new_data.get("email")) is not str:
                raise AttributeError

            data_updated = item

            with open(f"{directory_path}{filename_database}", "w") as json_file:
                dump(dados_json, json_file, indent=4)
            
            return jsonify(data_updated), 200
        else:
            raise NotFoundError

