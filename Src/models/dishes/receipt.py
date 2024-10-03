from Src.models.dishes.ingredient import ingredient_model
from Src.models.nomenclature_model import nomenclature_model
from Src.Core.base_models import base_model_name
from Src.Core.custom_exceptions import custom_exceptions


# Класс рецепта
class receipt_model(base_model_name):
    __ingredients: dict = dict()
    __steps_cooking: list = list()
    __number_servings: int = 0
    __cooking_time: str = ""

    def __init__(self):
        super().__init__()
        self.__ingredients = dict()
        self.__steps_cooking = list()

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value: dict):
        custom_exceptions.type(value, dict)
        self.__ingredients = value

    @property
    def steps_cooking(self):
        return self.__steps_cooking

    @steps_cooking.setter
    def steps_cooking(self, value: list):
        custom_exceptions.type(value, list)
        for step in value:
            custom_exceptions.type(step, str)
        self.__steps_cooking = value

    # Количество порций получающееся по рецепту
    @property
    def number_servings(self):
        return self.__number_servings

    @number_servings.setter
    def number_servings(self, value: int):
        custom_exceptions.type(value, int)
        self.__number_servings = value

    # Время приготовления в минутах
    @property
    def cooking_time(self):
        return self.__cooking_time

    @cooking_time.setter
    def cooking_time(self, value: str):
        custom_exceptions.type(value, str)
        self.__cooking_time = value

    # Добавить ингридиент
    def add_ingredient(self, name: str, nomenclature: nomenclature_model, quantity: int):
        self.__ingredients[name] = ingredient_model(name, nomenclature, quantity)

    def __str__(self):
        return "receipt"

    # Парсинг JSON файла
    @staticmethod
    def parse_JSON(data: dict):
        custom_exceptions.type(data, dict)

        new_receipt = receipt_model()

        new_receipt.name = data["name"]
        new_receipt.unique_code = data["unique_code"]
        new_receipt.steps_cooking = data["steps_cooking"]
        new_receipt.cooking_time = data["cooking_time"]
        new_receipt.number_servings = data["number_servings"]

        ingredients = {}
        for i in list(data["ingredients"].keys()):
            ingredients[i] = ingredient_model.parse_JSON(data["ingredients"][i])
        new_receipt.ingredients = ingredients

        return new_receipt
