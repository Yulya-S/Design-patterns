from Src.Core.abstract_report import abstract_report
from Src.Core.format_reporting import format_reporting

import os

"""
Отчет формирует набор данных в формате markdown
"""


class json_report(abstract_report):
    def __init__(self) -> None:
        super().__init__()
        self.__format = format_reporting.JSON

    def creat(self, data: list | dict):
        fields, data = self._create_fields(data)

        self.result += '{'
        for row in data:
            self.result += f'"{getattr(row, fields[-1])}": '
            self.result += '{'
            for i in range(len(fields) - 1):
                value = getattr(row, fields[i])
                self.result += f'"{fields[i]}": {str(value)},'
            self.result += '},'
        self.result += '}'

    def upload_to_file(self, data: list | dict, path: str = "../Docs/reports/", file_name: str = "report"):
        if not os.path.exists(path):
            self._custom_exceptions.other_exception(f"Папки {path} не существует")
        self.creat(data)
        with open(f"{path}{file_name}.json", "w") as md_file:
            md_file.write(self.result)
