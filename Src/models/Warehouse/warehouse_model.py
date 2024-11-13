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

    @staticmethod
    def parse_JSON(data: dict):
        custom_exceptions.type(data, dict)
        new_warehouse = warehouse_model("")
        if len(data) == 0:
            return None

        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(warehouse_model, x)),
                             dir(warehouse_model)))

        for field in fields:
            custom_exceptions.presence_element_in_dict(data, field)
            new_warehouse.__setattr__(field, data[field])
        return new_warehouse

    def __str__(self):
        return "warehouse_model"
