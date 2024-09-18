from Src.Core.base_models import base_model_code
from Src.models.group_model import group_model
from Src.models.range_model import range_model


class nomenclature_model(base_model_code):
    __full_name = ""
    __group = None
    __range = None

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        if not isinstance(value, str):
            raise self.custom_exception.type(type(value), str)
        if len(value) > 255:
            raise self.custom_exception.length(len(value), 255, ">")
        self.__full_name = value

    @property
    def nomenclature_group(self):
        return self.__group

    @nomenclature_group.setter
    def nomenclature_group(self, value: group_model):
        if not isinstance(value, group_model):
            raise self.custom_exception.type(type(value), group_model)
        self.__group = value

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value: range_model):
        if not isinstance(value, range_model):
            raise self.custom_exception.type(type(value), range_model)
        self.__range = value
