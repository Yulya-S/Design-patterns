from Src.settings_manager import settings_manager

manager1 = settings_manager()
manager1.open("settings.json")
print(f"settings1: {manager1.settings.inn}")