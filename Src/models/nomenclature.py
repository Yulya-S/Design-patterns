from Src.checks import type_check
from Src.abstract_model import abstract_model


class nomenclature(abstract_model):
    __name = ""

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        type_check(value, str)
        self.__name = value

    def _equal(self, other) -> bool:
        if other is None or not isinstance(other, nomenclature):
            return False
        return self.unique_code == other.unique_code

    def _noequal(self, other) -> bool:
        if other is None or not isinstance(other, nomenclature):
            return True
        return self.unique_code != other.unique_code

    def __eq__(self, other) -> bool:
        return self._equal(other)

    def __ne__(self, other) -> bool:
        return self._noequal(other)
