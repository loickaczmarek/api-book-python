from src.entrypoint.book_controller import BookController
from src.domain.usecase.get_book_by_name_usecase import GetBookByNameUseCase
from src.domain.usecase.get_all_books_usecase import GetAllBooksUseCase
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

controller = BookController(GetBookByNameUseCase(MockBookRepository)
                            , GetAllBooksUseCase(MockBookRepository))

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
    controller.updateBook("harry potter")
    book = controller.getBook("harry potter")
    assert book.isAvailable == False