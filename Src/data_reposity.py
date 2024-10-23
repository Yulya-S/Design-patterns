from Src.Core.abstract_logic import abstract_logic


# Репозиторий данных
class data_reposity(abstract_logic):
    __data = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(data_reposity, cls).__new__(cls)
        return cls.instance

    # Набор данных
    @property
    def data(self):
        return self.__data

    # Ключи для хранения данных
    @staticmethod
    def group_key() -> str:
        return "group"

    @staticmethod
    def range_key() -> str:
        return "range"

    @staticmethod
    def nomenclature_key() -> str:
        return "nomenclature"

    @staticmethod
    def receipt_key() -> str:
        return "receipt"

    @staticmethod
    def warehouse_key() -> str:
        return "warehouse"

    @staticmethod
    def transaction_key() -> str:
        return "transaction"

    @staticmethod
    def keys():
        return [data_reposity.receipt_key(), data_reposity.nomenclature_key(), data_reposity.group_key(),
                data_reposity.range_key(), data_reposity.warehouse_key(), data_reposity.transaction_key()]

    # Перегрузка абстрактного метода
    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)
