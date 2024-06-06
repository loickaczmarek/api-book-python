from src.domain.repository.book_repository import BookRepository


class GetBookByNameUseCase:
    bookRepository: BookRepository

    def __init__(self, bookRepository: BookRepository):
        self.bookRepository = bookRepository

    def getBook(self, name: str):
        return self.bookRepository.getBook(self.bookRepository, name)
