from Src.Core.abstract_report import abstract_report
from Src.Core.format_reporting import format_reporting

"""
Отчет формирует набор данных в формате csv
"""


class markdown_report(abstract_report):
    def __init__(self) -> None:
        super().__init__()
        self.__format = format_reporting.MARCDOWN

    def creat(self, data: list | dict):
        if isinstance(data, dict):
            dd = data.copy()
            data = list()
            for key in list(dd.keys()):
                data.append(dd[key])

        if not isinstance(data, list):
            raise self._custom_exceptions.type(type(data), list)
        if len(data) == 0:
            raise self._custom_exceptions.length(len(data), 1, "=")

        first_model = data[0]
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(first_model.__class__, x)),
                             dir(first_model)))

        for field in fields:
            self.result += f"{str(field)}:"
        self.result += "\n"

        for row in data:
            for field in fields:
                value = getattr(row, field)
                self.result += f"{str(value)};"
            self.result += "\n"