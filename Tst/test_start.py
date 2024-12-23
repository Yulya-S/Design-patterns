from Src.settings_manager import settings_manager
from Src.start_service import start_service
import unittest


# Набор тестов для проверки работы старта приложения
class test_start(unittest.TestCase):
    # Проверить создание инстанса start_service
    def test_create_start_service(self):
        # Подготовка
        manager = settings_manager()
        manager.open("", "..")

        # Действие
        start = start_service()

        # Проверки
        assert start is not None

    def test_data_reposity_append_data(self):
        # Подготовка
        manager = settings_manager()
        manager.open("", "..")

        # Действие
        start = start_service()
        start.create()

        # Проверки
        assert start is not None
