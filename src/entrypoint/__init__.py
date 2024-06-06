from src.entrypoint.book_controller import BookController
from src.domain.usecase.get_book_by_name_usecase import GetBookByNameUseCase
from src.domain.usecase.get_all_books_usecase import GetAllBooksUseCase
from src.infrastructure.datasource.book_datasource import BookDatasource
from fastapi import APIRouter

bookRouter = APIRouter()

bookController = BookController(GetBookByNameUseCase(BookDatasource)
                            , GetAllBooksUseCase(BookDatasource))

@bookRouter.get("/books/{name}")
def getBook(name):
    return bookController.getBook(name)


@bookRouter.get("/books")
def getBooks():
    return bookController.getBooks()