from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.formats_and_methods.comparison_format import comparison_format

from Src.logic.nomenclature_prototype import nomenclature_prototype
from Src.Reports.OBS.turnover_balance_sheet import turnover_balance_sheet
from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.Dto.filter import filter_model
from Src.data_reposity import data_reposity
from datetime import datetime


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

        # данные до периода
        for i in result.data:
            self.__tbs.start[int(not i.type)] += i.quantity

        start_filter = filter_model()
        start_filter.update_filter("warehouse", comparison_format.EQUAL, warehouse)
        start_filter.set_periods(datetime.strptime("01-01-1900", "%d-%m-%Y"), period[1])
        prototype = nomenclature_prototype(transactions)
        result = prototype.create(transactions, start_filter)

        # данные за период
        for i in result.data:
            self.__tbs.current[int(not i.type)] += i.quantity
        self.__calculation()

    # расчет результатов
    def __calculation(self):
        result = self.__tbs.start[0] - self.__tbs.start[1]
        result += self.__tbs.current[0] - self.__tbs.current[1]
        self.__tbs.result[int(result < 0)] = result

    @property
    def tbs(self):
        return self.__tbs

    @property
    def result(self):
        return self.__tbs.result
