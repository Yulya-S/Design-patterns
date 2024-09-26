from Src.Core.abstract_logic import abstract_logic
from Src.Core.format_reporting import format_reporting
from Src.Reports.csv_report import csv_report
from Src.Reports.markdown_report import markdown_report
from Src.Core.abstract_report import abstract_report

import Src.Reports as rps


class report_factory(abstract_logic):
    __reports: dict = {}

    def __init__(self) -> None:
        super().__init__()
        self.__reports[format_reporting.CSV] = rps.csv_report.csv_report
        self.__reports[format_reporting.MARCDOWN] = markdown_report

    def create(self, format: format_reporting) -> abstract_report:
        if not isinstance(format, format_reporting):
            raise self._custom_exception.type(type(format), format_reporting)
        if format not in self.__reports.keys():
            raise self.set_exception(ValueError(f"Указанный вариант формата не реализован!"))

        report = self.__reports[format]
        return report()

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
