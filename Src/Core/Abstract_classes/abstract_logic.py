from abc import ABC, abstractmethod
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.event_type import event_type


# Абстрактный класс для обработки логики
class abstract_logic(ABC):
    __error_text: str = ""

    @property
    def error_text(self) -> str:
        return self.__error_text.strip()

    @error_text.setter
    def error_text(self, message: str):
        custom_exceptions.type(message, str)
        self.__error_text = message.strip()

    @property
    def is_error(self) -> bool:
        return self.error_text != ""

    def _inner_set_exception(self, ex: Exception):
        self.__error_text = f"Ошибка! Исключение {ex}"

    # Абстрактный метод для загрузки и обработки исключений
    @abstractmethod
    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)

    # Обработка
    @abstractmethod
    def handle_event(self, type: event_type, params):
        custom_exceptions.type(type, event_type)
