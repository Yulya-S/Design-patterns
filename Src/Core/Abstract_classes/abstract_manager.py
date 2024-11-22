from Src.Core.custom_exceptions import custom_exceptions
from Src.Reports.json_report import json_report
from Src.data_reposity import data_reposity
from Src.Json_deserialization import json_deserialization

from abc import ABC, abstractmethod
import os
import json


# Абстрактный класс менеджера
class abstract_manager(ABC):
    @staticmethod
    @abstractmethod
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
    @abstractmethod
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
