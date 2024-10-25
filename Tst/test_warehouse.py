from Src.settings_manager import settings_manager
from Src.start_service import start_service
from Src.data_reposity import data_reposity

from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.Warehouse.warehouse_turnover_model import warehouse_turnover_model
from Src.models.Warehouse.turnover_factory import turnover_factory

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
        assert len(reposity.data[data_reposity.transaction_key()]) == 7

    def test_turnover_factory(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        manager.open("../settings1.json")
        start = start_service()
        start.create()

        # Действие
        result = turnover_factory.create_turnover(reposity.data[data_reposity.warehouse_key()][0],
                                                  reposity.data[data_reposity.nomenclature_key()]["гр"],
                                                  reposity.data[data_reposity.range_key()]["гр"])

        # Проверки
        assert type(result) == warehouse_turnover_model
        assert result.turnover == 6
