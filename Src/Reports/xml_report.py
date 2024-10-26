from Src.Core.Abstract_classes.abstract_report import abstract_report
from Src.Core.formats_and_methods.format_reporting import format_reporting
from Src.Core.custom_exceptions import custom_exceptions

from dicttoxml import dicttoxml
import os


# Отчет формирует набор данных в формате xml
class xml_report(abstract_report):
    def __init__(self) -> None:
        super().__init__()
        self.__format = format_reporting.XML

    def create(self, data: list | dict):
        result = self._data_to_dict(data)
        self.result = str(dicttoxml(result))

    def upload_to_file(self, data: list | dict, path: str = "../Docs/reports/", file_name: str = "report"):
        if not os.path.exists(path):
            custom_exceptions.other_exception(f"Папки {path} не существует")
        self.create(data)

        try:
            with open(f"{path}{file_name}.xml", "w") as xml_file:
                xml_file.write(self.result)
            return True
        except:
            return False
