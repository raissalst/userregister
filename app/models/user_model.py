from controllers.user_controller import increment_id

class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name.title()
        self.email = email.lower()
        self.id = increment_id()