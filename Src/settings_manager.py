import json
import os
from Src.models.settings import settings


class settings_manager():
    __file_name = "settings.json"
    __path = f"{os.curdir}"
    __settings: settings = settings()

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    def open(self, file_name: str = "", path: str = ""):
        if not isinstance(file_name, str) or not isinstance(path, str):
            raise TypeError("Некорректно переданы параметры!")
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
        except:
            self.__settings = self.__default_setting
            return False

    def convert(self, data: {}):
        fields = dir(self.__settings)
        for key in data.keys():
            if key in fields:
                self.__settings.__setattr__(key, data[key])

    # Настройки
    @property
    def settings(self):
        return self.__settings

    @property
    def __default_setting(self):
        data = settings()
        data.inn = "380008092020"
        data.account = "38000809202"
        data.correspondent_account = "38000809202"
        data.bic = "380008092"
        data.organization_name = "Рога и копыта"
        data.type_ownership = "OOOOO"
        return data