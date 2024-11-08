from Src.Core.Abstract_classes.abstract_report import abstract_report
from Src.Core.formats_and_methods.format_reporting import format_reporting
from Src.Core.custom_exceptions import custom_exceptions

import os


# rtf отчет
class rtf_report(abstract_report):
    def __init__(self) -> None:
        super().__init__()
        self.__format = format_reporting.CSV

    # создание отчета
    def create(self, data: list | dict):
        fields, data = self._create_fields(data)

        for field in fields:
            self.result += f"{str(field)}\t"
        self.result += "\n"

        for row in data:
            for field in fields:
                value = getattr(row, field)
                self.result += f"{str(value)}\t"
            self.result += "\n"

    # сохранение результата в файл
    def upload_to_file(self, data: list | dict, path: str = "../Docs/reports/", file_name: str = "report"):
        if not os.path.exists(path):
            custom_exceptions.other_exception(f"Папки {path} не существует")
        self.create(data)

        try:
            with open(f"{path}{file_name}.rtf", "w") as rtf_file:
                rtf_file.write(self.result)
            return True
        except:
            return False
