from Src.custom_exceptions import custom_exceptions
from Src.abstract_model import abstract_model


class range_model(abstract_model):
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
            raise custom_exceptions().type(value, str)
        self.__basic_unit_measurement = value

    @property
    def conversion_factor(self) -> int:
        return self.__conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, value: int):
        if not isinstance(value, int):
            raise custom_exceptions().type(value, int)
        self.__conversion_factor = value

    def __eq__(self, other) -> bool:
        if other is None or not isinstance(other, range_model):
            return False
        return self.name == other.name

    def __ne__(self, other) -> bool:
        if other is None or not isinstance(other, range_model):
            return True
        return self.name != other.name
