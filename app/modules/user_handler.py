from flask import jsonify
import os
from json import dump, load
from app.exc.attribute_error import AttributeError
from app.exc.email_error import EmailError
from app.exc.not_found_error import NotFoundError
from app.exc.wrong_keys_error import WrongKeysError

filename_database = os.environ.get("FILE_BASE")
directory_path = os.environ.get("DIRECTORY_PATH")

datainitial = {"data": []}

def access_json_file(new_user_data):
    try:
        with open(f"{directory_path}{filename_database}", "r") as json_file:
            dados = load(json_file)
    except:
        with open(f"{directory_path}{filename_database}", "w") as json_file:
            dump(datainitial, json_file, indent=4)
        with open(f"{directory_path}{filename_database}", "r") as json_file:
            dados = load(json_file)
    
    return post_new_user(new_user_data, dados)

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

def list_users():
    try:
        with open(f"{directory_path}{filename_database}", "r") as json_file:
            dados = load(json_file)
            return jsonify(dados)
    except:
        with open(f"{directory_path}{filename_database}", "w") as json_file:
            dump(datainitial, json_file, indent=4)
        with open(f"{directory_path}{filename_database}", "r") as json_file:
            dados = load(json_file)
            return jsonify(dados)


def post_new_user(new_user_data, dados):
    user_list = dados.get("data")

    try:
        if type(new_user_data.get("nome")) is not str or type(new_user_data.get("email")) is not str:
            type_name = type(new_user_data.get("nome")).__name__
            type_email = type(new_user_data.get("email")).__name__
            raise AttributeError(type_name, type_email)

        new_name = new_user_data.get("nome").title()
        new_email = new_user_data.get("email").lower()
        new_user_data["nome"] = new_name
        new_user_data["email"] = new_email
        new_user_data["id"] = user_list[-1]["id"] + 1 if len(user_list) != 0 else 1

        if next((item for item in user_list if item["email"] == new_email), None) != None:
            raise EmailError()
        
        user_list.append(new_user_data)
        with open(f"{directory_path}{filename_database}", "w") as json_file:
            dump(dados, json_file, indent=4)
        return jsonify(new_user_data), 201
    
    except AttributeError as err:
        return err.message
    
    except EmailError as err:
        return err.message


def delete_user_by_id(id):
    dados_json = load_json_file_data()
    list_of_users = dados_json["data"]

    if len(list_of_users) == 0:
        raise NotFoundError

    for index, item in enumerate(list_of_users):
        if item["id"] == id:
            data_to_be_deleted = item
            list_of_users.pop(index)
            with open(f"{directory_path}{filename_database}", "w") as json_file:
                dump(dados_json, json_file, indent=4)
        else:
            raise NotFoundError
    return jsonify(data_to_be_deleted), 200

def update_user_by_id(new_data, id):
    dados_json = load_json_file_data()
    list_of_users = dados_json["data"]

    if len(list_of_users) == 0:
        raise NotFoundError
    
    array_of_valid_keys = ["nome", "email"]
    array_of_entry_to_update_keys = new_data.keys()
    array_of_wrong_keys = []

    for key in array_of_entry_to_update_keys:
        if key not in array_of_valid_keys:
            array_of_wrong_keys.append(key)

    if len(array_of_wrong_keys) != 0:
        raise WrongKeysError(array_of_wrong_keys)

    for item in list_of_users:
        if item["id"] == id:
            if new_data.get("nome"):
                item["nome"] = new_data["nome"]
            if new_data.get("email"):
                item["email"] = new_data["email"]
            data_updated = item

            with open(f"{directory_path}{filename_database}", "w") as json_file:
                dump(dados_json, json_file, indent=4)
            
            return jsonify(data_updated), 200
        else:
            raise NotFoundError

