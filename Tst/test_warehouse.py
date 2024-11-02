from Src.settings_manager import settings_manager
from Src.start_service import start_service
from Src.data_reposity import data_reposity

from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.Warehouse.warehouse_turnover_model import warehouse_turnover_model
from Src.models.Warehouse.turnover_creater import turnover_creater

import unittest
from datetime import datetime, timedelta
from time import time
import os


# Набор тестов для склада
class test_warehouse(unittest.TestCase):
    # Проверить создание транзакции
    def test_warehouse_transaction_generation(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        manager.open("", "..")
        start = start_service()
        start.create()

        # Действие
        start.generate_transaction(
            warehouse_model("1"), reposity.data[data_reposity.nomenclature_key()]["гр"],
            1, False, reposity.data[data_reposity.range_key()]["кг"]
        )

        # Проверки
        assert len(reposity.data[data_reposity.transaction_key()]) == 7

    # Проверка создания 1000-и случайных транзакций
    def test_start_service_generate_1000_transaction(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        manager.open("", "..")
        start = start_service()
        start.create()

        # Действие
        start.generate_n_transactions(1000)

        # Проверки
        assert len(reposity.data[data_reposity.transaction_key()]) == 1000

    def test_start_service_create_turnover_with_block_period(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        manager.open("settings.json", "..")
        start = start_service()
        start.create()
        start.generate_n_transactions(1000, datetime.strptime("09-01-2024", "%d-%m-%Y"))
        warehouse = reposity.data[data_reposity.warehouse_key()][0]
        nomenclature = reposity.data[data_reposity.nomenclature_key()]["гр"]
        range = reposity.data[data_reposity.range_key()]["гр"]

        # Действие
        result1 = turnover_creater.create_with_block_period(warehouse, nomenclature, range)
        start.settings.block_period = datetime.strptime("01-01-2022", "%d-%m-%Y")
        result2 = turnover_creater.create_with_block_period(warehouse, nomenclature, range)

        # Проверки
        assert len(result1.data) != len(result2.data)

    # Проверка расчетов оборота
    def test_turnover_factory(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        manager.open("", "..")
        start = start_service()
        start.create()
        creater = turnover_creater()

        # Действие
        result = turnover_creater.create(reposity.data[data_reposity.warehouse_key()][0],
                                         reposity.data[data_reposity.nomenclature_key()]["гр"],
                                         reposity.data[data_reposity.range_key()]["гр"],
                                         [datetime.now() + timedelta(days=-1), datetime.now() + timedelta(days=1)])

        # Проверки
        assert type(result) == warehouse_turnover_model
        assert result.turnover == 6

    def test_start_service_create_turnover_with_block_period_load(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        manager.open("", "..")
        start = start_service()
        start.create()
        warehouse = reposity.data[data_reposity.warehouse_key()][0]
        nomenclature = reposity.data[data_reposity.nomenclature_key()]["гр"]
        range = reposity.data[data_reposity.range_key()]["гр"]

        # Процесс
        with open("../load.md", "w") as file:
            for i in [1000, 2000, 3000, 4000]:
                start.generate_n_transactions(i, datetime.strptime("10-01-2024", "%d-%m-%Y"))
                for l in ["01-01-2024", "01-01-2023", "01-01-2022"]:
                    start_time = time()
                    start.settings.block_period = datetime.strptime(l, "%d-%m-%Y")
                    result = turnover_creater.create_with_block_period(warehouse, nomenclature, range)
                    end_time = time()
                    file.write(f"transaction_count = {i}, block_date = {l}, time={end_time - start_time}\n")
