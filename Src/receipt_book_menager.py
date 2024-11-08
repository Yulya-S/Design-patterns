from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.event_type import event_type

from Src.models.dishes.receipt import receipt_model
from Src.data_reposity import data_reposity

import os
import codecs


# Менеджер книги рецептов
class receipt_book_menager(abstract_logic):
    __path = f".{os.curdir}{os.sep}Docs"

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(receipt_book_menager, cls).__new__(cls)
        return cls.instance

    # Прочитать рецепты из директории Docs
    def open(self, path: str = ""):
        custom_exceptions.type(path, str)
        if path != "":
            self.__path = path

        try:
            reseipts = []
            files = os.listdir(self.__path)
            for file in files:
                name = file.split(".")
                if len(name) == 2 and name[1] == "md":
                    with codecs.open(f"{self.__path}{os.sep}{file}", "r", "utf_8_sig") as file:
                        reseipts.append(self.__parsing_Markdown(file.read()))
            return reseipts
        except Exception as ex:
            self.set_exception(ex)
            return list()

    # Парсинг фала типа Markdown
    def __parsing_Markdown(self, file: str):
        custom_exceptions.type(file, str)
        new_receipt = receipt_model()
        # Название
        new_receipt.name = file.split("#")[1].strip()
        # Количество порций
        new_receipt.number_servings = int(file.split("`")[1].split(" ")[0])
        # Время приготовления
        new_receipt.cooking_time = file.split("`")[-2]

        # Шаги приготовления
        steps = file.split("`")[-1].strip().split("\n")
        for i in range(len(steps)):
            steps[i] = steps[i].strip()
        new_receipt.steps_cooking = steps

        # Ингредиенты
        ingredients = file.split("`")[2].split("#")[0].split("|")
        i = 7
        while i < len(ingredients):
            ingredients[i] = ingredients[i].strip()
            ingredients[i + 1] = ingredients[i + 1].strip()

            data = data_reposity()
            nomenclature = data.data[data_reposity.nomenclature_key()][ingredients[i + 1].split(" ")[1]]
            new_receipt.add_ingredient(ingredients[i], nomenclature, int(ingredients[i + 1].strip(" ")[0]))
            i += 3

        return new_receipt

    # создание рецептов из JSON
    @staticmethod
    def parse_JSON(data: dict):
        custom_exceptions.type(data, dict)
        receipts = []
        for i in list(data.keys()):
            receipts.append(receipt_model.parse_JSON(data[i]))
        return receipts

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)

    def handle_event(self, type: event_type, params):
        super().handle_event(type, params)
