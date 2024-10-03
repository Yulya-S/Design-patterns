from Src.Core.base_models import base_model_name
from Src.Core.custom_exceptions import custom_exceptions

"""
Модель группы номенклатуры
"""


class group_model(base_model_name):
    """
    Default группа - сырье (фабричный метод)
    """

    @staticmethod
    def default_group_source():
        item = group_model()
        item.name = "Сырье"
        return item

    """
    Default группа - замарозка (фабричный метод)
    """

    @staticmethod
    def default_group_cold():
        item = group_model()
        item.name = "Заморозка"
        return item

    def __str__(self):
        return "group_model"

    # Парсинг JSON файла
    @staticmethod
    def parse_JSON(data: dict):
        custom_exceptions.type(data, dict)

        new_group = group_model()
        new_group.name = data["name"]
        new_group.unique_code = data["unique_code"]

        return new_group
