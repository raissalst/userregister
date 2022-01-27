# from app.controllers import dev_controller
from flask import Flask, request
from app.exc.email_error import EmailError
from app.exc.not_found_error import NotFoundError
from app.exc.wrong_keys_error import WrongKeysError
from app.exc.attribute_error import AttributeError
from app.modules import user_handler
from models.user_model import User
from app.controllers import user_controller

def user_route(app):
    @app.get("/user")
    def get_users_list():
        return user_handler.list_users()

    @app.get("/user/<int:id>")
    def filter_user(id):
        try:
            return user_handler.filter_user_by_id(id)
        except NotFoundError as e:
            return e.message
    
    @app.post("/user")
    def post_users():
        new_user_data = request.get_json()

        try:
            new_user = User(**new_user_data)
            return user_controller.post_new_user(new_user.__dict__)
        except TypeError as e:
            return {"msg": f"{e}"}, 404
        except AttributeError as err:
            return err.message


    @app.delete("/user/<int:id>")
    def delete_users(id):
        try:
            return user_handler.delete_user_by_id(id)
        except NotFoundError as e:
            return e.message

    @app.patch("/user/<int:id>")
    def update_user(id):
        new_user_data = request.get_json()
        try:
            return user_handler.update_user_by_id(new_user_data, id)
        except NotFoundError as e:
            return e.message
        except WrongKeysError as e:
            return e.message
        except AttributeError as err:
            return err.message
        except EmailError as err:
            return err.message
        except TypeError as e:
            return {"msg": f"{e}"}, 404