from Src.Core.abstract_report import abstract_report
from Src.Core.format_reporting import format_reporting

"""
Отчет формирует набор данных в формате csv
"""


class csv_report(abstract_report):
    def __init__(self) -> None:
        super().__init__()
        self.__format = format_reporting.CSV

    def creat(self, data: list | dict):
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

        for field in fields:
            self.result += f"{str(field)}:"
        self.result += "\n"

        for row in data:
            for field in fields:
                value = getattr(row, field)
                self.result += f"{str(value)};"
            self.result += "\n"
