from abc import ABC, abstractmethod
from Src.Core.custom_exceptions import custom_exceptions

"""
Абстрактный класс для обработки логики
"""


class abstract_logic(ABC):
    __error_text: str = ""
    __custom_exception = custom_exceptions()

    @property
    def error_text(self) -> str:
        return self.__error_text.strip()

    @property
    def custom_exception(self):
        return self.__custom_exception

    @error_text.setter
    def error_text(self, message: str):
        if not isinstance(message, str):
            raise self.custom_exception.type(type(message), str)
        self.__error_text = message.strip()

    @property
    def is_error(self) -> bool:
        return self.error_text != ""

    def _inner_set_exception(self, ex: Exception):
        self.__error_text = f"Ошибка! Исключение {ex}"

    """
    Абстрактный метод для загрузки и обработки исключений
    """

    @abstractmethod
    def set_exception(self, ex: Exception):
        pass
