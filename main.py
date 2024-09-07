import json
import os


class settings:
    __inn = ""
    __account = ""
    __correspondent_account = ""
    __bic = ""
    __organization_name = ""
    __type_ownership = ""

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str) or len(value) != 12:
            raise TypeError("Некорректно передан параметр!")
        self.__inn = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        if not isinstance(value, str) or len(value) != 11:
            raise TypeError("Некорректно передан параметр!")
        self.__account = value

    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        if not isinstance(value, str) or len(value) != 11:
            raise TypeError("Некорректно передан параметр!")
        self.__correspondent_account = value

    @property
    def bic(self):
        return self.__bic

    @bic.setter
    def bic(self, value: str):
        if not isinstance(value, str) or len(value) != 9:
            raise TypeError("Некорректно передан параметр!")
        self.__bic = value

    @property
    def organization_name(self):
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно передан параметр!")
        self.__organization_name = value

    @property
    def type_ownership(self):
        return self.__type_ownership

    @type_ownership.setter
    def type_ownership(self, value: str):
        if not isinstance(value, str) or len(value) != 5:
            raise TypeError("Некорректно передан параметр!")
        self.__type_ownership = value


class settings_manager:
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


manager1 = settings_manager()
manager1.open("settings.json")
print(f"settings1: {manager1.settings.inn}")

manager2 = settings_manager()
manager2.open("settings1.json")
print(f"settings2: {manager2.settings.inn}")
