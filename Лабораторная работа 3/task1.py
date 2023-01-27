"""
1. Атрибуты name и author должны быть неизменны
2. __private атрибуты и методы где они используются не наследуются
---> Переписываем __setattr__, возможно я не понял задание, если что поясните, пожалуйста
"""


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __setattr__(self, key, value):
        if self.__dict__.get(key) is None or self.__dict__.get(key) is None:
            object.__setattr__(self, key, value)
        else:
            if key != "name" and key != "author":
                object.__setattr__(self, key, value)
            else:
                raise AttributeError("Данный атрибут изменяться не может")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. Печатная книга."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        if type(pages) is not int:
            raise TypeError('Число страниц должно быть целым числом')
        if pages > 0:
            self.pages = pages
        else:
            raise ValueError("Число страниц должно быть положительным")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс книги. Аудиконига."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        if type(duration) is not float:
            raise TypeError('Продолжительность должна быть числом с плавающей точкой')
        if duration > 0:
            self.duration = duration
        else:
            raise ValueError("Продолжительность должна быть положительной")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
