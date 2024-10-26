from enum import Enum


# Форматы отчетов
class comparison_format(Enum):
    EQUAL = 1
    LIKE = 2
    RANGE = 3

    @staticmethod
    def list():
        result = {}
        for item in comparison_format:
            result[item.name] = item.value
        return result