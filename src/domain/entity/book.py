class Book:
    name: str
    isAvailable: bool

    def __init__(self, name):
        self.name = name
        self.isAvailable = True

    def rentBook(self):
        self.isAvailable = False

    def returnBook(self):
        self.isAvailable = True
