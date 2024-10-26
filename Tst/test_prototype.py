from Src.logic.nomenclature_prototype import nomenclature_prototype
from Src.Dto.filter import filter_model
from Src.data_reposity import data_reposity
from Src.start_service import start_service
from Src.Core.formats_and_methods.comparison_format import comparison_format

import unittest


class test_prototype(unittest.TestCase):
    # тест варианта фильтрации: EQUAL
    def test_prototype_receipt(self):
        # подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        if len(reposity.data[data_reposity.receipt_key()]) == 0:
            raise Exception("Нет данных")

        data = reposity.data[data_reposity.receipt_key()]
        if type(data) == dict:
            dd = list()
            for i in list(data.keys()):
                dd.append(data[i])
            data = dd

        item = data[0]
        item_filter = filter_model()
        item_filter.name = item.name
        prototype = nomenclature_prototype(data)

        # действия
        result = prototype.create(data, item_filter)

        # проверки
        assert len(result.data) == 1
        assert result.data[0] == item

    # тест варианта фильтрации: LIKE
    def test_prototype_nomenclature_comparation_format_like(self):
        # подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        if len(reposity.data[data_reposity.receipt_key()]) == 0:
            raise Exception("Нет данных")

        data = reposity.data[data_reposity.receipt_key()]
        if type(data) == dict:
            dd = list()
            for i in list(data.keys()):
                dd.append(data[i])
            data = dd

        item = data[0]

        item_filter = filter_model()
        item_filter.formats.name = comparison_format.LIKE
        item_filter.name = item.name[:2]
        prototype = nomenclature_prototype(data)

        # действия
        result = prototype.create(data, item_filter)

        # проверки
        assert len(result.data) == 1
        assert result.data[0] == item

    # Тест возможности проверки соответствия значений внутри основного класса
    def test_prototype_nomenclature_comparation_look_inside_is_true(self):
        # подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        if len(reposity.data[data_reposity.receipt_key()]) == 0:
            raise Exception("Нет данных")

        data = reposity.data[data_reposity.receipt_key()]
        if type(data) == dict:
            dd = list()
            for i in list(data.keys()):
                dd.append(data[i])
            data = dd

        item_filter = filter_model()
        item_filter.formats.name = comparison_format.LIKE
        item_filter.name = "щ"  # только в одном рецепте существует ингредиент "Ванилин(щепотка)"
        prototype = nomenclature_prototype(data)

        # действия
        result = prototype.create(data, item_filter, True)

        # проверки
        assert len(result.data) == 1
