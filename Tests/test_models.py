import unittest

from Src.custom_exceptions import custom_exceptions
from Src.settings_manager import settings_manager
from Src.models.range_model import range_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.nomenclature_group_model import nomenclature_group_model
from Src.models.organization_model import organization_model
from Src.models.warehouse_model import warehouse_model

"""
Набор тестов для проверки работы моделей
"""


class test_models(unittest.TestCase):
    # проверка ввода данных (nomenclature_model)
    def test_nomenclature_model_data(self):
        # подготовка
        item1 = nomenclature_model()
        item1.name = "name"
        item2 = nomenclature_model()
        common_nomenclature_group_model = nomenclature_group_model()
        common_range_model = range_model("кг", 1)
        common_range_model.name = "1"
        item1.full_name = "Полное название"
        item1.nomenclature_group = common_nomenclature_group_model
        item1.range = common_range_model
        item2.full_name = "Полное название1"
        item2.nomenclature_group = common_nomenclature_group_model
        item2.range = common_range_model

        # проверки
        assert item1.name == "name"
        assert item1.full_name != item2.full_name
        assert item1.nomenclature_group == item2.nomenclature_group
        assert item1.range == item2.range

    # проверка ошибок при вводе данных (nomenclature_model)
    def test_nomenclature_model_data_fail(self):
        # подготовка
        item = nomenclature_model()

        # проверки
        with self.assertRaises(custom_exceptions):
            item.name = None
        with self.assertRaises(custom_exceptions):
            item.name = "1" * 60
        with self.assertRaises(custom_exceptions):
            item.full_name = None
        with self.assertRaises(custom_exceptions):
            item.full_name = "1" * 260
        with self.assertRaises(custom_exceptions):
            item.nomenclature_group = None
        with self.assertRaises(custom_exceptions):
            item.range = None

    # проверить вариант сравнения (по коду)
    def test_nomenclature_model_comparisons(self):
        # подготовка
        item1 = nomenclature_model()
        item1.name = "test1"
        item2 = nomenclature_model()
        item2.name = "test1"

        # проверки
        assert item1 != item2
        assert item1 != None
        assert item1 == item1
        assert not item1 == None

    # проверить вариант сравнения (по наименованию)
    def test_range_model_comparisons(self):
        # подготовка
        item1 = range_model("кг", 1)
        item1.name = "test1"
        item2 = range_model("кг", 1)
        item2.name = "test2"

        # проверки
        assert item1 != item2
        assert item1 != None
        assert item1 == item1
        assert not item1 == None

    # проверка ввода данных (range_model)
    def test_range_model_data(self):
        # подготовка
        item = range_model("кг", 1)

        # проверки
        assert item.basic_unit_measurement == "кг"
        assert item.conversion_factor == 1

    # проверка ошибок при вводе данных (range_model)
    def test_range_model_data_fail(self):
        # подготовка
        item = range_model("кг", 1)

        # проверки
        with self.assertRaises(custom_exceptions):
            item.basic_unit_measurement = None
        with self.assertRaises(custom_exceptions):
            item.conversion_factor = None

    # проверка ввода данных (organization_model)
    def test_organization_model_data(self):
        # подготовка
        settings = settings_manager().settings
        item = organization_model(settings)

        # проверки
        assert item.inn == settings.inn
        assert item.account == settings.account
        assert item.bic == settings.bic
        assert item.type_ownership == settings.type_ownership

    # проверка ошибок при вводе данных (organization_model)
    def test_organization_model_data_fail(self):
        # проверки
        with self.assertRaises(custom_exceptions):
            item = organization_model(None)
