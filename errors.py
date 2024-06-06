class InputError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UserError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)