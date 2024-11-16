from Src.Core.custom_exceptions import custom_exceptions
from Src.models.Warehouse.warehouse_model import warehouse_model
from datetime import datetime


class turnover_balance_sheet:
    __period: [datetime, datetime]
    __warehouse: warehouse_model = None
    __start: list = []
    __current: list = []
    __result: list = []

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, value: int):
        custom_exceptions.type(value, int)
        self.__start.append(value)

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, value: int):
        custom_exceptions.type(value, int)
        self.__current.append(value)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value: int):
        custom_exceptions.type(value, int)
        self.__result.append(value)

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
