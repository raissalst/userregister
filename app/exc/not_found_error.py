from http import HTTPStatus

class NotFoundError(Exception):
    def __init__(self):
        self.message = {"error": "User not found."
                         }, HTTPStatus.NOT_FOUND
        super().__init__(self.message)