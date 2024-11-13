from Src.data_reposity import data_reposity
from Src.models.nomenclature_model import nomenclature_model
from Src.Dto.filter import filter_model
from Src.logic.nomenclature_prototype import nomenclature_prototype
from Src.Reports.json_report import json_report
from Src.Json_deserialization import json_deserialization

from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.formats_and_methods.comparison_format import comparison_format

import os
import json


# Обрработчик изменений в репозитории данных
class data_reposity_menager:
    # изменение номенклатуры
    @staticmethod
    def change_nomenclature(object: nomenclature_model):
        custom_exceptions.type(object, nomenclature_model)
        reposity = data_reposity()

        for i in range(len(reposity.data[data_reposity.nomenclature_key()])):
            if object.unique_code == reposity.data[data_reposity.nomenclature_key()][i].unique_code:
                reposity.data[data_reposity.nomenclature_key()][i] = object

        for i in data_reposity.keys():
            if i != data_reposity.nomenclature_key():
                if type(reposity.data[i]) == list:
                    for l in reposity.data[i]:
                        l.change_value_if_equal(object)
                elif type(reposity.data[i]) == dict:
                    for l in list(reposity.data[i].keys()):
                        reposity.data[i][l].change_value_if_equal(object)

    # проверка возможности удаления номенклатуры
    @staticmethod
    def can_delete_nomenclature(object: nomenclature_model) -> bool:
        custom_exceptions.type(object, nomenclature_model)
        reposity = data_reposity()

        filter = filter_model()
        filter.update_filter("unique_code", comparison_format.EQUAL, id)

        for i in data_reposity.keys():
            if i != data_reposity.nomenclature_key():
                data = reposity.data[i]
                prototype = nomenclature_prototype(data)
                result = prototype.create(data, filter, True)
                if len(result.data) > 0:
                    return False
        return True

    # сохранение данных из data_reposity  в json файл
    @staticmethod
    def save(path: str = "", file_name: str = ""):
        custom_exceptions.type(path, str)
        custom_exceptions.type(file_name, str)
        if path == "":
            path = "..\\Datasets"
        if file_name == "":
            file_name = "data.json"
        d = {}
        report = json_report()
        reposity = data_reposity()

        for i in data_reposity().keys():
            d[i] = report.dict_result(reposity.data[i])
        try:
            json_file = open(f"{path}{os.sep}{file_name}", "w")
            json_file.write(json.dumps(d))
            json_file.close()
            return True
        except:
            pass
        return f"{d}"

    @staticmethod
    def load(path: str = "", file_name: str = ""):
        custom_exceptions.type(path, str)
        custom_exceptions.type(file_name, str)
        if path == "":
            path = "..\\Datasets"
        if file_name == "":
            file_name = "data.json"

        data = None
        try:
            full_name = f"{path}{os.sep}{file_name}"
            stream = open(full_name)
            data = json.load(stream)
            stream.close()
        except:
            pass

        deserialization = json_deserialization()
        reposity = data_reposity()
        for i in reposity.keys():
            if i in list(data.keys()):
                reposity.data[i] = deserialization.__getattribute__(i)(data[i])
