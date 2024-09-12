from Src.abstract_reference import abstract_reference


class range(abstract_reference):
    __name = ""
    __basic_unit_measurement = ""
    __conversion_factor = 0

    def __init__(self, basic_unit_measurement: str, conversion_factor: int):
        self.basic_unit_measurement(basic_unit_measurement)
        self.conversion_factor(conversion_factor)

    @property
    def basic_unit_measurement(self) -> str:
        return self.__basic_unit_measurement

    @basic_unit_measurement.setter
    def basic_unit_measurement(self, text: str):
        self.__basic_unit_measurement = text

    @property
    def conversion_factor(self) -> int:
        return self.__conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, value: int):
        self.__conversion_factor = value




    def _equal(self, other) -> bool:
        if other is None or not isinstance(other, range):
            return False
        return self.name == other.name

    def _noequal(self, other) -> bool:
        if other is None or not isinstance(other, range):
            return True
        return self.name != other.name

    def __eq__(self, other) -> bool:
        return self._equal(other)

    def __ne__(self, other) -> bool:
        return self._noequal(other)