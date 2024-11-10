from Src.Core.custom_exceptions import custom_exceptions
from Src.models.nomenclature_model import nomenclature_model
from Src.data_reposity import data_reposity
from Src.data_reposity_menager import data_reposity_menager
from Src.logic.observe_service import observe_service
from Src.Core.event_type import event_type


# обработчик взаимодействий с номенклатурой
class nomenclature_service:
    __reposity: data_reposity = data_reposity()

    # получение данных
    def get(self, name: str):
        custom_exceptions.type(name, str)
        if name in list(self.__reposity.data[data_reposity.nomenclature_key()].keys()):
            return self.__reposity.data[data_reposity.nomenclature_key()][name].__str__()
        return None

    # добавление данных
    def put(self, nomenclature: str):
        custom_exceptions.type(nomenclature, str)
        nomenclature = nomenclature_model.parse_from_str(nomenclature)
        if nomenclature is not None:
            self.__reposity.data[data_reposity.nomenclature_key()][nomenclature.unique_code] = nomenclature
            return True
        return False

    # удаление данных
    def delete(self, nomenclature: str):
        custom_exceptions.type(nomenclature, str)
        nomenclature = nomenclature_model.parse_from_str(nomenclature)
        if nomenclature is not None and data_reposity_menager.can_delete_nomenclature(nomenclature):
            for i in list(self.__reposity.data[data_reposity.nomenclature_key()].keys()):
                if self.__reposity.data[data_reposity.nomenclature_key()][i].unique_code == nomenclature.unique_code:
                    self.__reposity.data[data_reposity.nomenclature_key()].pop(i)
                    return True
        return False

    # изменение данных
    def patch(self, nomenclature: str):
        custom_exceptions.type(nomenclature, str)
        nomenclature = nomenclature_model.parse_from_str(nomenclature)
        observe_service.raise_event(event_type.CHANGE_NOMENCLATURE, nomenclature)
