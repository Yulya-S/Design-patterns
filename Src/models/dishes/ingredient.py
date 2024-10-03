from Src.Core.base_models import base_model_name
from Src.models.nomenclature_model import nomenclature_model
from Src.Core.custom_exceptions import custom_exceptions


# Класс ингредиента
class ingredient_model(base_model_name):
    __nomenclature: nomenclature_model = None
    __quantity: int = 0

    def __init__(self, name: str, nomenclature: nomenclature_model, quantity: int):
        super().__init__()
        custom_exceptions.type(name, str)
        custom_exceptions.type(nomenclature, nomenclature_model)
        custom_exceptions.type(quantity, int)
        self.name = name
        self.__nomenclature = nomenclature
        self.__quantity = quantity

    # Единица измерения
    @property
    def range_model(self):
        return self.__nomenclature

    @range_model.setter
    def range_model(self, value: nomenclature_model):
        custom_exceptions.type(value, nomenclature_model)
        self.__nomenclature = value

    # Необходимое количество ингредиента
    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        custom_exceptions.type(value, int)
        self.__quantity = value

    def __str__(self):
        return "ingredient"

    # Парсинг JSON файла
    @staticmethod
    def parse_JSON(data: dict):
        custom_exceptions.type(data, dict)
        if len(data) == 0:
            return None

        new_ingredient = ingredient_model(data["name"], nomenclature_model.parse_JSON(data["range_model"]),
                                          data["quantity"])
        return new_ingredient

