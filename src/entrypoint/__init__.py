from src.entrypoint.book_controller import BookController
from src.domain.usecase.get_book_by_name_usecase import GetBookByNameUseCase
from src.domain.usecase.get_all_books_usecase import GetAllBooksUseCase
from src.domain.usecase.rent_book_usecase import RentBookUseCase
from src.domain.usecase.return_book_usecase import ReturnBookUseCase
from src.infrastructure.datasource.book_datasource import BookDatasource
from src.domain.entity.book import Book
from fastapi import APIRouter
from pydantic import BaseModel

bookRouter = APIRouter()

bookController = BookController(GetBookByNameUseCase(BookDatasource),
                             GetAllBooksUseCase(BookDatasource),
                                RentBookUseCase(BookDatasource),
                                ReturnBookUseCase(BookDatasource))

@bookRouter.get("/books/{name}")
def getBook(name):
    return bookController.getBook(name)


@bookRouter.get("/books")
def getBooks():
    return bookController.getBooks()

class BookData(BaseModel):
    name: str
    isAvailable: bool

@bookRouter.post("/books")
def updateBook(book: BookData):
    bookController.updateBook(book)
    return "ok"