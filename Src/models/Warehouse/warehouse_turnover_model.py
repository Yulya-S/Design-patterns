from Src.Core.Abstract_classes.base_models import base_model_name
from Src.Core.formats_and_methods.comparison_format import comparison_format
from Src.Core.custom_exceptions import custom_exceptions
from Src.logic.nomenclature_prototype import nomenclature_prototype
from Src.Dto.filter import filter_model

from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model
from Src.models.Warehouse.warehouse_model import warehouse_model

from datetime import datetime


# Класс складского оборота
class warehouse_turnover_model(base_model_name):
    __warehouse: warehouse_model = None
    __turnover: int = 0
    __nomenclature: nomenclature_model = None
    __range: range_model = None

    @property
    def warehouse(self):
        return self.__warehouse

    @warehouse.setter
    def warehouse(self, value: warehouse_model):
        custom_exceptions.type(value, warehouse_model)
        self.__warehouse = value

    @property
    def turnover(self):
        return self.__turnover

    @turnover.setter
    def turnover(self, value: int):
        custom_exceptions.type(value, int)
        self.__turnover = value

    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        custom_exceptions.type(value, nomenclature_model)
        self.__nomenclature = value

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value: range_model):
        custom_exceptions.type(value, range_model)
        self.__range = value

    def __str__(self):
        return "warehouse_turnover_model"
