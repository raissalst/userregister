class EmailError(Exception):
    def __init__(self):
        self.message = {"error": "User already exists."
                         }, 409
        super().__init__(self.message)