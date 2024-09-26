from Src.Core.abstract_report import abstract_report
from Src.Core.format_reporting import format_reporting

import os

"""
Отчет формирует набор данных в формате csv
"""


class rtf_report(abstract_report):
    def __init__(self) -> None:
        super().__init__()
        self.__format = format_reporting.CSV

    def creat(self, data: list | dict):
        fields, data = self._create_fields(data)

        for field in fields:
            self.result += f"{str(field)}\t"
        self.result += "\n"

        for row in data:
            for field in fields:
                value = getattr(row, field)
                self.result += f"{str(value)}\t"
            self.result += "\n"

    def upload_to_file(self, data: list | dict, path: str = "../Docs/reports/", file_name: str = "report"):
        if not os.path.exists(path):
            self._custom_exceptions.other_exception(f"Папки {path} не существует")
        self.creat(data)
        with open(f"{path}{file_name}.rtf", "w") as csv_file:
            csv_file.write(self.result)