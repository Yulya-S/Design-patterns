from Src.checks import value_check

import random
import string
from abc import ABC, abstractmethod


class abstract_reference(ABC):
    __name: str = ""

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        value_check(len(value) < 50)
        self.__name = value
