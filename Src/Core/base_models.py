from Src.Core.abstract_model import abstract_model

"""
Базовый класс для наследования с поддержкой сравнения по коду
"""


class base_model_code(abstract_model):
    def set_compare_mode(self, other, equal: bool = True) -> bool:
        return super().set_compare_mode(other, equal)


"""
Базовый класс для наследования с поддержкой сравнения по наименованию
"""


class base_model_name(abstract_model):
    __name: str = ""

    @property
    def name(self) -> str:
        return self.__name.strip()

    @name.setter
    def name(self, value: str):
        self._custom_exception.type(value, str)
        self._custom_exception.length_more(value, 255)
        self.__name = value

    def set_compare_mode(self, other, equal: bool = True) -> bool:
        # если equal = True, то проверяем что значения равны иначе проверяем не равенство
        if other is None or not isinstance(other, abstract_model):
            return not equal

        if equal:
            return self.name == other.name
        return self.name != other.name
