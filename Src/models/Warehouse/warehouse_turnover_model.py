from Src.Core.base_models import base_model_name
from Src.Core.comparison_format import comparison_format
from Src.Core.custom_exceptions import custom_exceptions
from Src.logic.nomenclature_prototype import nomenclature_prototype
from Src.Dto.filter import filter_model

from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model
from Src.models.Warehouse.warehouse_model import warehouse_model

from datetime import datetime

# Класс складского оборота
class warehouse_turnover_model(base_model_name):
    __data: list = []
    __warehouse: warehouse_model = None
    __turnover: int = 0
    __nomenclature: nomenclature_model = None
    __range: range_model = None

    def __init__(self, data: list, warehouse: warehouse_model, nomenclature: nomenclature_model, range: range_model):
        super().__init__()
        custom_exceptions.type(data, list)
        custom_exceptions.type(warehouse, warehouse_model)
        custom_exceptions.type(nomenclature, nomenclature_model)
        custom_exceptions.type(range, range_model)
        self.__warehouse = warehouse
        self.__nomenclature = nomenclature
        self.__range = range
        filter = filter_model()
        filter.update_filter("warehouse", comparison_format.EQUAL, self.__warehouse)
        filter.update_filter("nomenclature", comparison_format.EQUAL, self.__nomenclature)
        result = nomenclature_prototype(data)
        result.create(data, filter)
        self.__data = result.data

    def add_period(self, begin_period: datetime, end_period: datetime):
        filter = filter_model()
        filter.update_filter("warehouse", comparison_format.EQUAL, self.__warehouse)
        filter.update_filter("nomenclature", comparison_format.EQUAL, self.__nomenclature)
        result = nomenclature_prototype(self.__data)
        result.create(self.__data, filter)
        self.__data = result.data

    def __str__(self):
        return "warehouse_turnover_model"
