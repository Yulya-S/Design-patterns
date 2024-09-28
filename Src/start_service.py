from Src.Core.abstract_logic import abstract_logic
from Src.data_reposity import data_reposity
from Src.models.group_model import group_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model
from Src.settings_manager import settings_manager
from Src.receipt_book_menager import receipt_book_menager
from Src.settings import settings_model

"""
Сервис для реализации первого старта приложения
"""


class start_service(abstract_logic):
    __reposity: data_reposity = None
    __settings_manager: settings_manager = None
    __receipt_manager: receipt_book_menager = None

    def __init__(self, reposity: data_reposity, manager: settings_manager,
                 recipe_manager: receipt_book_menager) -> None:
        super().__init__()
        self._custom_exception.type(reposity, data_reposity)
        self._custom_exception.type(manager, settings_manager)
        self._custom_exception.type(recipe_manager, receipt_book_menager)
        self.__reposity = reposity
        self.__settings_manager = manager
        self.__recipe_manager = recipe_manager

    """
    Текущие настройки
    """

    @property
    def settings(self) -> settings_model:
        return self.__settings_manager.settings

    """
    Сформировать группы номенклатуры
    """

    def __create_nomenclature_groups(self):
        list = []
        list.append(group_model.default_group_cold())
        list.append(group_model.default_group_source())
        self.__reposity.data[data_reposity.group_key()] = list

    def __create_nomenclatures(self):
        dict = {}
        dict[range_model.default_range_gr().name] = nomenclature_model.default_source_gr()
        dict[range_model.default_range_ml().name] = nomenclature_model.default_source_ml()
        dict[range_model.default_range_pcs().name] = nomenclature_model.default_source_pcs()
        self.__reposity.data[data_reposity.nomenclature_key()] = dict

    def __create_ranges(self):
        dict = {}
        dict[range_model.default_range_kg().name] = range_model.default_range_kg()
        dict[range_model.default_range_gr().name] = range_model.default_range_gr()
        dict[range_model.default_range_l().name] = range_model.default_range_l()
        dict[range_model.default_range_ml().name] = range_model.default_range_ml()
        dict[range_model.default_range_pcs().name] = range_model.default_range_pcs()
        self.__reposity.data[data_reposity.range_key()] = dict

    """
    Первый старт
    """

    def create(self):
        self.__create_nomenclature_groups()
        self.__create_ranges()
        self.__create_nomenclatures()
        self.__reposity.data[data_reposity.receipt_key()] = self.__recipe_manager.open()

    """
    Перегрузка абстрактного метода
    """

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
