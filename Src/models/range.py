from Src.checks import type_check
from Src.abstract_model import abstract_model


class range(abstract_model):
    __name = ""

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        type_check(value, str)
        self.__name = value

    def __eq__(self, other) -> bool:
        if other is None or not isinstance(other, range):
            return False
        return self.name == other.name

    def __ne__(self, other) -> bool:
        if other is None or not isinstance(other, range):
            return True
        return self.name != other.name
