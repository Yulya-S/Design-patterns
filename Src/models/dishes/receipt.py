from Src.models.dishes.ingredient import ingredient_model
from Src.models.nomenclature_model import nomenclature_model
from Src.Core.base_models import base_model_name


# Класс рецепта
class receipt_model(base_model_name):
    __ingredients: dict = dict()
    __steps_cooking: list = list()
    __number_servings: int = 0
    __cooking_time: str = ""

    @property
    def ingredients(self):
        return self.__ingredients

    # Количество порций получающееся по рецепту
    @property
    def number_servings(self):
        return self.__number_servings

    @number_servings.setter
    def number_servings(self, value: int):
        if not isinstance(value, int):
            raise self._custom_exception.type(type(value), int)
        self.__number_servings = value

    # Время приготовления в минутах
    @property
    def cooking_time(self):
        return self.__cooking_time

    @cooking_time.setter
    def cooking_time(self, value: str):
        if not isinstance(value, str):
            raise self._custom_exception.type(type(value), str)
        self.__cooking_time = value

    # Добавить ингридиент
    def add_ingredient(self, name: str, nomenclature: nomenclature_model, quantity: int):
        self.__ingredients[name] = ingredient_model(name, nomenclature, quantity)

    # Добавить шаги приготовления
    def add_steps_cooking(self, steps_cooking: list):
        if not isinstance(steps_cooking, list):
            raise self._custom_exception.type(type(steps_cooking), list)
        for step in steps_cooking:
            if not isinstance(step, str):
                raise self._custom_exception.type(type(step), str)
        self.__steps_cooking = steps_cooking
