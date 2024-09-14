from Src.checks import type_check
from Src.abstract_reference import abstract_reference


class range_model(abstract_reference):
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
        type_check(value, str)
        self.__basic_unit_measurement = value

    @property
    def conversion_factor(self) -> int:
        return self.__conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, value: int):
        type_check(value, int)
        self.__conversion_factor = value