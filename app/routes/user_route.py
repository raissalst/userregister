# from app.controllers import dev_controller
from http import HTTPStatus
from flask import request, jsonify
from app.exc.email_error import EmailError
from app.exc.not_found_error import NotFoundError
from app.models.user_model import User
# from app.exc.wrong_keys_error import WrongKeysError
# from app.exc.attribute_error import AttributeError
# from app.modules import user_handler

from app.controllers import user_controller

def user_route(app):
    @app.get("/user")
    def get_users_list():
        return jsonify(user_controller.load_json_file_data())
        # return ""

    # @app.get("/user/<int:id>")
    # def filter_user(id):
    #     try:
    #         return user_controller.filter_user_by_id(id)
    #     except NotFoundError as e:
    #         return e.message
    
    @app.post("/user")
    def post_users():
        new_user_data = request.get_json()
        try:
            new_user = User(**new_user_data)
            return user_controller.post_new_user(new_user.__dict__), HTTPStatus.CREATED
        except TypeError as e:
            return {"msg": f"{e}"}, HTTPStatus.BAD_REQUEST
        except AttributeError as e:
            return {"msg": f"{e}"}, HTTPStatus.BAD_REQUEST
        except EmailError as err:
            return err.message


    @app.delete("/user/<int:id>")
    def delete_users(id):
        try:
            return user_controller.delete_user_by_id(id)
        except NotFoundError as e:
            return e.message

    @app.patch("/user/<int:id>")
    def update_user(id):
        new_user_data = request.get_json()
        try:
            return user_controller.update_user_by_id(new_user_data, id)
        except NotFoundError as e:
            return e.message
        except TypeError as e:
            return {"msg": f"{e}"}, HTTPStatus.BAD_REQUEST
        except AttributeError as e:
            return {"msg": f"{e}"}, HTTPStatus.BAD_REQUEST
        except EmailError as err:
            return err.message