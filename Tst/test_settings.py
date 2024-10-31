import unittest
from Src.settings_manager import settings_manager
from Src.Core.custom_exceptions import custom_exceptions


# Набор тестов для проверки работы с настройками
class test_settings(unittest.TestCase):
    # проверить открытие и загрузку настроек с ошибкой
    def test_settings_manager_open_fail(self):
        # подготовка
        manager = settings_manager()

        # действие
        manager.open("../settings1.json", "setting")

        # проверки
        assert manager.is_error == True

    # проверить открытие и загрузку настроек
    def test_settings_manager_open(self):
        # подготовка
        manager = settings_manager()

        # действие
        result = manager.open("../settings.json")

        # проверки
        assert result is True

    # проверить работу шаблона singletone
    def test_settings_manager_singletone(self):
        # подготовка
        manager1 = settings_manager()
        manager2 = settings_manager()

        # действие
        result = manager1.open("../settings.json")

        # проверки
        assert manager1 == manager2
        assert manager1.current_settings.inn == manager2.current_settings.inn
        assert manager1.current_settings.account == manager2.current_settings.account
        assert manager1.current_settings.correspondent_account == manager2.current_settings.correspondent_account
        assert manager1.current_settings.bic == manager2.current_settings.bic
        assert manager1.current_settings.organization_name == manager2.current_settings.organization_name
        assert manager1.current_settings.type_ownership == manager2.current_settings.type_ownership

    # проверить введение данных с сошибкой
    def test_settings_manager_singletone_fail(self):
        # подготовка
        manager = settings_manager()

        # проверки
        with self.assertRaises(custom_exceptions):
            manager.settings.inn = None
        with self.assertRaises(custom_exceptions):
            manager.settings.inn = "1"
        with self.assertRaises(custom_exceptions):
            manager.settings.account = None
        with self.assertRaises(custom_exceptions):
            manager.settings.account = "1"
        with self.assertRaises(custom_exceptions):
            manager.settings.correspondent_account = None
        with self.assertRaises(custom_exceptions):
            manager.settings.correspondent_account = "1"
        with self.assertRaises(custom_exceptions):
            manager.settings.bic = None
        with self.assertRaises(custom_exceptions):
            manager.settings.bic = "1"
        with self.assertRaises(custom_exceptions):
            manager.settings.organization_name = None
        with self.assertRaises(custom_exceptions):
            manager.settings.type_ownership = None
        with self.assertRaises(custom_exceptions):
            manager.settings.type_ownership = "1"

    # проверка сравнения настроек
    def test_setting_manager_get_setting(self):
        # подготовка
        manager1 = settings_manager()
        manager2 = settings_manager()

        # проверки
        assert manager1.settings == manager2.settings


if __name__ == '__main__':
    unittest.main()
