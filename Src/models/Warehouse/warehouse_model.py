from Src.Core.Abstract_classes.base_models import base_model_name
from Src.Core.custom_exceptions import custom_exceptions


# Класс склада
class warehouse_model(base_model_name):
    __address: str = ""

    def __init__(self, address: str):
        super().__init__()
        custom_exceptions.type(address, str)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        custom_exceptions.type(value, str)
        self.__address = value

    def __str__(self):
        return "warehouse_model"
