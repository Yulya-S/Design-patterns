from Src.Core.custom_exceptions import custom_exceptions

from Src.data_reposity import data_reposity

from Src.models.Warehouse.turnover_creater import turnover_creater
from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.Warehouse.warehouse_turnover_model import warehouse_turnover_model

from datetime import datetime


# Создание оборотов из данных о транзакциях
class turnover_creater_manager(turnover_creater):
    @staticmethod
    def create_turnover_with_JSON(filter_data: dict) -> warehouse_turnover_model:
        reposity = data_reposity()

        custom_exceptions.type(filter_data, dict)
        custom_exceptions.elements_not_in_array(["warehouse", "nomenclature", "range", "periods"], filter_data)
        custom_exceptions.elements_not_in_array(["begin", "end"], filter_data["periods"])
        custom_exceptions.None_received(filter_data["warehouse"])
        custom_exceptions.None_received(filter_data["nomenclature"])
        custom_exceptions.None_received(filter_data["range"])

        nomenclature = reposity.data[data_reposity.nomenclature_key()][filter_data["nomenclature"]]
        range = reposity.data[data_reposity.range_key()][filter_data["range"]]
        periods = [datetime.strptime(filter_data["periods"]["begin"], "%d-%m-%Y"),
                   datetime.strptime(filter_data["periods"]["end"], "%d-%m-%Y")]
        warehouse = warehouse_model(filter_data["warehouse"])
        for i in reposity.data[data_reposity.warehouse_key()]:
            if i.address == warehouse.address:
                warehouse = i
                break
        if warehouse not in reposity.data[data_reposity.warehouse_key()]:
            custom_exceptions.other_exception(f"{warehouse} отсутствует в списке складов")

        return turnover_creater.create(warehouse, nomenclature, range, periods)
