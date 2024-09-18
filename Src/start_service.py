from Src.Core.abstract_logic import abstract_logic
from Src.data_reposity import data_reposity
from Src.models.group_model import group_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model
from Src.settings_manager import settings_manager
from Src.settings import settings

"""
Сервис для реализации первого старта приложения
"""


class start_service(abstract_logic):
    __reposity: data_reposity = None
    __settings_manager: settings_manager = None

    def __init__(self, reposity: data_reposity, manager: settings_manager) -> None:
        super().__init__()
        if not isinstance(reposity, data_reposity):
            self._custom_exception.type(type(reposity), data_reposity)
        if not isinstance(manager, settings_manager):
            self._custom_exception.type(type(manager), settings_manager)
        self.__reposity = reposity
        self.__settings_manager = manager

    """
    Текущие настройки
    """

    @property
    def settings(self) -> settings:
        return self.__settings_manager.settings

    """
    Сформировать группы номенклатуры
    """

    def __create_nomenclature_groups(self):
        list = []
        list.append(group_model.default_group_cold())
        list.append(group_model.default_group_source())
        self.__reposity.data[data_reposity.group_key()] = list

    """
    Добавление новой еденицы измерения
    """

    def add_range(self, basic_unit_measurement_name: str, conversion_factor_value: int):
        self.__reposity.data["ranges"].append(range_model(basic_unit_measurement_name, conversion_factor_value))

    """
    Первый старт
    """

    def create(self):
        self.__create_nomenclature_groups()
        self.__reposity.data["nomenclature"] = nomenclature_model()
        self.__reposity.data["ranges"] = list()

    """
    Перегрузка абстрактного метода
    """

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
