from datetime import datetime

from Src.Core.Abstract_classes.base_models import base_model_name
from Src.Core.custom_exceptions import custom_exceptions
from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model


# Класс складских транзакций
class warehouse_transaction_model(base_model_name):
    __warehouse: warehouse_model = None
    __nomenclature: nomenclature_model = None
    __quantity: int = 0
    __type: bool = 0  # 0 - расход;   1 - приход;
    __range: range_model = None
    __date: datetime = None

    def __init__(self, warehouse: warehouse_model, nomenclature: nomenclature_model,
                 quantity: int, type: bool, range: range_model, date: datetime = datetime.now()):
        super().__init__()
        self.warehouse = warehouse
        self.nomenclature = nomenclature
        self.quantity = quantity
        self.type = type
        self.range = range
        self.period = date

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
        return self.__date

    @period.setter
    def period(self, value: datetime):
        custom_exceptions.type(value, datetime)
        self.__date = value

    @staticmethod
    def parse_JSON(data: dict):
        custom_exceptions.type(data, dict)
        if len(data) == 0:
            return None

        warehouse = warehouse_model.parse_JSON(data["warehouse"])
        nomenclature = nomenclature_model.parse_JSON(data["nomenclature"])
        range = range_model.parse_JSON(data["range"])
        new_transaction = warehouse_transaction_model(warehouse, nomenclature, data["quantity"], data["type"], range,
                                                      datetime.strptime(data["period"], "%d-%m-%Y"))

        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(warehouse_transaction_model, x)),
                             dir(warehouse_transaction_model)))

        for field in fields:
            custom_exceptions.presence_element_in_dict(data, field)
            if field in ["range", "warehouse", "nomenclature", "period"]:
                continue
            new_transaction.__setattr__(field, data[field])
        return new_transaction

    def __str__(self):
        return "warehouse_transaction_model"
