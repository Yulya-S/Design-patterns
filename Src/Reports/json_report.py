import json

from Src.Core.Abstract_classes.abstract_report import abstract_report
from Src.Core.formats_and_methods.format_reporting import format_reporting
from Src.Core.custom_exceptions import custom_exceptions

import os


# json отчет
class json_report(abstract_report):
    def __init__(self) -> None:
        super().__init__()
        self.__format = format_reporting.JSON

    # создание отчета
    def create(self, data: list | dict):
        self.result = str(self._data_to_dict(data))

    def dict_result(self, data: list | dict):
        return self._data_to_dict(data)

    # сохранение результата в файл
    def upload_to_file(self, data: list | dict, path: str = "..\\Docs\\reports\\", file_name: str = "report"):
        if not os.path.exists(path):
            custom_exceptions.other_exception(f"Папки {path} не существует")

        self.create(data)
        result = self._data_to_dict(data)

        try:
            with open(f"{path}{file_name}.json", "w") as json_file:
                json_file.write(json.dumps(dict(result)))
            return True
        except:
            return False
