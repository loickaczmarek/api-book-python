from src.domain.usecase.get_book_by_name_usecase import GetBookByNameUseCase
from src.domain.usecase.get_all_books_usecase import GetAllBooksUseCase
from src.domain.entity.book import Book
from src.domain.usecase.rent_book_usecase import RentBookUseCase
from src.domain.usecase.return_book_usecase import ReturnBookUseCase


class BookController:

    def __init__(self,
                 getBookByNameUseCase : GetBookByNameUseCase ,
                 getAllBooksUseCase : GetAllBooksUseCase ,
                 rentBookUseCase : RentBookUseCase ,
                 returnBookUseCase : ReturnBookUseCase):
        self.getBookByNameUseCase = getBookByNameUseCase
        self.getAllBooksUseCase = getAllBooksUseCase
        self.rentBookUseCase = rentBookUseCase
        self.returnBookUseCase = returnBookUseCase

    def getBook(self, name: str):
        return self.getBookByNameUseCase.getBook(name)

    def getBooks(self):
        return self.getAllBooksUseCase.getAllBooks()

    def updateBook(self, book: Book):
        foundBook = self.getBookByNameUseCase.getBook(book.name)
        if foundBook is not None:
            if book.isAvailable == False:
                self.rentBookUseCase.rentBook(foundBook)
            else:
                self.returnBookUseCase.returnBook(foundBook)
