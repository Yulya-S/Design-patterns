from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.event_type import event_type
from Src.Core.formats_and_methods.log_level import log_level

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

    # изменение настроек
    def save(self, value: list):

        custom_exceptions.type(value, list)
        custom_exceptions.length_noequal(value, 2)
        custom_exceptions.type(value[0], str)

        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(settings_manager, x)),
                             dir(settings_manager)))

        if value[0] in fields and type(self.settings.__getattribute__(value[0])) == type(value[1]):
            self.settings.__setattr__(value[0], value[1])
            self.settings.generate_data = False
            if value[0] == "block_period":
                value[1] = str(value[1].date())
        try:
            stream = open(f".{os.sep}settings.json", "r")
            j = json.load(stream)
            j[value[0]] = value[1]
            stream.close()
            json_file = open(f".{os.sep}settings.json", "w")
            json_file.write(json.dumps(dict(j)))
            json_file.close()
            return f"{True}"
        except:
            return f"{False}"

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
        data.log_level: log_level.DEBUG
        return data

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)

    def handle_event(self, type: event_type, params):
        super().handle_event(type, params)
        if type == event_type.CHANGE_BLOCK_PERIOD:
            self.save(params)
