from Src.Core.base_models import base_model_name


class range_model(base_model_name):
    __base = None
    __conversion_factor: int = 0

    def __init__(self, name: str, conversion_factor_value: int):
        super().__init__()
        if not isinstance(name, str):
            raise self._custom_exception.type(type(name), str)
        if not isinstance(conversion_factor_value, int):
            raise self._custom_exception.type(type(conversion_factor_value), int)
        self.name = name
        self.conversion_factor = conversion_factor_value

    @property
    def base(self) -> str:
        return self.__base

    @base.setter
    def base(self, value) -> str:
        if not isinstance(value, range_model):
            raise self._custom_exception.type(type(value), range_model)
        self.__base = value

    @property
    def conversion_factor(self) -> int:
        return self.__conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, value: int):
        if not isinstance(value, int):
            raise self._custom_exception.type(type(value), int)
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
