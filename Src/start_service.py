from Src.Core.abstract_logic import abstract_logic
from Src.Core.custom_exceptions import custom_exceptions

from Src.models.group_model import group_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model
from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.Warehouse.warehouse_transaction_model import warehouse_transaction_model

from Src.settings_manager import settings_manager
from Src.receipt_book_menager import receipt_book_menager
from Src.settings import settings_model
from Src.data_reposity import data_reposity


# Сервис для реализации первого старта приложения
class start_service(abstract_logic):
    __reposity: data_reposity = None
    __settings_manager: settings_manager = None
    __receipt_manager: receipt_book_menager = None

    def __init__(self) -> None:
        super().__init__()
        self.__reposity = data_reposity()
        self.__settings_manager = settings_manager()
        self.__recipe_manager = receipt_book_menager()

    # Текущие настройки
    @property
    def settings(self) -> settings_model:
        return self.__settings_manager.settings

    @property
    def reposity(self):
        return self.__reposity

    # Формирование данных
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

    # Первый старт
    def create(self, path: str = ""):
        custom_exceptions.type(path, str)
        self.__create_nomenclature_groups()
        self.__create_ranges()
        self.__create_nomenclatures()
        if path == ".":
            path += "\\Docs"
        self.__reposity.data[data_reposity.receipt_key()] = self.__recipe_manager.open(path)

    # Генерация транзакции
    def generate_transaction(self, warehouse: warehouse_model, nomenclature: nomenclature_model,
                             quantity: int, type: bool, range: range_model):
        if data_reposity.transaction_key() not in list(self.__reposity.data.keys()):
            self.__reposity.data[data_reposity.transaction_key()] = []
        if data_reposity.warehouse_key() not in list(self.__reposity.data.keys()):
            self.__reposity.data[data_reposity.warehouse_key()] = []
        if warehouse not in self.__reposity.data[data_reposity.warehouse_key()]:
            self.__reposity.data[data_reposity.warehouse_key()].append(warehouse)

        self.__reposity.data[data_reposity.transaction_key()].append(warehouse_transaction_model(
            warehouse, nomenclature, quantity, type, range
        ))

    # Перегрузка абстрактного метода
    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
