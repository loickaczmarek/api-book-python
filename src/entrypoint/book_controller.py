from src.domain.usecase.get_book_by_name_usecase import GetBookByNameUseCase
from src.domain.usecase.get_all_books_usecase import GetAllBooksUseCase

class BookController:

    def __init__(self,
                 getBookByNameUseCase : GetBookByNameUseCase,
                 getAllBooksUseCase : GetAllBooksUseCase):
        self.getBookByNameUseCase = getBookByNameUseCase
        self.getAllBooksUseCase = getAllBooksUseCase

    def getBook(self, name : str):
        return self.getBookByNameUseCase.getBook(name)

    def getBooks(self):
        return self.getAllBooksUseCase.getAllBooks()