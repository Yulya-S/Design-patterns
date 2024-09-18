from Src.Core.abstract_logic import abstract_logic
from Src.data_reposity import data_reposity
from Src.models.group_model import group_model
from Src.models.nomenclature_model import nomenclature_model
from Src.settings_manager import settings_manager
from Src.receipt_book_menager import receipt_book_menager
from Src.settings import settings

"""
Сервис для реализации первого старта приложения
"""


class start_service(abstract_logic):
    __reposity: data_reposity = None
    __settings_manager: settings_manager = None
    __recipe_book: receipt_book_menager = None

    def __init__(self, reposity: data_reposity, manager: settings_manager, recipe_book: receipt_book_menager) -> None:
        super().__init__()
        if not isinstance(reposity, data_reposity):
            self._custom_exception.type(type(reposity), data_reposity)
        if not isinstance(manager, settings_manager):
            self._custom_exception.type(type(manager), settings_manager)
        if not isinstance(recipe_book, receipt_book_menager):
            self._custom_exception.type(type(recipe_book), receipt_book_menager)
        self.__reposity = reposity
        self.__settings_manager = manager
        self.__recipe_book = recipe_book

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
    Первый старт
    """

    def create(self):
        self.__create_nomenclature_groups()
        self.__reposity.data["nomenclature"] = nomenclature_model()

    """
    Перегрузка абстрактного метода
    """

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
