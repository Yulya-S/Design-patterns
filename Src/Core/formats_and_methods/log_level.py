from enum import Enum

# Форматы расчетов оборотов
class log_level(Enum):
    DEBUG = 1
    INFO = 2
    ERROR = 3

    @staticmethod
    def list():
        result = {}
        for item in log_level:
            result[item.name] = item.value
        return result