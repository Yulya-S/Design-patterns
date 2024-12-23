from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.Core.formats_and_methods.format_reporting import format_reporting
from Src.Core.Abstract_classes.abstract_report import abstract_report
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.event_type import event_type
from Src.settings import settings_model

from Src.Reports.csv_report import csv_report
from Src.Reports.markdown_report import markdown_report
from Src.Reports.json_report import json_report
from Src.Reports.rtf_report import rtf_report
from Src.Reports.xml_report import xml_report
from Src.Reports.OBS.tbs_json_report import tbs_json_report


# фабрика формата отчета
class report_factory(abstract_logic):
    __reports: dict = {}
    __settings: settings_model = None

    def __init__(self, settings: settings_model) -> None:
        super().__init__()
        custom_exceptions.type(settings, settings_model)
        self.__settings = settings
        if self.__settings.report_handlers == []:
            self.__reports[format_reporting.CSV.value] = csv_report
            self.__reports[format_reporting.MARCDOWN.value] = markdown_report
            self.__reports[format_reporting.JSON.value] = json_report
            self.__reports[format_reporting.XML.value] = xml_report
            self.__reports[format_reporting.RTF.value] = rtf_report
            self.__reports[format_reporting.TBS.value] = tbs_json_report
        else:
            for i in self.__settings.report_handlers:
                if i["type"] not in self.__reports.keys():
                    try:
                        self.__reports[i["type"]] = eval(i["hendler"])
                    except:
                        custom_exceptions.other_exception(f"не существует способа форматирования отчета: {i['hengler']}")

    # создание класса отчета нужного формата
    def create(self, format: format_reporting) -> abstract_report:
        custom_exceptions.type(format, format_reporting)

        if format.value not in self.__reports.keys():
            self.set_exception(
                custom_exceptions.other_exception(f"Указанный вариант формата {format} не реализован!"))
            return None

        report = self.__reports[format.value]
        return report()

    # создание класса отчета с форматом по умолчанию
    @property
    def create_default(self):
        return self.create(self.__settings.default_report_format)

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)

    def handle_event(self, type: event_type, params):
        super().handle_event(type, params)
