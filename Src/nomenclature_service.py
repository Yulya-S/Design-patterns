from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.formats_and_methods.comparison_format import comparison_format
from Src.Dto.filter import filter_model
from Src.logic.nomenclature_prototype import nomenclature_prototype
from Src.models.nomenclature_model import nomenclature_model
from Src.data_reposity import data_reposity


# обработчик взаимодействий с номенклатурой
class nomenclature_service:
    __reposity: data_reposity = data_reposity()

    # проверка что бы при удалении ничего небыло затронуто
    def __check_before_deletion(self, id: str) -> bool:
        custom_exceptions.type(id, str)
        filter = filter_model()
        filter.update_filter("unique_code", comparison_format.EQUAL, id)

        for i in data_reposity.keys():
            if i != data_reposity.nomenclature_key():
                data = self.__reposity.data[i]
                if type(data) == dict:
                    ll = []
                    for l in list(self.__reposity.data[i].keys()):
                        ll.append(self.__reposity.data[i][l])
                    data = ll

                prototype = nomenclature_prototype(data)
                result = prototype.create(data, filter, True)
                if len(result.data) > 0:
                    return False

        return True

    # получение данных
    def get(self, name: str):
        custom_exceptions.type(name, str)
        if name in list(self.__reposity.data[data_reposity.nomenclature_key()].keys()):
            return self.__reposity.data[data_reposity.nomenclature_key()][name]
        return None

    # добавление данных
    def put(self, name: str, groupe_name: str, range_name: str):
        custom_exceptions.type(name, str)
        custom_exceptions.type(groupe_name, str)
        custom_exceptions.type(range_name, str)

        if name in list(self.__reposity.data[data_reposity.nomenclature_key()].keys()):
            return False
        if groupe_name not in [i.name for i in self.__reposity.data[data_reposity.group_key()]]:
            return False
        if range_name not in list(self.__reposity.data[data_reposity.range_key()]):
            return False

        groupe = [i.name for i in self.__reposity.data[data_reposity.group_key()]].index(groupe_name)
        groupe = self.__reposity.data[data_reposity.group_key()][groupe]
        range = self.__reposity.data[data_reposity.range_key()][range_name]

        model = nomenclature_model()
        model.nomenclature_group = groupe
        model.range = range

        self.__reposity.data[data_reposity.nomenclature_key()][name] = model
        return True

    # удаление данных
    def delete(self, name: str):
        custom_exceptions.type(name, str)
        if name not in list(self.__reposity.data[data_reposity.nomenclature_key()].keys()):
            return False
        nomenclature = self.__reposity.data[data_reposity.nomenclature_key()][name]
        if self.__check_before_deletion(nomenclature.unique_code):
            self.__reposity.data[data_reposity.nomenclature_key()].pop(name)
            return True
        return False

    # изменение данных
    def patch(self, name: str, groupe_name: str, range_name: str):
        custom_exceptions.type(name, str)
        custom_exceptions.type(groupe_name, str)
        custom_exceptions.type(range_name, str)

        if name not in list(self.__reposity.data[data_reposity.nomenclature_key()].keys()):
            return False
        if groupe_name not in [i.name for i in self.__reposity.data[data_reposity.group_key()]]:
            return False
        if range_name not in list(self.__reposity.data[data_reposity.range_key()]):
            return False

        nomenclature = self.__reposity.data[data_reposity.nomenclature_key()][name]
        groupe = [i.name for i in self.__reposity.data[data_reposity.group_key()]].index(groupe_name)
        groupe = self.__reposity.data[data_reposity.group_key()][groupe]
        range = self.__reposity.data[data_reposity.range_key()][range_name]

        nomenclature.nomenclature_group = groupe
        nomenclature.range = range

        self.__reposity.data[data_reposity.nomenclature_key()][name] = nomenclature
        return True
