import random
import string
from abc import ABC, abstractmethod
from Src.Core.custom_exceptions import custom_exceptions


class abstract_model(ABC):
    __name: str = ""
    __unique_code: str = ""
    _custom_exception: custom_exceptions = custom_exceptions()

    def __init__(self):
        self.__unique_code = ''.join(random.sample((string.ascii_letters + string.digits), 15))

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self._custom_exception.type(value, str)
        self._custom_exception.length_more(value, 50)
        self.__name = value

    @property
    def unique_code(self) -> str:
        return self.__unique_code

    @abstractmethod
    def set_compare_mode(self, other, equal: bool = True) -> bool:
        # если equal = True, то проверяем что значения равны иначе проверяем не равенство
        if other is None or not isinstance(other, abstract_model):
            return not equal

        if equal:
            return self.unique_code == other.unique_code
        return self.unique_code != other.unique_code

    def __eq__(self, other):
        return self.set_compare_mode(other, True)

    def __ne__(self, other):
        return self.set_compare_mode(other, False)
