import unittest
from Src.settings_manager import settings_manager


class test_settings(unittest.TestCase):
    def test_settings_manager_open_fail(self):
        manager = settings_manager()
        manager.open("../settings1.json", "setting")
        assert manager.is_error == True
        manager.error_text = "текст  "
        assert manager.error_text == "текст"

    def test_settings_manager_open(self):
        manager = settings_manager()
        result = manager.open("../settings.json")
        assert result is True

    def test_settings_manager_singletone(self):
        manager1 = settings_manager()
        result = manager1.open("../settings.json")
        manager2 = settings_manager()

        assert manager1 == manager2
        assert manager1.current_settings.inn == manager2.current_settings.inn
        assert manager1.current_settings.account == manager2.current_settings.account
        assert manager1.current_settings.correspondent_account == manager2.current_settings.correspondent_account
        assert manager1.current_settings.bic == manager2.current_settings.bic
        assert manager1.current_settings.organization_name == manager2.current_settings.organization_name
        assert manager1.current_settings.type_ownership == manager2.current_settings.type_ownership

    def test_settings_manager_fail_data(self):
        manager = settings_manager()
        with self.assertRaises(TypeError):
            manager.settings.inn = None
        with self.assertRaises(ValueError):
            manager.settings.inn = "1"
        with self.assertRaises(TypeError):
            manager.settings.account = None
        with self.assertRaises(ValueError):
            manager.settings.account = "1"
        with self.assertRaises(TypeError):
            manager.settings.correspondent_account = None
        with self.assertRaises(ValueError):
            manager.settings.correspondent_account = "1"
        with self.assertRaises(TypeError):
            manager.settings.bic = None
        with self.assertRaises(ValueError):
            manager.settings.bic = "1"
        with self.assertRaises(TypeError):
            manager.settings.organization_name = None
        with self.assertRaises(TypeError):
            manager.settings.type_ownership = None
        with self.assertRaises(ValueError):
            manager.settings.type_ownership = "1"

    def test_setting_manager_get_setting(self):
        manager1 = settings_manager()
        manager2 = settings_manager()
        assert manager1.settings == manager2.settings


if __name__ == '__main__':
    unittest.main()
