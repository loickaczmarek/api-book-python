from src.domain.entity.book import Book


class BookRepository:

    def getBook(self, name):
        raise "implements me"

    def getBooks(self):
        raise "implements me"

    def updateBook(self, book: Book):
        raise "implements me"
