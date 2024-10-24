from Src.Core.comparison_format import comparison_format
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.filter_metods import filter_metods


# Формирования прототипов
class prototype_factory:
    __reports = {
        comparison_format.EQUAL: filter_metods.equals,
        comparison_format.LIKE: filter_metods.like,
        comparison_format.RANGE: filter_metods.range
    }

    @staticmethod
    def get(format: comparison_format):
        custom_exceptions.type(format, comparison_format)
        if format not in comparison_format:
            raise Exception("Формат не был определен!")
        return prototype_factory.__reports[format]
