from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.event_type import event_type

from Src.models.group_model import group_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.range_model import range_model
from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.Warehouse.warehouse_transaction_model import warehouse_transaction_model
from Src.receipt_book_menager import receipt_book_menager

import os
import json


# класс десереализации JSON
class json_deserialization(abstract_logic):
    __result: dict | list = None

    @property
    def result(self):
        return self.__result

    # Чтение JSON файла
    def __read_JSON(self, json_file: str, path: str = ""):
        custom_exceptions.type(json_file, str)
        custom_exceptions.type(path, str)

        try:
            full_name = f"{path}{os.sep}{json_file}"
            stream = open(full_name)
            data = json.load(stream)
            return data
        except Exception as ex:
            self.set_exception(ex)
            return None

    def group_from_JSON(self, json_file: str, path: str = ""):
        data_json = self.__read_JSON(json_file, path)
        return self.group(data_json)

    def group(self, data: dict):
        custom_exceptions.type(data, dict)
        self.__result = []
        for i in list(data.keys()):
            self.__result.append(group_model.parse_JSON(data[i]))
        return self.__result

    def nomenclature_from_JSON(self, json_file: str, path: str = ""):
        data_json = self.__read_JSON(json_file, path)
        return self.nomenclature(data_json)

    def nomenclature(self, data: dict):
        custom_exceptions.type(data, dict)
        self.__result = {}
        for i in list(data.keys()):
            value = nomenclature_model.parse_JSON(data[i])
            self.__result[i] = value
        return self.__result

    def range_from_JSON(self, json_file: str, path: str = ""):
        data_json = self.__read_JSON(json_file, path)
        return self.range(data_json)

    def range(self, data: dict):
        custom_exceptions.type(data, dict)
        self.__result = {}
        for i in list(data.keys()):
            value = range_model.parse_JSON(data[i])
            self.__result[value.name] = value
        return self.__result

    def warehouse_from_JSON(self, json_file: str, path: str = ""):
        data_json = self.__read_JSON(json_file, path)
        return self.warehouse(data_json)

    def warehouse(self, data: dict):
        custom_exceptions.type(data, dict)
        self.__result = []
        for i in list(data.keys()):
            self.__result.append(warehouse_model.parse_JSON(data[i]))
        return self.__result

    def transaction_from_JSON(self, json_file: str, path: str = ""):
        data_json = self.__read_JSON(json_file, path)
        return self.transaction(data_json)

    def transaction(self, data: dict):
        custom_exceptions.type(data, dict)
        self.__result = []
        for i in list(data.keys()):
            self.__result.append(warehouse_transaction_model.parse_JSON(data[i]))
        return self.__result

    def receipts_from_JSON(self, json_file: str, path: str = ""):
        data_json = self.__read_JSON(json_file, path)
        return self.receipt(data_json)

    def receipt(self, data: dict):
        custom_exceptions.type(data, dict)
        self.__result = receipt_book_menager.parse_JSON(data)
        return self.__result

    def set_exception(self, ex: Exception):
        super().set_exception(ex)

    def handle_event(self, type: event_type, params):
        super().handle_event(type, params)
