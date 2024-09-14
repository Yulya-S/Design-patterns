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

    def __eq__(self, other) -> bool:
        return self._equal(other)

    def __ne__(self, other) -> bool:
        return self._noequal(other)
