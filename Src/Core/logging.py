from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.Core.formats_and_methods.log_level import log_level
from Src.Core.event_type import event_type

from Src.settings_manager import settings_manager
from Src.logic.observe_service import observe_service

from datetime import datetime


class logging(abstract_logic):
    __settings: settings_manager = settings_manager()

    def __init__(self):
        observe_service.append(self)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(logging, cls).__new__(cls)
        return cls.instance

    # Логи типа DEBUG
    def __DEBUG(self, details):
        with open("log.txt", "a") as f:
            text = f"[DEBUG]\t{datetime.now()}\t{details}"
            f.write(text)

    # Логи типа INFO
    def __INFO(self, details):
        with open("log.txt", "a") as f:
            text = f"[INFO]\t{datetime.now()}\t{details}"
            f.write(text)

    # Логи типа ERROR
    def __ERROR(self, details):
        with open("log.txt", "a") as f:
            text = f"[ERROR]\t{datetime.now()}\t{details}"
            f.write(text)

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)

    def handle_event(self, type: event_type, params):
        super().handle_event(type, params)
        if type == event_type.DEBUG_LOG and self.__settings.settings.log_level <= log_level.DEBUG.value:
            self.__DEBUG(params)
        if type == event_type.INFO_LOG and self.__settings.settings.log_level <= log_level.INFO.value:
            self.__INFO(params)
        if type == event_type.ERROR_LOG and self.__settings.settings.log_level <= log_level.ERROR.value:
            self.__DEBUG(params)
