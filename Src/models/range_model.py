from Src.Core.base_models import base_model_name


class range_model(base_model_name):
    __basic_unit_measurement = ""
    __conversion_factor = 0

    def __init__(self, basic_unit_measurement_name: str, conversion_factor_value: int):
        self.basic_unit_measurement = basic_unit_measurement_name
        self.conversion_factor = conversion_factor_value

    @property
    def basic_unit_measurement(self) -> str:
        return self.__basic_unit_measurement

    @basic_unit_measurement.setter
    def basic_unit_measurement(self, value: str):
        if not isinstance(value, str):
            raise self.custom_exception.type(type(value), str)
        self.__basic_unit_measurement = value

    @property
    def conversion_factor(self) -> int:
        return self.__conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, value: int):
        if not isinstance(value, int):
            raise self.custom_exception.type(type(value), int)
        self.__conversion_factor = value
