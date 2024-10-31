from Src.settings_manager import settings_manager
from Src.start_service import start_service
from Src.data_reposity import data_reposity

from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.Warehouse.warehouse_turnover_model import warehouse_turnover_model
from Src.models.Warehouse.turnover_creater import turnover_creater

import unittest
from datetime import datetime, timedelta


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

    # Проверка расчетов оборота
    def test_turnover_factory(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        manager.open("../settings1.json")
        start = start_service()
        start.create()
        creater = turnover_creater()

        # Действие
        result = creater.create_turnover(reposity.data[data_reposity.warehouse_key()][0],
                                         reposity.data[data_reposity.nomenclature_key()]["гр"],
                                         reposity.data[data_reposity.range_key()]["гр"],
                                         [datetime.now() + timedelta(days=-1), datetime.now() + timedelta(days=1)])

        # Проверки
        assert type(result) == warehouse_turnover_model
        assert result.turnover == 6
