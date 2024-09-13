from Src.checks import type_check, value_check
from Src.abstract_reference import abstract_reference
from Src.models.nomenclature_group_model import nomenclature_group_model
from Src.models.range_model import range_model


class nomenclature_model(abstract_reference):
    __full_name = ""
    __nomenclature_group = None
    __range = None

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        type_check(value, str)
        value_check(len(value) < 255)
        self.__full_name = value

    @property
    def nomenclature_group(self):
        return self.__nomenclature_group

    @nomenclature_group.setter
    def nomenclature_group(self, value: nomenclature_group_model):
        type_check(value, nomenclature_group_model)
        self.__nomenclature_group = value

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value: range_model):
        type_check(value, range_model)
        self.__range = value
