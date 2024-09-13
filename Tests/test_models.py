import unittest

from Src.settings_manager import settings_manager
from Src.models.range import range
from Src.models.nomenclature import nomenclature
from Src.models.range_model import range_model
from Src.models.nomenclature_model import nomenclature_model
from Src.models.nomenclature_group_model import nomenclature_group_model
from Src.models.organization_model import organization_model
from Src.models.warehouse_model import warehouse_model


class test_models(unittest.TestCase):
    def test_nomenclature_correct_data(self):
        item = nomenclature()
        item.name = "test1"
        assert item.name == "test1"

    def test_nomenclature_fail_data(self):
        item = nomenclature()
        with self.assertRaises(TypeError):
            item.name = None

    def test_nomenclature_comparisons(self):
        item1 = nomenclature()
        item1.name = "test1"
        item2 = nomenclature()
        item2.name = "test1"

        assert item1 != item2
        assert item1 != None
        assert item1 == item1
        assert not item1 == None

    def test_range_comparisons(self):
        item1 = range()
        item1.name = "test1"
        item2 = range()
        item2.name = "test2"

        assert item1 != item2
        assert item1 != None
        assert item1 == item1
        assert not item1 == None

    def test_range_model_correct_data(self):
        item = range_model("кг", 1)
        assert item.basic_unit_measurement == "кг"
        assert item.conversion_factor == 1

    def test_range_model_fail_data(self):
        item = range_model("кг", 1)
        with self.assertRaises(TypeError):
            item.basic_unit_measurement = None
        with self.assertRaises(TypeError):
            item.conversion_factor = None

    def test_nomenclature_model_correct_data(self):
        item1 = nomenclature_model()
        item1.name = "name"
        assert item1.name == "name"

        item2 = nomenclature_model()
        group = nomenclature_group_model()
        r = range_model("кг", 1)
        item1.full_name = "Полное название"
        item1.nomenclature_group = group
        item1.range = r
        item2.full_name = "Полное название1"
        item2.nomenclature_group = group
        item2.range = r
        assert item1.full_name != item2.full_name
        assert item1.nomenclature_group == item2.nomenclature_group
        assert item1.range == item2.range

    def test_nomenclature_model_fail_data(self):
        item = nomenclature_model()
        with self.assertRaises(TypeError):
            item.name = None
        with self.assertRaises(ValueError):
            item.name = "1" * 60
        with self.assertRaises(TypeError):
            item.full_name = None
        with self.assertRaises(ValueError):
            item.full_name = "1" * 260
        with self.assertRaises(TypeError):
            item.nomenclature_group = None
        with self.assertRaises(TypeError):
            item.range = None

    def test_organization_model_correct_data(self):
        settings = settings_manager().settings
        item = organization_model(settings)
        assert item.inn == settings.inn
        assert item.account == settings.account
        assert item.bic == settings.bic
        assert item.type_ownership == settings.type_ownership

    def test_organization_model_fail_data(self):
        with self.assertRaises(TypeError):
            item = organization_model(None)
