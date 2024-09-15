from Src.custom_exceptions import custom_exceptions
from Src.abstract_model import abstract_model
from Src.models.nomenclature_group_model import nomenclature_group_model
from Src.models.range_model import range_model


class nomenclature_model(abstract_model):
    __full_name = ""
    __nomenclature_group = None
    __range = None

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        if not isinstance(value, str):
            raise custom_exceptions().type(value, str)
        if len(value) > 255:
            raise custom_exceptions().length(len(value), 255, ">")
        self.__full_name = value

    @property
    def nomenclature_group(self):
        return self.__nomenclature_group

    @nomenclature_group.setter
    def nomenclature_group(self, value: nomenclature_group_model):
        if not isinstance(value, nomenclature_group_model):
            raise custom_exceptions().type(value, nomenclature_group_model)
        self.__nomenclature_group = value

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value: range_model):
        if not isinstance(value, range_model):
            raise custom_exceptions().type(value, range_model)
        self.__range = value

    def set_compare_mode(self, other, equal: bool = True) -> bool:
        return super().set_compare_mode(other, equal)