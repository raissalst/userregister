from flask import jsonify
import os
from json import dump, load
from app.exc.attribute_error import AttributeError
from app.exc.email_error import EmailError

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
        new_user_data["id"] = len(user_list) + 1

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