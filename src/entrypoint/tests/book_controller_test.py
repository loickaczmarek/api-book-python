from src.entrypoint.book_controller import BookController
from src.domain.usecase.get_book_by_name_usecase import GetBookByNameUseCase
from src.domain.usecase.get_all_books_usecase import GetAllBooksUseCase
from src.domain.usecase.rent_book_usecase import RentBookUseCase
from src.domain.usecase.return_book_usecase import ReturnBookUseCase
from src.domain.repository.book_repository import BookRepository
from src.domain.entity.book import Book

class MockBookRepository(BookRepository):
    books = [Book("harry potter"), Book("seigneur des anneaux")]

    def getBook(self, name):
        for book in self.books:
            if name == book.name:
                return book
        return None

    def getBooks(self):
        return self.books

    def updateBook(self, book : Book):
        for currentBook in self.books:
            if book.name == currentBook.name:
                currentBook.name = book.name
                currentBook.isAvailable = book.isAvailable

controller = BookController(GetBookByNameUseCase(MockBookRepository),
                            GetAllBooksUseCase(MockBookRepository),
                            RentBookUseCase(MockBookRepository),
                            ReturnBookUseCase(MockBookRepository))

def test_get_one_existing_book():
    book = controller.getBook("harry potter")
    assert book.name == "harry potter"

def test_get_not_existing_book():
    book = controller.getBook("pokemon")
    assert book is None

def test_get_all_books():
    books = controller.getBooks()
    assert books[0].name == "harry potter"
    assert books[1].name == "seigneur des anneaux"

def test_rent_existing_book():
    controller.updateBook(Book("harry potter", False))
    book = controller.getBook("harry potter")
    assert book.isAvailable == False

def test_rent_not_existing_book():
    controller.updateBook(Book("pokemon", False))
    book = controller.getBook("pokemon")
    assert book is None

def test_return_existing_book():
    controller.updateBook(Book("harry potter", True))
    book = controller.getBook("harry potter")
    assert book.isAvailable == True