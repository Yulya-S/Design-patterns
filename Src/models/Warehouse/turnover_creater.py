from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.data_reposity import data_reposity
from Src.Core.custom_exceptions import custom_exceptions

from Src.models.Warehouse.turnover_factory import turnover_factory
from Src.models.Warehouse.warehouse_turnover_model import warehouse_turnover_model
from Src.models.Warehouse.turnover_filter_data import turnover_filter_data
from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model
from Src.Core.formats_and_methods.turnover_format import turnover_format

from datetime import datetime


class turnover_creater(abstract_logic):
    __reposity: data_reposity = None

    def __init__(self):
        self.__reposity = data_reposity()

    def create_turnover(self, warehouse: warehouse_model, nomenclature: nomenclature_model,
                        range: range_model, periods: [datetime, datetime],
                        format: turnover_format = turnover_format.SUMM) -> warehouse_turnover_model:
        data = turnover_filter_data(self.__reposity.data[data_reposity.transaction_key()])
        data.preparation_data(warehouse, nomenclature, periods)

        method = turnover_factory.get(format)

        turnover = warehouse_turnover_model()
        turnover.warehouse = warehouse
        turnover.nomenclature = nomenclature
        turnover.range = range
        turnover.turnover = method(data.data)

        return turnover

    def create_turnover_with_JSON(self, filter_data: dict) -> warehouse_turnover_model:
        custom_exceptions.type(filter_data, dict)
        custom_exceptions.elements_not_in_array(["warehouse", "nomenclature", "range", "periods"], filter_data)
        custom_exceptions.elements_not_in_array(["begin", "end"], filter_data["periods"])
        custom_exceptions.None_received(filter_data["warehouse"])
        custom_exceptions.None_received(filter_data["nomenclature"])
        custom_exceptions.None_received(filter_data["range"])

        nomenclature = self.__reposity.data[data_reposity.nomenclature_key()][filter_data["nomenclature"]]
        range = self.__reposity.data[data_reposity.range_key()][filter_data["range"]]
        periods = [datetime.strptime(filter_data["periods"]["begin"], "%d-%m-%Y"),
                   datetime.strptime(filter_data["periods"]["end"], "%d-%m-%Y")]
        warehouse = warehouse_model(filter_data["warehouse"])
        for i in self.__reposity.data[data_reposity.warehouse_key()]:
            if i.address == warehouse.address:
                warehouse = i
                break
        if warehouse not in self.__reposity.data[data_reposity.warehouse_key()]:
            custom_exceptions.other_exception(f"{warehouse} отсутствует в списке складов")

        return self.create_turnover(warehouse, nomenclature, range, periods)

    def set_exception(self, ex: Exception):
        super().set_exception(ex)