from Src.models.ingredient import ingredient_model
from Src.models.product import product_model
from Src.models.range_model import range_model
from Src.Core.base_models import base_model_name


# Класс рецепта
class recipe(base_model_name):
    __ingredients: list = list()
    __steps_cooking: list = list()

    # Добавить ингридиент
    def add_ingredient(self, product: product_model, range: range_model, quantity: int):
        self.__ingredients.append(ingredient_model(product, range, quantity))

    # Добавить шаги приготовления
    def add_steps_cooking(self, steps_cooking: list):
        if not isinstance(steps_cooking, list):
            raise self._custom_exception.type(type(steps_cooking), list)
        for step in steps_cooking:
            if not isinstance(step, str):
                raise self._custom_exception.type(type(step), str)
        self.__steps_cooking = steps_cooking
