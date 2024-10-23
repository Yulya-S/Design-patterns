from Src.Core.base_models import base_model_name
from Src.Core.custom_exceptions import custom_exceptions


# Класс склада
class warehouse_model(base_model_name):
    __address: str = ""

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        custom_exceptions.type(value, str)
        self.__address = value

    @staticmethod
    def create(address: str):
        warehouse = warehouse_model()
        warehouse.address = address
        return warehouse

    def __str__(self):
        return "warehouse_model"
