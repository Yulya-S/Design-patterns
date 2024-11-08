from abc import ABC, abstractmethod
from Src.Core.custom_exceptions import custom_exceptions

#  класс абстрактного прототипа (для фильтров)
class abstract_prototype(ABC):
    __data = []

    @property
    def data(self) -> list:
        return self.__data

    @data.setter
    def data(self, value: list):
        self.__data = value

    def __init__(self, source: list) -> None:
        super().__init__()
        custom_exceptions.type(source, list)
        self.__data = source

    # Создание фильтра
    @abstractmethod
    def create(self, data: list, filter):
        custom_exceptions.type(data, list)