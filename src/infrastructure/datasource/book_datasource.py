from src.domain.repository.book_repository import BookRepository
from src.domain.entity.book import Book

class BookDatasource(BookRepository):
    books = [Book("harry potter"), Book("seigneur des anneaux"), Book("narnia")]

    def getBook(self, name):
        for book in self.books:
            if name == book.name:
                return book
        return None

    def getBooks(self):
        return self.books

    def updateBook(self, book: Book):
        for currentBook in self.books:
            if book.name == currentBook.name:
                currentBook.name = book.name
                currentBook.isAvailable = book.isAvailable