from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.event_type import event_type

from Src.Dto.filter import filter_model
from Src.data_reposity import data_reposity
from Src.Core.formats_and_methods.comparison_format import comparison_format
from Src.models.Warehouse.warehouse_model import warehouse_model

from datetime import datetime


# Заполнение фильтра из Json
class filter_json_deserialization(abstract_logic):
    __filter: filter_model = None
    __reposity: data_reposity = None

    @property
    def result(self):
        return self.__filter

    # Заполнение данных фильтрации из словаря
    def read_data(self, data: dict):
        custom_exceptions.type(data, dict)
        self.__filter = filter_model()
        self.__reposity = data_reposity()

        for i in list(data.keys()):
            getattr(filter_json_deserialization, f"_filter_json_deserialization__{i}")(self, data[i])

    def __name(self, data: dict):
        custom_exceptions.elements_not_in_array(["comparison_format", "value"], data)
        self.__filter.update_filter("name", comparison_format(data["comparison_format"]), data["value"])

    def __id(self, data: dict):
        custom_exceptions.elements_not_in_array(["comparison_format", "value"], data)
        self.__filter.update_filter("id", comparison_format(data["comparison_format"]), data["value"])

    def __warehouse(self, data: dict):
        custom_exceptions.elements_not_in_array(["comparison_format", "value"], data)
        if data["value"] not in ["", None]:
            value = warehouse_model(data["value"])
            for i in self.__reposity.data[data_reposity.warehouse_key()]:
                if value.address == i.address:
                    value = i
                    break
            if value not in self.__reposity.data[data_reposity.warehouse_key()]:
                custom_exceptions.other_exception(f"{value} отсутствует в списке складов")
        else:
            value = data["value"]

        self.__filter.update_filter("warehouse", comparison_format(data["comparison_format"]), value)

    def __nomenclature(self, data: dict):
        custom_exceptions.elements_not_in_array(["comparison_format", "value"], data)
        if data["value"] not in ["", None]:
            if data["value"] not in list(self.__reposity.data[data_reposity.nomenclature_key()].keys()):
                custom_exceptions.other_exception(f"{data['value']} отсутствует в списке номенклатур")
            value = self.__reposity.data[data_reposity.nomenclature_key()][data["value"]]
        else:
            value = data["value"]
        self.__filter.update_filter("nomenclature", comparison_format(data["comparison_format"]), value)

    def __periods(self, data: dict):
        custom_exceptions.elements_not_in_array(["begin", "end"], data)
        periods = [datetime.strptime(data["begin"], "%d-%m-%Y"), datetime.strptime(data["end"], "%d-%m-%Y")]
        self.__filter.set_periods(periods[0], periods[1])

    def set_exception(self, ex: Exception):
        super().set_exception(ex)

    def handle_event(self, type: event_type, params):
        super().handle_event(type, params)
