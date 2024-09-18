from Src.Core.base_models import base_model_name
from Src.models.range_model import range_model


# Класс продукта
class product_model(base_model_name):
    __count_in_warehouse: int = 0
    __range_model: range_model = None

    def __init__(self, name: str, range: range_model):
        super().__init__()
        if not isinstance(name, str):
            raise self._custom_exception.type(type(name), str)
        if not isinstance(range, range_model):
            raise self._custom_exception.type(type(range), range_model)
        self.name = name
        self.__range_model = range

    # Количество на складе
    @property
    def count_in_warehouse(self):
        return self.__count_in_warehouse

    # Добавить продукт в определенном количестве
    def add_quantity(self, quantity: int):
        if not isinstance(quantity, int):
            raise self._custom_exception.type(type(quantity), int)
        self.__count_in_warehouse += quantity

    # Убрать продукт в определенном количестве
    def remove_quantity(self, quantity: int):
        if not isinstance(quantity, int):
            raise self._custom_exception.type(type(quantity), int)
        if self.__count_in_warehouse < quantity:
            return False
        self.__count_in_warehouse -= quantity
        return True
