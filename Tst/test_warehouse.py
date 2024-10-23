from Src.settings_manager import settings_manager
from Src.start_service import start_service
from Src.data_reposity import data_reposity

from Src.models.Warehouse.warehouse_model import warehouse_model

import unittest


# Набор тестов для склада
class test_warehouse(unittest.TestCase):
    # Проверить создание транзакции
    def test_warehouse_transaction_generation(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        manager.open("../settings1.json")
        start = start_service()
        start.create()

        # Действие
        start.generate_transaction(
            warehouse_model("1"), reposity.data[data_reposity.nomenclature_key()]["гр"],
            1, False, reposity.data[data_reposity.range_key()]["кг"]
        )

        # Проверки
        assert len(reposity.data[data_reposity.transaction_key()]) == 1
