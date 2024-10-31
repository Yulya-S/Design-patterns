from enum import Enum
from Src.Core.custom_exceptions import custom_exceptions


# Форматы расчетов оборотов
class turnover_format(Enum):
    SUMM = 1

    @staticmethod
    def list():
        result = {}
        for item in turnover_format:
            result[item.name] = item.value
        return result

    @staticmethod
    def check(format: int) -> bool:
        custom_exceptions.type(format, int)
        for item in turnover_format:
            if item.value == format:
                return True
        return False