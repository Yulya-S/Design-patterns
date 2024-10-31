from abc import ABC, abstractmethod
from Src.Core.custom_exceptions import custom_exceptions


class abstract_prototype(ABC):
    __data = []

    def __init__(self, source: list) -> None:
        super().__init__()
        custom_exceptions.type(source, list)
        self.__data = source

    @abstractmethod
    def create(self, data: list, filter):
        custom_exceptions.type(data, list)

    @property
    def data(self) -> list:
        return self.__data

    @data.setter
    def data(self, value: list):
        self.__data = value