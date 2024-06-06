from src.domain.repository.book_repository import BookRepository
from src.domain.entity.book import Book


class RentBookUseCase:
    bookRepository: BookRepository

    def __init__(self, bookRepository: BookRepository):
        self.bookRepository = bookRepository

    def rentBook(self, book: Book):
        book.isAvailable = False
        self.bookRepository.updateBook(self.bookRepository, book)
