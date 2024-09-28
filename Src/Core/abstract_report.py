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
    def creat(self, data: list):
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

    def _create_fields(self, data: list | dict):
        if isinstance(data, dict):
            dd = data.copy()
            data = list()
            for key in list(dd.keys()):
                data.append(dd[key])

        self._custom_exceptions.type(data, list)
        if len(data) == 0:
            self._custom_exceptions.other_exception("Набор данных пуст!")

        first_model = data[0]
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(first_model.__class__, x)),
                             dir(first_model)))

        return fields, data

    @abstractmethod
    def upload_to_file(self, data: list | dict, path: str = "../Docs/reports/", file_name: str = "report"):
        pass
