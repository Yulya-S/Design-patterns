from Src.Core.formats_and_methods.turnover_format import turnover_format
from Src.Core.formats_and_methods.turnover_methods import turnover_methods
from Src.Core.custom_exceptions import custom_exceptions


# Фабрика функций для расчета оборотов
class turnover_factory:
    __methods = {
        turnover_format.SUMM: turnover_methods.summ
    }

    @staticmethod
    def get(format: turnover_format):
        custom_exceptions.type(format, turnover_format)
        if format not in turnover_format:
            raise Exception("Формат не был определен!")
        return turnover_factory.__methods[format]
