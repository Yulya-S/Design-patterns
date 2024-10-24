from Src.Core.comparison_format import comparison_format
from Src.Core.custom_exceptions import custom_exceptions
from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.models.nomenclature_model import nomenclature_model


class formats:
    __data = {}
    __name: comparison_format = comparison_format.EQUAL
    __id: comparison_format = comparison_format.EQUAL

    def get(self, field: str):
        custom_exceptions.type(field, str)
        if field not in self.__data:
            return comparison_format.EQUAL
        return self.__data[field]

    def set(self, field: str, format: comparison_format = comparison_format.EQUAL):
        custom_exceptions.type(field, str)
        self.__data[field] = format


class filter_model:
    __name: str = ""
    __id: str = ""
    __warehouse: warehouse_model = None
    __nomenclature: nomenclature_model = None
    __formats: formats = None

    def __init__(self):
        self.__formats = formats()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        custom_exceptions.type(value, str)
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        custom_exceptions.type(value, str)
        self.__id = value

    @property
    def warehouse(self):
        return self.__warehouse

    @warehouse.setter
    def warehouse(self, value: warehouse_model):
        custom_exceptions.type(value, warehouse_model)
        self.__warehouse = value

    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        custom_exceptions.type(value, nomenclature_model)
        self.__nomenclature = value

    @property
    def formats(self):
        return self.__formats

    def update_filter(self, field: str, format: comparison_format, value: any):
        custom_exceptions.type(field, str)
        custom_exceptions.type(format, comparison_format)

        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(self.__class__, x)),
                             dir(self)))

        if field not in fields:
            custom_exceptions.other_exception("Введенное поле фильтрации несуществует!")
        self.__setattr__(field, value)
        self.__formats.set(field, format)