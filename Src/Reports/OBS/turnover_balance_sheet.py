from Src.Core.custom_exceptions import custom_exceptions
from Src.models.Warehouse.warehouse_model import warehouse_model
from datetime import datetime


class turnover_balance_sheet:
    __period: [datetime, datetime]
    __warehouse: warehouse_model = None
    __debet_start: int = 0
    __debet: int = 0
    __debet_result: int = 0
    __kredit_start: int = 0
    __kredit: int = 0
    __kredit_result: int = 0

    @property
    def start(self):
        return [self.__debet_start, self.__kredit_start]

    @start.setter
    def start(self, value: list):
        custom_exceptions.elements_is_type(value, int)
        custom_exceptions.length_noequal(value, 2)
        self.__debet_start = value[0]
        self.__kredit_start = value[1]

    @property
    def current(self):
        return [self.__debet, self.__kredit]

    @current.setter
    def current(self, value: list):
        custom_exceptions.elements_is_type(value, int)
        custom_exceptions.length_noequal(value, 2)
        self.__debet = value[0]
        self.__kredit = value[1]

    @property
    def result(self):
        return [self.__kredit_result, self.__kredit_result]

    @result.setter
    def result(self, value: list):
        custom_exceptions.elements_is_type(value, int)
        custom_exceptions.length_noequal(value, 2)
        self.__debet_result = value[0]
        self.__kredit_result = value[1]

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, value: list):
        custom_exceptions.elements_is_type(value, datetime)
        self.__period = value

    @property
    def warehouse(self):
        return self.__warehouse

    @warehouse.setter
    def warehouse(self, value: warehouse_model):
        custom_exceptions.type(value, warehouse_model)
        self.__warehouse = value
