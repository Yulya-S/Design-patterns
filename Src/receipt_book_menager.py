from Src.Core.abstract_logic import abstract_logic
from Src.models.receipt_book import receipt_book_model
from Src.models.dishes.receipt import receipt_model
from Src.models.dishes.product import product_model

import os
import codecs


# Менеджер книги рецептов
class receipt_book_menager(abstract_logic):
    __path = f".{os.curdir}{os.sep}Docs"
    __receipt_book: receipt_book_model = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(receipt_book_menager, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        if self.__receipt_book is None:
            self.__receipt_book = self.__default_receipt_book
            self.open()

    @property
    def receipt_book(self):
        return self.__receipt_book

    # Прочитать рецепты из директории Docs
    def open(self, path: str = ""):
        if not isinstance(path, str):
            raise self._custom_exception.type(type(path), str)
        if path != "":
            self.__path = path

        try:
            files = os.listdir(self.__path)
            for file in files:
                name = file.split(".")
                if len(name) == 2 and name[1] == "md":
                    with codecs.open(f"{self.__path}{os.sep}{file}", "r", "utf_8_sig") as file:
                        self.__parsing_Markdown(file.read())
        except Exception as ex:
            self.set_exception(ex)
            return False

    # Парсинг фала типа Markdown
    def __parsing_Markdown(self, file: str):
        if not isinstance(file, str):
            raise self._custom_exception.type(type(file), str)
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
        new_receipt.add_steps_cooking(steps)

        # Ингредиенты
        ingredients = file.split("`")[2].split("#")[0].split("|")
        i = 7
        while i < len(ingredients):
            ingredients[i] = ingredients[i].strip()
            ingredients[i + 1] = ingredients[i + 1].strip()
            r = ingredients[i + 1].split(" ")[1]
            r = self.__receipt_book.get_range_by_name(r)
            if r == None:
                raise self._custom_exception.None_received("range")
            new_receipt.add_ingredient(product_model(ingredients[i], r), r, int(ingredients[i + 1].strip(" ")[0]))
            i += 3

        self.__receipt_book.add_receipt(new_receipt)

    # Добавление в книгу рецептов единиц измерения
    @property
    def __default_receipt_book(self) -> receipt_book_model:
        data = receipt_book_model()
        data.add_range("кг", 1)
        data.add_range("гр", 1000)
        data.add_range("шт", 1)
        data.add_range("л", 1)
        data.add_range("мл", 1000)
        return data

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
