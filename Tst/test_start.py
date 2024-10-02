from Src.settings_manager import settings_manager
from Src.start_service import start_service
from Src.data_reposity import data_reposity
from Src.receipt_book_menager import receipt_book_menager
import unittest

"""
Набор тестов для проверки работы старта приложения
"""


class test_start(unittest.TestCase):
    """
    Проверить создание инстанса start_service
    """

    def test_create_start_service(self):
        # Подготовка
        manager = settings_manager()
        manager.open("../settings1.json")
        reposity = data_reposity()
        receipt_book = receipt_book_menager()

        # Действие
        start = start_service(reposity, manager, receipt_book)

        # Проверки
        assert start is not None

    def test_data_reposity_append_data(self):
        # Подготовка
        manager = settings_manager()
        manager.open("../settings1.json")
        reposity = data_reposity()
        receipt_book = receipt_book_menager()

        # Действие
        start = start_service(reposity, manager, receipt_book)
        start.create()

        # Проверки
        assert start is not None