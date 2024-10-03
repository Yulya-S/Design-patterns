from Src.Core.abstract_logic import abstract_logic
from Src.Core.custom_exceptions import custom_exceptions
from Src.data_reposity import data_reposity
from Src.models.group_model import group_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model
from Src.settings_manager import settings_manager
from Src.receipt_book_menager import receipt_book_menager
from Src.settings import settings_model

import os
import json

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
        custom_exceptions.type(reposity, data_reposity)
        custom_exceptions.type(manager, settings_manager)
        custom_exceptions.type(recipe_manager, receipt_book_menager)
        self.__reposity = reposity
        self.__settings_manager = manager
        self.__recipe_manager = recipe_manager

    """
    Текущие настройки
    """

    @property
    def settings(self) -> settings_model:
        return self.__settings_manager.settings

    @property
    def reposity(self):
        return self.__reposity

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

    # Чтение JSON файла
    def __read_JSON(self, json_file: str, path: str = ""):
        custom_exceptions.type(json_file, str)
        custom_exceptions.type(path, str)

        try:
            full_name = f"{path}{os.sep}{json_file}"
            stream = open(full_name)
            data = json.load(stream)
            return data
        except Exception as ex:
            self.set_exception(ex)
            return None

    def group_from_JSON(self, json_file: str, path: str = ""):
        data_json = self.__read_JSON(json_file, path)
        self.__reposity.data[self.__reposity.group_key()] = []

        for i in list(data_json.keys()):
            self.__reposity.data[self.__reposity.group_key()].append(group_model.parse_JSON(data_json[i]))

    def nomenclature_from_JSON(self, json_file: str, path: str = ""):
        data_json = self.__read_JSON(json_file, path)
        self.__reposity.data[self.__reposity.nomenclature_key()] = {}

        for i in list(data_json.keys()):
            value = nomenclature_model.parse_JSON(data_json[i])
            self.__reposity.data[self.__reposity.nomenclature_key()][value.name] = value

    def range_from_JSON(self, json_file: str, path: str = ""):
        data_json = self.__read_JSON(json_file, path)
        self.__reposity.data[self.__reposity.range_key()] = {}

        for i in list(data_json.keys()):
            value = range_model.parse_JSON(data_json[i])
            self.__reposity.data[self.__reposity.range_key()][value.name] = value

    def receipts_from_JSON(self, json_file: str, path: str = ""):
        data_json = self.__read_JSON(json_file, path)
        self.__reposity.data[self.__reposity.receipt_key()] = receipt_book_menager.parse_JSON(data_json)

    """
    Перегрузка абстрактного метода
    """

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
