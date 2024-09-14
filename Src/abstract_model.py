import random
import string
from abc import ABC, abstractmethod


class abstract_model(ABC):
    __name = ""
    __unique_code: str = ""

    def __init__(self):
        self.__unique_code = ''.join(random.sample((string.ascii_letters + string.digits), 15))

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def unique_code(self) -> str:
        return self.__unique_code

    def _equal(self, other) -> bool:
        if other is None or not isinstance(other, abstract_model):
            return False
        return self.unique_code == other.unique_code

    @abstractmethod
    def __eq__(self, other):
        return self._equal(other)

    def _noequal(self, other) -> bool:
        if other is None or not isinstance(other, abstract_model):
            return True
        return self.unique_code != other.unique_code

    @abstractmethod
    def __ne__(self, other):
        return self._noequal(other)
