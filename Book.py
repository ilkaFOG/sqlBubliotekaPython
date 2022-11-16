class Book:
    def __init__(self, title:str, author:str, year:int):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f'{self.title},{self.author},{self.year}'

    def __repr__(self):
        return f'{self.title},{self.author},{self.year}'

    @property
    def author (self):
        return self.__author

    @author.setter
    def author (self, author:str):
        assert isinstance(author, str), "Автор должен быть строкой"
        self.__author = author

    @property
    def year (self):
        return self.__year

    @year.setter
    def year (self, year:int):
        assert isinstance(year, int), "Год должен целочисленным"
        self.__year = year

    @property
    def title (self):
        return self.__title

    @title.setter
    def title (self, title:str):
        assert isinstance(title, str), "Название должно быть строкой"
        self.__title = title

