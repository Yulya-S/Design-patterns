from Src.Core.Abstract_classes.abstract_report import abstract_report
from Src.Core.formats_and_methods.format_reporting import format_reporting
from Src.Core.custom_exceptions import custom_exceptions
from Src.Reports.OBS.turnover_balance_sheet import turnover_balance_sheet
from Src.data_reposity import data_reposity

import os
import json

class tbs_json_report(abstract_report):
    def __init__(self) -> None:
        super().__init__()
        self.__format = format_reporting.TBS

    # создание результата в формате dict
    def __create_dict_result(self, data: turnover_balance_sheet):
        custom_exceptions.type(data, turnover_balance_sheet)
        result = {}

        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(data.__class__, x)), dir(data)))
        reposity = data_reposity()
        nomenclatures = reposity.data[data_reposity.nomenclature_key()]
        for i in range(len(list(nomenclatures))):
            result[i] = {}
            for l in fields:
                if l != "period":
                    result[i][l] = data.__getattribute__(l)[i]
        result["period"] = data.period
        return result

    # создание отчета
    def create(self, data: turnover_balance_sheet):
        self.result = str(self.__create_dict_result(data))

    # сохранение результата в файл
    def upload_to_file(self, data: turnover_balance_sheet, path: str = "../Docs/reports/", file_name: str = "report"):
        custom_exceptions.type(data, turnover_balance_sheet)
        if not os.path.exists(path):
            custom_exceptions.other_exception(f"Папки {path} не существует")
        result = self.__create_dict_result(data)

        try:
            with open(f"{path}{file_name}.json", "w") as json_file:
                json_file.write(json.dumps(result))
            return True
        except:
            return False
