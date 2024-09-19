from Src.Core.base_models import base_model_name


class range_model(base_model_name):
    __basic_unit_measurement: str = ""
    __conversion_factor: int = 0

    def __init__(self, basic_unit_measurement_name: str, conversion_factor_value: int):
        super().__init__()
        if not isinstance(basic_unit_measurement_name, str):
            raise self._custom_exception.type(type(basic_unit_measurement_name), str)
        if not isinstance(conversion_factor_value, int):
            raise self._custom_exception.type(type(conversion_factor_value), int)
        self.basic_unit_measurement = basic_unit_measurement_name
        self.conversion_factor = conversion_factor_value

    @property
    def basic_unit_measurement(self) -> str:
        return self.__basic_unit_measurement

    @basic_unit_measurement.setter
    def basic_unit_measurement(self, value: str):
        if not isinstance(value, str):
            raise self._custom_exception.type(type(value), str)
        self.__basic_unit_measurement = value

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
        return range_model("кг", 1)

    @staticmethod
    def default_range_gr():
        return range_model("гр", 1000)

    @staticmethod
    def default_range_l():
        return range_model("л", 1)

    @staticmethod
    def default_range_ml():
        return range_model("мл", 1000)

    @staticmethod
    def default_range_pcs():
        return range_model("шт", 1)
