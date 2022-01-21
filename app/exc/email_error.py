class EmailError(Exception):
    def __init__(self):
        self.message = {"error": "E-mail already registered."
                         }, 409
        super().__init__(self.message)