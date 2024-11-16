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
        reposity = data_reposity()
        if warehouse not in reposity.data[data_reposity.warehouse_key()]:
            return
        self.__tbs.warehouse = warehouse

    @property
    def tbs(self):
        return self.__tbs

    def create(self):
        reposity = data_reposity()
        all_transactions = reposity.data[data_reposity.transaction_key()]
        nomenclatures = reposity.data[data_reposity.nomenclature_key()]

        for i in list(nomenclatures.keys()):
            current_filter = filter_model()
            current_filter.update_filter("warehouse", comparison_format.EQUAL, self.__tbs.warehouse)
            current_filter.update_filter("nomenclature", comparison_format.EQUAL, nomenclatures[i])
            current_filter.set_periods(self.__tbs.period[0], self.__tbs.period[1])
            prototype = nomenclature_prototype(all_transactions)
            result = prototype.create(all_transactions, current_filter)

            data = [0, 0]
            # данные за периода
            for i in result.data:
                data[int(not i.type)] += i.quantity
            data = data[0] - data[1]
            self.__tbs.current = data

            start_filter = filter_model()
            start_filter.update_filter("warehouse", comparison_format.EQUAL, self.__tbs.warehouse)
            current_filter.update_filter("nomenclature", comparison_format.EQUAL, nomenclatures[i])
            start_filter.set_periods(datetime.strptime("01-01-1900", "%d-%m-%Y"), self.__tbs.period[0])
            prototype = nomenclature_prototype(all_transactions)
            result = prototype.create(all_transactions, start_filter)

            data = [0, 0]
            # данные до периода
            for i in result.data:
                data[int(not i.type)] += i.quantity
            data = data[0] - data[1]
            self.__tbs.start = data
            self.__tbs.result = self.__tbs.start[-1] + self.__tbs.current[-1]
