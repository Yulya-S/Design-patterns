from Src.Core.base_models import base_model_name
from Src.models.nomenclature_model import nomenclature_model


# Класс ингредиента
class ingredient_model(base_model_name):
    __nomenclature: nomenclature_model = None
    __quantity: int = 0

    def __init__(self, name: str, nomenclature: nomenclature_model, quantity: int):
        super().__init__()
        self._custom_exception.type(name, str)
        self._custom_exception.type(nomenclature, nomenclature_model)
        self._custom_exception.type(quantity, int)
        self.name = name
        self.__nomenclature = nomenclature
        self.__quantity = quantity

    # Единица измерения
    @property
    def range_model(self):
        return self.__nomenclature

    # Необходимое количество ингредиента
    @property
    def quantity(self):
        return self.__quantity
