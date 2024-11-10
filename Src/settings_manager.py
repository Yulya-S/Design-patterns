from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.event_type import event_type

from Src.settings import settings_model
from Src.Reports.report_factory import report_factory
from Src.logic.observe_service import observe_service

from datetime import datetime
import json
import os


# Менеджер настроек
class settings_manager(abstract_logic):
    __file_name = "settings.json"
    __path = f"{os.curdir}"
    __settings: settings_model = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        if self.__settings is None:
            self.__settings = self.__default_setting
        observe_service.append(self)

    @property
    def settings(self):
        return self.__settings

    # чтение настроек из файла
    def open(self, file_name: str = "", path: str = ""):
        custom_exceptions.type(file_name, str)
        custom_exceptions.type(path, str)

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

    # применение значений
    def convert(self, data: {}):
        fields = dir(self.__settings)
        for key in data.keys():
            if key in fields:
                self.__settings.__setattr__(key, data[key])

    @property
    def current_settings(self) -> settings:
        return self.__settings

    # стандартные настройки
    @property
    def __default_setting(self) -> settings:
        data = settings_model()
        data.inn = "380008092020"
        data.account = "38000809202"
        data.correspondent_account = "38000809202"
        data.bic = "380008092"
        data.organization_name = "Рога и копыта"
        data.type_ownership = "OOOOO"
        data.report_format = report_factory.create_default
        data.block_period = datetime.now()
        return data

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)

    def handle_event(self, type: event_type, params):
        super().handle_event(type, params)
