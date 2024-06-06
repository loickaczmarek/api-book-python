from fastapi import FastAPI
from src.entrypoint import bookRouter

app = FastAPI()

app.include_router(bookRouter)

#books = [Book("harry potter"), Book("seigneur des anneaux"), Book("narnia")]


#@app.get("/books/{name}")
#def read_item(name):
#    for book in books:
#        if name == book.name:
#            return book
#    return None


#@app.get("/books")
#def read_items():
#    return books

#class BookUpdate(BaseModel):
#    name: str
#    rent: bool

#@bookRouter.post("books")
#def updateBook(bookUpdate: BookUpdate):
#    for book in books:
#        if bookUpdate.name == book.name:
#            if bookUpdate.rent:
#               book.rentBook()
#           else:
#               book.returnBook()
#           return "ok"
#  return "ko"
