from src.domain.repository.book_repository import BookRepository


class GetAllBooksUseCase:
    bookRepository: BookRepository

    def __init__(self, bookRepository: BookRepository):
        self.bookRepository = bookRepository

    def getAllBooks(self):
        return self.bookRepository.getBooks(self.bookRepository)