import unittest
from Src.models.range import range
from Src.models.nomenclature import nomenclature


class test_models(unittest.TestCase):
    def test_nomenclature_model(self):
        item1 = nomenclature()
        item1.name = "test1"

        item2 = nomenclature()
        item2.name = "test1"

        assert item1 != item2

    def test_range_model(self):
        item1 = range()
        item1.name = "test1"

        item2 = range()
        item2.name = "test1"

        assert item1 == item2
