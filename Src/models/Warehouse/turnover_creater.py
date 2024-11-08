from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.Core.formats_and_methods.turnover_format import turnover_format
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.event_type import event_type

from Src.data_reposity import data_reposity
from Src.settings_manager import settings_manager

from Src.models.Warehouse.turnover_factory import turnover_factory
from Src.models.Warehouse.warehouse_turnover_model import warehouse_turnover_model
from Src.models.Warehouse.turnover_filter_data import turnover_filter_data
from Src.models.Warehouse.warehouse_model import warehouse_model

from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model

from datetime import datetime


# Создание оборотов из данных о транзакциях
class turnover_creater(abstract_logic):
    @staticmethod
    def create(warehouse: warehouse_model, nomenclature: nomenclature_model, range: range_model,
               periods: [datetime, datetime], data: list = [], format: turnover_format = turnover_format.SUMM):
        custom_exceptions.type(data, list)
        reposity = data_reposity()

        if len(data) > 0:
            data = turnover_filter_data(data.copy())
        else:
            data = turnover_filter_data(reposity.data[data_reposity.transaction_key()])
        data.preparation_data(warehouse, nomenclature, periods)
        method = turnover_factory.get(format)
        turnover = warehouse_turnover_model()
        turnover.warehouse = warehouse
        turnover.nomenclature = nomenclature
        turnover.range = range
        turnover.data = data.data
        turnover.turnover = method(data.data)
        return turnover

    @staticmethod
    def create_with_block_period(warehouse: warehouse_model, nomenclature: nomenclature_model, range: range_model,
                                 turnover_data: list = [], turnover_format=turnover_format.SUMM):
        s_m = settings_manager()
        block_period = s_m.settings.block_period
        return turnover_creater.create(warehouse, nomenclature, range,
                                       [datetime.strptime("01-01-1900", "%d-%m-%Y"), block_period],
                                       turnover_data, turnover_format)

    def set_exception(self, ex: Exception):
        super().set_exception(ex)

    def handle_event(self, type: event_type, params):
        super().handle_event(type, params)
