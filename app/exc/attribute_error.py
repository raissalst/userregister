class AttributeError(Exception):
    def __init__(self):
        self.message = {"Error in types of values": "Values must be type string."}, 400

        super().__init__(self.message)