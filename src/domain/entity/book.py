class Book():
    name: str
    isAvailable: bool

    def __init__(self, name, isAvailable : bool = True):
        self.name = name
        self.isAvailable = isAvailable
