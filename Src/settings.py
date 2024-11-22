from Src.Core.formats_and_methods.format_reporting import format_reporting
from Src.Core.custom_exceptions import custom_exceptions

from datetime import datetime


# Модель настроек
class settings_model:
    # настройки компании
    __inn: str = ""
    __account: str = ""
    __correspondent_account: str = ""
    __bic: str = ""
    __organization_name: str = ""
    __type_ownership: str = ""
    __generate_data: bool = True

    # настройки отчетов
    __default_report_format: format_reporting = format_reporting.CSV
    __report_handlers: list = list()

    __block_period: datetime = datetime.now()

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        custom_exceptions.type(value, str)
        custom_exceptions.length_noequal(value, 12)
        self.__inn = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        custom_exceptions.type(value, str)
        custom_exceptions.length_noequal(value, 11)
        self.__account = value

    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        custom_exceptions.type(value, str)
        custom_exceptions.length_noequal(value, 11)
        self.__correspondent_account = value

    @property
    def bic(self):
        return self.__bic

    @bic.setter
    def bic(self, value: str):
        custom_exceptions.type(value, str)
        custom_exceptions.length_noequal(value, 9)
        self.__bic = value

    @property
    def organization_name(self):
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        custom_exceptions.type(value, str)
        self.__organization_name = value

    @property
    def type_ownership(self):
        return self.__type_ownership

    @type_ownership.setter
    def type_ownership(self, value: str):
        custom_exceptions.type(value, str)
        custom_exceptions.length_noequal(value, 5)
        self.__type_ownership = value

    @property
    def generate_data(self):
        return self.__generate_data

    @generate_data.setter
    def generate_data(self, value: bool):
        custom_exceptions.type(value, bool)
        self.__generate_data = value

    @property
    def default_report_format(self):
        return self.__default_report_format

    @default_report_format.setter
    def default_report_format(self, value: int):
        custom_exceptions.type(value, int)
        try:
            self.__default_report_format = format_reporting(value)
        except:
            custom_exceptions.other_exception(f"Ошибка преобразования {value} в format_reporting")

    @property
    def report_handlers(self):
        return self.__report_handlers

    @report_handlers.setter
    def report_handlers(self, value: list):
        custom_exceptions.type(value, list)
        self.__report_handlers = value

    @property
    def block_period(self):
        return self.__block_period

    @block_period.setter
    def block_period(self, value: datetime | str):
        if type(value) not in [datetime, str]:
            custom_exceptions.other_exception(f"Некорректно передан параметр! {type(value)} not in [datetime, str]")
        if isinstance(value, str):
            self.__block_period = datetime.strptime(value, "%d-%m-%Y")
        else:
            self.__block_period = value
