from Src.models.range_model import range_model
from Src.Core.base_models import base_model_code


# Класс книга рецептов
class receipt_book_model(base_model_code):
    __ranges: list = list()
    __recipes: list = list()

    # Получить список рецептов
    @property
    def receipes(self):
        return self.__recipes

    # Добавить единицу измерения
    def add_range(self, basic_unit_measurement_name: str, conversion_factor_value: int):
        self.__ranges.append(range_model(basic_unit_measurement_name, conversion_factor_value))

    # Добавить рецепт
    def add_receipt(self, receipt):
        self.__recipes.append(receipt)

    # поиск единицы измерения в списке
    def get_range_by_name(self, name: str):
        if not isinstance(name, str):
            raise self._custom_exception.type(type(name), str)
        for i in self.__ranges:
            if i.basic_unit_measurement == name:
                return i
        return None
