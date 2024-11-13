from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.event_type import event_type

from Src.models.group_model import group_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model
from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.Warehouse.warehouse_transaction_model import warehouse_transaction_model

from Src.settings_manager import settings_manager
from Src.receipt_book_menager import receipt_book_menager
from Src.settings import settings_model
from Src.data_reposity import data_reposity
from Src.data_reposity_menager import data_reposity_menager
from Src.logic.observe_service import observe_service

from random import randrange
from datetime import datetime, timedelta


# Сервис для реализации первого старта приложения
class start_service(abstract_logic):
    __reposity: data_reposity = None
    __settings_manager: settings_manager = None
    __receipt_manager: receipt_book_menager = None

    def __init__(self, path: str = "", file_name: str = "") -> None:
        super().__init__()
        self.__reposity = data_reposity()
        self.__settings_manager = settings_manager()
        self.__settings_manager.open(path, file_name)
        self.__recipe_manager = receipt_book_menager()
        observe_service.append(self)
        if self.__settings_manager.settings.generate_data:
            self.create()

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

    def __create_warehouse(self):
        self.__reposity.data[data_reposity.warehouse_key()] = [warehouse_model("Ул. N, дом. 1")]

    def __create_transactions(self):
        list = []
        for i in range(3):
            list.append(self.generate_transaction(self.__reposity.data[data_reposity.warehouse_key()][0],
                                                  self.__reposity.data[data_reposity.nomenclature_key()][
                                                      range_model.default_range_gr().name],
                                                  2 + i, True,
                                                  self.__reposity.data[data_reposity.range_key()][
                                                      range_model.default_range_kg().name]))
        for i in range(3):
            list.append(self.generate_transaction(self.__reposity.data[data_reposity.warehouse_key()][0],
                                                  self.__reposity.data[data_reposity.nomenclature_key()][
                                                      range_model.default_range_gr().name],
                                                  i, False,
                                                  self.__reposity.data[data_reposity.range_key()][
                                                      range_model.default_range_kg().name]))
        self.__reposity.data[data_reposity.transaction_key()] = list

    # Первый старт
    def create(self, path: str = ""):
        custom_exceptions.type(path, str)
        self.__create_nomenclature_groups()
        self.__create_ranges()
        self.__create_nomenclatures()
        self.__create_warehouse()
        self.__create_transactions()
        if path == ".":
            path += "\\Docs"
        self.__reposity.data[data_reposity.receipt_key()] = self.__recipe_manager.open(path)

    # Генерация транзакции
    def generate_transaction(self, warehouse: warehouse_model, nomenclature: nomenclature_model,
                             quantity: int, type: bool, range: range_model, date: datetime = datetime.now()):
        custom_exceptions.type(date, datetime)

        if data_reposity.transaction_key() not in list(self.__reposity.data.keys()):
            self.__reposity.data[data_reposity.transaction_key()] = []
        if data_reposity.warehouse_key() not in list(self.__reposity.data.keys()):
            self.__reposity.data[data_reposity.warehouse_key()] = []
        if warehouse not in self.__reposity.data[data_reposity.warehouse_key()]:
            self.__reposity.data[data_reposity.warehouse_key()].append(warehouse)

        transaction = warehouse_transaction_model(warehouse, nomenclature, quantity, type, range, date)
        self.__reposity.data[data_reposity.transaction_key()].append(transaction)
        return transaction

    # генерация введенного количества транзакций
    def generate_n_transactions(self, transaction_count: int, last_date: datetime = datetime.now()):
        custom_exceptions.type(transaction_count, int)
        custom_exceptions.type(last_date, datetime)

        list = []
        warehouse = self.__reposity.data[data_reposity.warehouse_key()][0]
        nomenclature = self.__reposity.data[data_reposity.nomenclature_key()][range_model.default_range_gr().name]
        r = self.__reposity.data[data_reposity.range_key()][range_model.default_range_kg().name]
        for i in range(transaction_count):
            value = int(randrange(2, 100))
            operation = bool(randrange(2))
            date = last_date - timedelta(days=i)
            list.append(self.generate_transaction(warehouse, nomenclature, value, operation, r, date))
        self.__reposity.data[data_reposity.transaction_key()] = list

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)

    def handle_event(self, type: event_type, params):
        super().handle_event(type, params)
        if type == event_type.CHANGE_NOMENCLATURE:
            data_reposity_menager.change_nomenclature(nomenclature_model.parse_from_str(params))
