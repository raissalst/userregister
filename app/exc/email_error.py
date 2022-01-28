from email.policy import HTTP
from http import HTTPStatus

class EmailError(Exception):
    def __init__(self):
        self.message = {"error": "E-mail already registered."
                         }, HTTPStatus.CONFLICT
        super().__init__(self.message)