from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.Core.event_type import event_type


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

    # список существующих в репозитории ключей
    @staticmethod
    def keys():
        return [data_reposity.receipt_key(), data_reposity.nomenclature_key(), data_reposity.group_key(),
                data_reposity.range_key(), data_reposity.warehouse_key(), data_reposity.transaction_key()]

    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)

    def handle_event(self, type: event_type, params):
        super().handle_event(type, params)
