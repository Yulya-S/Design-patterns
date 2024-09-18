from Src.Core.base_models import base_model_name
from Src.models.dishes.product import product_model
from Src.models.range_model import range_model


# Класс ингредиента
class ingredient_model(base_model_name):
    __product: product_model = None
    __range_model: range_model = None
    __quantity: int = 0

    def __init__(self, product: product_model, range: range_model, quantity: int):
        super().__init__()
        if not isinstance(product, product_model):
            raise self._custom_exception.type(type(product), product)
        if not isinstance(range, range_model):
            raise self._custom_exception.type(type(range), range_model)
        if not isinstance(quantity, int):
            raise self._custom_exception.type(type(quantity), int)
        self.__product = product
        self.__range_model = range
        self.__quantity = quantity

    # Каким продуктом является ингредиент
    @property
    def product(self):
        return self.__product

    # Единица измерения
    @property
    def range_model(self):
        return self.__range_model

    # Необходимое количество ингредиента
    @property
    def quantity(self):
        return self.__quantity
