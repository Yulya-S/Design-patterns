from Src.Core.abstract_report import abstract_report
from Src.Core.format_reporting import format_reporting

import os

"""
Отчет формирует набор данных в формате markdown
"""


class xml_report(abstract_report):
    def __init__(self) -> None:
        super().__init__()
        self.__format = format_reporting.XML

    def creat(self, data: list | dict):
        fields, data = self._create_fields(data)

        self.result += '<?xml version="1.0"?>'
        self.result += "<table><tr>"
        for field in fields:
            self.result += f"<th>{str(field)}</th>"
        self.result += "</tr>"
        self.result += "\n"
        for row in data:
            self.result += "<tr>"
            for field in fields:
                value = getattr(row, field)
                self.result += f'<td>{str(value)}</td>'
            self.result += "</tr>"
        self.result += "</table>"

    def upload_to_file(self, data: list | dict, path: str = "../Docs/reports/", file_name: str = "report"):
        if not os.path.exists(path):
            self._custom_exceptions.other_exception(f"Папки {path} не существует")
        self.creat(data)
        with open(f"{path}{file_name}.xml", "w") as md_file:
            md_file.write(self.result)
