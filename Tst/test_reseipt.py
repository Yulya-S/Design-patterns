from Src.start_service import start_service
from Src.receipt_book_menager import receipt_book_menager
from Src.settings_manager import settings_manager
from Src.data_reposity import data_reposity
import unittest

"""
Набор тестов для проверки добавления рецептов
"""


class test_reseipt(unittest.TestCase):
    def test_reseipts_append_ingredients(self):
        # Подготовка
        manager = settings_manager()
        manager.open("../settings1.json")
        reposity = data_reposity()
        receipt_book = receipt_book_menager()

        # Действие
        start = start_service(reposity, manager, receipt_book)
        start.create()

        # Проверки
        assert len(reposity.data[data_reposity.receipt_key()]) == 2
        assert "Соль" in list(reposity.data[data_reposity.receipt_key()][0].ingredients.keys())
