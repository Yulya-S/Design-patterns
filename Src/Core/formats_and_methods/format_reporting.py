from enum import Enum
from Src.Core.custom_exceptions import custom_exceptions


# Форматы отчетов
class format_reporting(Enum):
    CSV = 1
    MARCDOWN = 2
    JSON = 3
    XML = 4
    RTF = 5

    @staticmethod
    def list():
        result = {}
        for item in format_reporting:
            result[item.name] = item.value
        return result

    @staticmethod
    def check(format: int) -> bool:
        custom_exceptions.type(format, int)
        for item in format_reporting:
            if item.value == format:
                return True
        return False
