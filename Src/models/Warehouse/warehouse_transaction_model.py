from datetime import datetime

from Src.Core.base_models import base_model_name
from Src.Core.custom_exceptions import custom_exceptions
from Src.models.Warehouse import warehouse_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model


# Класс складских транзакций
class warehouse_transaction_model(base_model_name):
    __warehouse: warehouse_model = None
    __nomenclature: nomenclature_model = None
    __quantity: int = 0
    __type: bool = 0  # 0 - расход;   1 - приход;
    __range: range_model = None
    __period: datetime = None

    def __init__(self, warehouse: warehouse_model, nomenclature: nomenclature_model,
                 quantity: int, type: bool, range: range_model):
        super().__init__()
        self.warehouse = warehouse
        self.nomenclature = nomenclature
        self.quantity = quantity
        self.type = type
        self.range = range
        self.period = datetime.now()

    @property
    def warehouse(self):
        return self.__warehouse

    @warehouse.setter
    def warehouse(self, value: warehouse_model):
        custom_exceptions.type(value, warehouse_model)
        self.__warehouse = value

    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        custom_exceptions.type(value, nomenclature_model)
        self.__nomenclature = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        custom_exceptions.type(value, int)
        self.__quantity = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value: bool):
        custom_exceptions.type(value, bool)
        self.__type = value

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value: range_model):
        custom_exceptions.type(value, range_model)
        self.__range = value

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, value: datetime):
        custom_exceptions.type(value, datetime)
        self.__period = value

    def __str__(self):
        return "warehouse_transaction_model"
