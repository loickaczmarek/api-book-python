from src.domain.repository.book_repository import BookRepository
from src.domain.entity.book import Book


class ReturnBookUseCase:
    bookRepository: BookRepository

    def __init__(self, bookRepository: BookRepository):
        self.bookRepository = bookRepository

    def returnBook(self, book: Book):
        book.isAvailable = True
        self.bookRepository.updateBook(self.bookRepository, book)
