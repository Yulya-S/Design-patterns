from Src.Core.custom_exceptions import custom_exceptions
from datetime import datetime


class turnover_balance_sheet:
    __period: [datetime, datetime]
    __debet: int = 0
    __kredit: int = 0

    @property
    def debet(self):
        return self.__debet

    @property
    def kredit(self):
        return self.__kredit

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, value: list):
        custom_exceptions.elements_is_type(value, datetime)
        self.__period = value