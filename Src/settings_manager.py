from Src.custom_exceptions import custom_exceptions
from Src.models.settings import settings
from Src.abstract_logic import abstract_logic

import json
import os

"""
Менеджер настроек
"""


class settings_manager(abstract_logic):
    __file_name = "settings.json"
    __path = f"{os.curdir}"
    __settings: settings = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        if self.__settings is None:
            self.__settings = self.__default_setting

    @property
    def settings(self):
        return self.__settings

    def open(self, file_name: str = "", path: str = ""):
        if not isinstance(file_name, str):
            raise custom_exceptions().type(file_name, str)
        if not isinstance(path, str):
            raise custom_exceptions().type(path, str)

        if file_name != "":
            self.__file_name = file_name
        if path != "":
            self.__path = path

        try:
            full_name = f"{self.__path}{os.sep}{self.__file_name}"
            stream = open(full_name)
            data = json.load(stream)
            self.convert(data)
            return True
        except Exception as ex:
            self.__settings = self.__default_setting
            self.set_exception(ex)
            return False

    def convert(self, data: {}):
        fields = dir(self.__settings)
        for key in data.keys():
            if key in fields:
                self.__settings.__setattr__(key, data[key])

    @property
    def current_settings(self) -> settings:
        return self.__settings

    @property
    def __default_setting(self) -> settings:
        data = settings()
        data.inn = "380008092020"
        data.account = "38000809202"
        data.correspondent_account = "38000809202"
        data.bic = "380008092"
        data.organization_name = "Рога и копыта"
        data.type_ownership = "OOOOO"
        return data

    def set_exception(self, ex: Exception):
        if not isinstance(ex, Exception):
            raise custom_exceptions().type(ex, Exception)
        self._inner_set_exception(ex)
