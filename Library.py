from Book import Book
from peewee import MySQLDatabase
from sql import BooksModel


class Library:
    __main = None

    def main(__main):
        if __main == None:
            __main = Library()
        return __main

    def __init__(self):
        self.__book_list =[]

    @property
    def count (self):
        return len(self.__book_list)

    def add(self, book:Book):
        assert isinstance(book, Book), "object is not Book instance"
        self.__book_list.extend(book)

    def removeAt(self, index:int):
        assert isinstance(index, int),"object is not Int instance"
        if index >= 0 and index < len(self.__book_list):
            return self.__book_list.pop(index)
        else:
            return None

    def getAt(self, index:int):
        assert isinstance(index, int),"object is not Int instance"
        if index >= 0 and index < len(self.__book_list):
            return self.__book_list.pop(index)
        return None

    def get_all(self):
        return iter(self.__book_list) 

    def __init__(self, data_base=MySQLDatabase('library', user='FOG', password='ilkaFOG29',
                                               host='localhost', port=3306)):
        self.__data_base = data_base
        self.__library_model = BooksModel()
        self.__library_model._meta.database = self.__data_base

    @staticmethod
    def __get_book(book):
        return Book(
            author=book.author,
            title=book.title,
            year=book.year
        )

    @staticmethod
    def __get_books(books):
        book_list = []
        for book in books:
            book_list.append(
                (
                    book.id,
                    Book(
                        author=book.author,
                        title=book.title,
                        year=book.year
                    )
                )
            )
        return book_list

    def remove_at(self, index: int):
        self.__library_model.get_by_id(index).delete_instance()

    def get_at(self, index: int):
        return self.__get_book(self.__library_model.get_by_id(index))


    def update_at(self, index, book: Book):
        instance: BooksModel
        instance = self.__library_model.get_by_id(index)
        instance.year = book.year
        instance.author = book.author
        instance.title = book.title
        instance.save()

    def connect(self):
        self.__data_base.connect()

    def close(self):
        self.__data_base.close()

    def add(self, book: Book):
        self.__library_model.create(
            author=book.author,
            year=book.year,
            title=book.title
        )

    def find_by_author(self, author):
        query = self.__library_model.select().where(BooksModel.author == author)
        return self.__get_books(query)

    def find_by_year(self, year):
        query = self.__library_model.select().where(BooksModel.year == year)
        return self.__get_books(query)

    def count(self):
        return self.__library_model.select().count()

    def get_all_books(self):
        query = self.__library_model.select()
        return self.__get_books(query)