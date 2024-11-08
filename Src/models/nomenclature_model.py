from Src.Core.Abstract_classes.base_models import base_model_code
from Src.models.group_model import group_model
from Src.models.range_model import range_model
from Src.Core.custom_exceptions import custom_exceptions


# класс номенклатуры
class nomenclature_model(base_model_code):
    __full_name: str = ""
    __group: group_model = None
    __range: range_model = None

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        custom_exceptions.type(value, str)
        custom_exceptions.length_more(value, 255)
        self.__full_name = value

    @property
    def nomenclature_group(self):
        return self.__group

    @nomenclature_group.setter
    def nomenclature_group(self, value: group_model):
        custom_exceptions.type(value, group_model)
        self.__group = value

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value: range_model):
        custom_exceptions.type(value, range_model)
        self.__range = value

    # стандартные значения
    @staticmethod
    def default_source_gr():
        item = nomenclature_model()
        item.range = range_model.default_range_gr()
        item.nomenclature_group = group_model.default_group_source()
        return item

    @staticmethod
    def default_source_ml():
        item = nomenclature_model()
        item.range = range_model.default_range_ml()
        item.nomenclature_group = group_model.default_group_source()
        return item

    @staticmethod
    def default_source_pcs():
        item = nomenclature_model()
        item.range = range_model.default_range_pcs()
        item.nomenclature_group = group_model.default_group_source()
        return item

    def __str__(self):
        return "nomenclature_model"

    # Парсинг JSON файла
    @staticmethod
    def parse_JSON(data: dict):
        custom_exceptions.type(data, dict)

        if len(data) == 0:
            return None

        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(nomenclature_model, x)),
                             dir(nomenclature_model)))

        new_nomenclature = nomenclature_model()

        for field in fields:
            custom_exceptions.presence_element_in_dict(data, field)
            if field == "nomenclature_group":
                data[field] = group_model.parse_JSON(data[field])
            elif field == "range":
                data[field] = range_model.parse_JSON(data[field])
            new_nomenclature.__setattr__(field, data[field])

        return new_nomenclature
