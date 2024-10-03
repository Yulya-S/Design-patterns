from Src.Core.base_models import base_model_name
from Src.Core.custom_exceptions import custom_exceptions


class range_model(base_model_name):
    __base = None
    __conversion_factor: int = 0

    def __init__(self, name: str, conversion_factor_value: int):
        super().__init__()
        custom_exceptions.type(name, str)
        custom_exceptions.type(conversion_factor_value, int)
        self.name = name
        self.conversion_factor = conversion_factor_value

    @property
    def base(self) -> str:
        return self.__base

    @base.setter
    def base(self, value) -> str:
        custom_exceptions.type(value, range_model)
        self.__base = value

    @property
    def conversion_factor(self) -> int:
        return self.__conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, value: int):
        custom_exceptions.type(value, int)
        self.__conversion_factor = value

    @staticmethod
    def default_range_kg():
        item = range_model("кг", 1)
        item.base = range_model.default_range_gr()
        return item

    @staticmethod
    def default_range_gr():
        return range_model("гр", 1000)

    @staticmethod
    def default_range_l():
        item = range_model("л", 1)
        item.base = range_model.default_range_ml()
        return item

    @staticmethod
    def default_range_ml():
        return range_model("мл", 1000)

    @staticmethod
    def default_range_pcs():
        return range_model("шт", 1)

    def __str__(self):
        return "range_model"

    # Парсинг JSON файла
    @staticmethod
    def parse_JSON(data: dict):
        custom_exceptions.type(data, dict)

        new_nomenclature = range_model(data["name"], int(data["conversion_factor"]))
        if data["base"] is not None:
            new_nomenclature.base = range_model.parse_JSON(data["base"])
        new_nomenclature.unique_code = data["unique_code"]

        return new_nomenclature
