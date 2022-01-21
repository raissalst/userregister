from http import HTTPStatus

class WrongKeysError(Exception):

    def __init__(self, array_of_keys: list):
        self.message = {"wrong keys": f"{', '.join(array_of_keys)}"}, HTTPStatus.BAD_REQUEST

        super().__init__(self.message)
