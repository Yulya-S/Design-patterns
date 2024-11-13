from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.formats_and_methods.comparison_format import comparison_format

from Src.logic.nomenclature_prototype import nomenclature_prototype
from Src.Reports.OBS.turnover_balance_sheet import turnover_balance_sheet
from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.Dto.filter import filter_model
from Src.data_reposity import data_reposity

from datetime import datetime
import os
import json


class tbs_calculation:
    __tbs: turnover_balance_sheet = turnover_balance_sheet()

    def __init__(self, period: [datetime, datetime], warehouse: warehouse_model):
        custom_exceptions.elements_is_type(period, datetime)
        self.__tbs.period = period
        transactions = data_reposity()
        if warehouse not in transactions.data[data_reposity.warehouse_key()]:
            return
        self.__tbs.warehouse = warehouse
        transactions = transactions.data[data_reposity.transaction_key()]

        current_filter = filter_model()
        current_filter.update_filter("warehouse", comparison_format.EQUAL, warehouse)
        current_filter.set_periods(period[0], period[1])
        prototype = nomenclature_prototype(transactions)
        result = prototype.create(transactions, current_filter)

        data = [0, 0]
        # данные за периода
        for i in result.data:
            data[int(not i.type)] += i.quantity
        self.__tbs.current = data

        start_filter = filter_model()
        start_filter.update_filter("warehouse", comparison_format.EQUAL, warehouse)
        start_filter.set_periods(datetime.strptime("01-01-1900", "%d-%m-%Y"), period[0])
        prototype = nomenclature_prototype(transactions)
        result = prototype.create(transactions, start_filter)

        data = [0, 0]
        # данные до периода
        for i in result.data:
            data[int(not i.type)] += i.quantity
        self.__tbs.start = data
        self.__calculation()

    # расчет результатов
    def __calculation(self):
        result = self.__tbs.start[0] - self.__tbs.start[1]
        result += self.__tbs.current[0] - self.__tbs.current[1]
        data = [0, 0]
        data[int(result < 0)] = result
        self.__tbs.result = data

    @property
    def tbs(self):
        return self.__tbs

    @property
    def result(self) -> dict:
        result = {}
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(self.tbs.__class__, x)),
                             dir(self.tbs)))
        for i in fields:
            result[i] = self.__tbs.__getattribute__(i)
        return result

    def save(self, path: str = "..\\..\\Docs\\reports\\", file_name: str = "tbs"):
        if not os.path.exists(path):
            custom_exceptions.other_exception(f"Папки {path} не существует")
        try:
            with open(f"{path}{file_name}.json", "w") as json_file:
                json_file.write(json.dumps(self.return_result))
            return True
        except:
            return False
