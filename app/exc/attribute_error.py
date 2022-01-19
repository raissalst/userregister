class AttributeError(Exception):
    def __init__(self, type_name: str, type_email: str):
        self.message = {"wrong fields": [
                             {"nome": type_name},
                             {"email": type_email}
                         ]}, 400

        super().__init__(self.message)