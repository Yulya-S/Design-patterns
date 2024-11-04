from Src.start_service import start_service
from Src.settings_manager import settings_manager
from Src.data_reposity import data_reposity
import unittest


# Набор тестов для проверки добавления рецептов
class test_reseipt(unittest.TestCase):
    def test_reseipts_append_ingredients(self):
        # Подготовка
        manager = settings_manager()
        manager.open("", "..")
        reposity = data_reposity()

        # Действие
        start = start_service()
        start.create()

        # Проверки
        assert len(reposity.data[data_reposity.receipt_key()]) == 2
        assert "Соль" in list(reposity.data[data_reposity.receipt_key()][1].ingredients.keys())
