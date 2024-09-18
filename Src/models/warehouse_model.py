from Src.Core.base_models import base_model_name
from Src.models.product import product_model


class warehouse_model(base_model_name):
    __products: list = list()

    # Добавление продукта на склад
    def append(self, product: product_model):
        if not isinstance(product, product_model):
            raise self._custom_exception.type(type(product), product_model)
        if product.name not in self.product_names:
            self.__products.append(product)

    # Получение названий продуктов находящихся на складе
    @property
    def product_names(self):
        l = list()
        for i in self.__products:
            l.append(i.name)
        return l

    # Получить продукт по его названию
    def get_product(self, name: str):
        for i in self.__products:
            if i.name == name:
                return i
        return None
