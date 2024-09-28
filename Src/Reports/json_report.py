from Src.Core.abstract_report import abstract_report
from Src.Core.format_reporting import format_reporting
from Src.Core.base_models import base_model_name, base_model_code

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

        self.result += '{\n'
        for row in data:
            self.result += f'"{getattr(row, fields[-1])}": '
            self.result += '\n{\n'
            for i in range(len(fields) - 1):
                value = getattr(row, fields[i])
                self.result += f'"{fields[i]}": {self.__recursion(value)},\n'
            self.result += '},\n'
        self.result += '}\n'

    def __recursion(self, data, text: str = ""):
        if isinstance(data, list) or isinstance(data, dict):
            fields, data = self._create_fields(data)
            if len(fields) == 0:
                return data
            text += '[\n'
            for row in data:
                text += f'"{getattr(row, fields[-1])}": '
                text += '{\n'
                for i in range(len(fields) - 1):
                    value = getattr(row, fields[i])
                    text += f'"{fields[i]}": {self.__recursion(value, text)},\n'
                text += '},\n'
            text += ']\n'
            data = text
        elif issubclass(type(data), base_model_name) or issubclass(type(data), base_model_code):
            fields, data = self._create_fields([data])
            if len(fields) == 0:
                return data
            for row in data:
                text += f'"{getattr(row, fields[-1])}": '
                text += '{\n'
                for i in range(len(fields) - 1):
                    value = getattr(row, fields[i])
                    text += f'"{fields[i]}": {self.__recursion(value, text)},\n'
                text += '},\n'
            data = text
        return data


    def upload_to_file(self, data: list | dict, path: str = "../Docs/reports/", file_name: str = "report"):
        if not os.path.exists(path):
            self._custom_exceptions.other_exception(f"Папки {path} не существует")
        self.creat(data)

        try:
            with open(f"{path}{file_name}.json", "w") as json_file:
                json_file.write(self.result)
            return True
        except:
            return False
