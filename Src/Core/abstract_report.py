from abc import ABC, abstractmethod
from Src.Core.format_reporting import format_reporting
from Src.Core.custom_exceptions import custom_exceptions


class abstract_report(ABC):
    __format: format_reporting == format_reporting.CSV
    __result: str = ""
    _custom_exceptions: custom_exceptions = custom_exceptions()

    """
    Сформировать
    """

    @abstractmethod
    def creat(selfd, data: list):
        pass

    """
    Тип формата
    """

    # @abstractmethod
    @property
    def format(self) -> format_reporting:
        return self.__format

    """
    Результат формирования отчета
    """

    @property
    def result(self) -> str:
        return self.__result

    @result.setter
    def result(self, value: str):
        self._custom_exceptions.type(value, str)
        self.__result = value
