from Src.data_reposity import data_reposity
from Src.Dto.filter_JSON_deserialization import filter_json_deserialization
from Src.logic.nomenclature_prototype import nomenclature_prototype
from Src.settings_manager import settings_manager
from Src.start_service import start_service

import unittest


# Набор тестов для фильтрации из Json файла
class test_filters_from_json(unittest.TestCase):
    # Проверить создание фильтра из Json файла
    def test_filter_json_deserialization(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        manager.open("", "..")
        start = start_service()
        start.create()
        filter = filter_json_deserialization()

        value = {
            "name": {
                "comparison_format": 2,
                "value": reposity.data[data_reposity.receipt_key()][0].name[:2]
            }
        }

        # Действие
        filter.read_data(value)
        data = reposity.data[data_reposity.receipt_key()]
        prototype = nomenclature_prototype(data)
        result = prototype.create(data, filter.result)

        # Проверки
        assert len(result.data) == 1
