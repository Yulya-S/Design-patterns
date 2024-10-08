from Src.Core.base_models import base_model_name

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
