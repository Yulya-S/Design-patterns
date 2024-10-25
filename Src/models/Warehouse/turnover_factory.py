from Src.models.Warehouse.warehouse_turnover_model import warehouse_turnover_model
from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model
from Src.data_reposity import data_reposity
from datetime import datetime


class turnover_factory:
    @staticmethod
    def create_turnover(warehouse: warehouse_model, nomenclature: nomenclature_model, range: range_model,
                        periods: [datetime, datetime] = [None, None]):
        reposity = data_reposity()
        turnover = warehouse_turnover_model(reposity.data[data_reposity.transaction_key()], warehouse,
                                            nomenclature, range)
        if None not in periods:
            turnover.add_period(periods[0], periods[1])

        for i in turnover.data:
            turnover.update_turnover(i.type, i.quantity)

        return turnover