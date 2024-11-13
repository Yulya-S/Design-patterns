from Src.Core.custom_exceptions import custom_exceptions
from Src.Dto.filter import filter_model

from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.nomenclature_model import nomenclature_model
from Src.Core.formats_and_methods.comparison_format import comparison_format
from Src.logic.nomenclature_prototype import nomenclature_prototype

from datetime import datetime


# Обработка фильтров для оборотов
class turnover_filter_data:
    __data: list = []

    def __init__(self, data: list):
        custom_exceptions.type(data, list)
        self.__data = data

    @property
    def data(self):
        return self.__data

    # подготовка данных
    def preparation_data(self, warehouse: warehouse_model, nomenclature: nomenclature_model,
                         periods: [datetime, datetime]):
        filter = self.__create_filter(warehouse, nomenclature, periods)
        prototype = nomenclature_prototype(self.__data)
        result = prototype.create(self.__data, filter)
        self.__data = result.data

    #  создание фильтра
    def __create_filter(self, warehouse: warehouse_model, nomenclature: nomenclature_model,
                        periods: [datetime, datetime]) -> filter_model:
        filter = filter_model()
        filter.update_filter("warehouse", comparison_format.EQUAL, warehouse)
        filter.update_filter("nomenclature", comparison_format.EQUAL, nomenclature)
        filter.set_periods(periods[0], periods[1])
        return filter
