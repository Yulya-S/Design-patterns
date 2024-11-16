from Src.data_reposity import data_reposity
from Src.data_reposity_menager import data_reposity_menager
from Src.start_service import start_service

import unittest


class test_reporting(unittest.TestCase):
    # проверка сохранения данных в файл
    def test_data_reposity_menager_save(self):
        # Подготовка
        start = start_service()
        start.create()

        # Действие
        result = data_reposity_menager.save()

        # Проверки
        assert result != ""

    # проверка восстановления данных из файла
    def test_data_reposity_menager_load(self):
        # Подготовка
        reposity = data_reposity()

        # Действие
        data_reposity_menager.load()

        # Проверки
        assert list(reposity.data.keys()) != []
