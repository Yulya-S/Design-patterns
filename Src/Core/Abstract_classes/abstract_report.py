from abc import ABC, abstractmethod
from Src.Core.formats_and_methods.format_reporting import format_reporting
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.Abstract_classes.base_models import base_model_name, base_model_code


class abstract_report(ABC):
    __format: format_reporting == format_reporting.CSV
    __result: str = ""

    """
    Сформировать
    """

    @abstractmethod
    def create(self, data: list):
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
        custom_exceptions.type(value, str)
        self.__result = value

    def _create_fields(self, data: list | dict):
        if isinstance(data, dict):
            dd = data.copy()
            data = list()
            for key in list(dd.keys()):
                data.append(dd[key])

        custom_exceptions.type(data, list)
        if len(data) == 0:
            custom_exceptions.other_exception("Набор данных пуст!")

        first_model = data[0]
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(first_model.__class__, x)),
                             dir(first_model)))

        return fields, data

    @abstractmethod
    def upload_to_file(self, data: list | dict, path: str = "../Docs/reports/", file_name: str = "report"):
        pass

    def _data_to_dict(self, data):
        if isinstance(data, list):
            fields, data = self._create_fields(data)
            if len(fields) == 0:
                return data
            result = {}
            if len(fields) == 0:
                return data
            for row in data:
                result[getattr(row, fields[-1])] = {}
                for i in range(len(fields)):
                    result[getattr(row, fields[-1])][fields[i]] = self._data_to_dict(getattr(row, fields[i]))
            data = result
        elif isinstance(data, dict):
            if len(list(data.keys())) == 0:
                return data
            result = {}
            for field in list(data.keys()):
                result[field] = self._data_to_dict(data[field])
            data = result
        elif issubclass(type(data), base_model_name) or issubclass(type(data), base_model_code):
            fields, data = self._create_fields([data])
            result = {}
            if len(fields) == 0:
                return data
            for row in data:
                for i in range(len(fields)):
                    result[fields[i]] = self._data_to_dict(getattr(row, fields[i]))
            data = result
        return data
