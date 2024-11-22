from Src.Core.Abstract_classes.abstract_model import abstract_model
from Src.Core.custom_exceptions import custom_exceptions


# Базовый класс для наследования с поддержкой сравнения по коду
class base_model_code(abstract_model):
    def set_compare_mode(self, other, equal: bool = True) -> bool:
        return super().set_compare_mode(other, equal)

    @staticmethod
    def parse_JSON(data: dict):
        pass

    def create_JSON(self):
        dict = {}
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(self.__class__, x)),
                             dir(self)))
        for i in fields:
            value = self.__getattribute__(i)
            if issubclass(type(value), base_model_name) or issubclass(type(value), base_model_code):
                value = value.create_JSON()
            dict[i] = value
        return dict

    def change_value_if_equal(self, value: any):
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(self, x)),
                             dir(self)))

        for field in fields:
            if type(self.__getattribute__(field)) == type(value) and self.__getattribute__(
                    field).unique_code == value.unique_code:
                self.__setattr__(field, value)
            elif issubclass(type(field), base_model_name) or issubclass(type(field), base_model_code):
                self.__getattribute__(field).change_value_if_equal(value)


# Базовый класс для наследования с поддержкой сравнения по наименованию
class base_model_name(abstract_model):
    __name: str = ""

    @property
    def name(self) -> str:
        return self.__name.strip()

    @name.setter
    def name(self, value: str):
        custom_exceptions.type(value, str)
        custom_exceptions.length_more(value, 255)
        self.__name = value

    def set_compare_mode(self, other, equal: bool = True) -> bool:
        # если equal = True, то проверяем что значения равны иначе проверяем не равенство
        if other is None or not isinstance(other, abstract_model):
            return not equal

        if equal:
            return self.name == other.name
        return self.name != other.name

    @staticmethod
    def parse_JSON(data: dict):
        pass

    def create_JSON(self):
        dict = {}
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(self.__class__, x)),
                             dir(self)))
        for i in fields:
            value = self.__getattribute__(i)
            if issubclass(type(value), base_model_name) or issubclass(type(value), base_model_code):
                value = value.create_JSON()
            dict[i] = value
        return dict

    def change_value_if_equal(self, value: any):
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(self, x)),
                             dir(self)))

        for field in fields:
            if type(self.__getattribute__(field)) == type(value) and self.__getattribute__(
                    field).unique_code == value.unique_code:
                self.__setattr__(field, value)
            elif issubclass(type(field), base_model_name) or issubclass(type(field), base_model_code):
                self.__getattribute__(field).change_value_if_equal(value)
