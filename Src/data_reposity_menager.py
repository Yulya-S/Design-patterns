from Src.data_reposity import data_reposity
from Src.models.nomenclature_model import nomenclature_model
from Src.Core.custom_exceptions import custom_exceptions
from Src.Dto.filter import filter_model
from Src.Core.formats_and_methods.comparison_format import comparison_format
from Src.logic.nomenclature_prototype import nomenclature_prototype


# Обрработчик изменений в репозитории данных
class data_reposity_menager:
    # изменение номенклатуры
    @staticmethod
    def change_nomenclature(object: nomenclature_model):
        custom_exceptions.type(object, nomenclature_model)
        reposity = data_reposity()

        for i in range(len(reposity.data[data_reposity.nomenclature_key()])):
            if object.unique_code == reposity.data[data_reposity.nomenclature_key()][i].unique_code:
                reposity.data[data_reposity.nomenclature_key()][i] = object

        for i in data_reposity.keys():
            if i != data_reposity.nomenclature_key():
                if type(reposity.data[i]) == list:
                    for l in reposity.data[i]:
                        l.change_value_if_equal(object)
                elif type(reposity.data[i]) == dict:
                    for l in list(reposity.data[i].keys()):
                        reposity.data[i][l].change_value_if_equal(object)

    # проверка возможности удаления номенклатуры
    @staticmethod
    def can_delete_nomenclature(object: nomenclature_model) -> bool:
        custom_exceptions.type(object, nomenclature_model)
        reposity = data_reposity()

        filter = filter_model()
        filter.update_filter("unique_code", comparison_format.EQUAL, id)

        for i in data_reposity.keys():
            if i != data_reposity.nomenclature_key():
                data = reposity.data[i]
                prototype = nomenclature_prototype(data)
                result = prototype.create(data, filter, True)
                if len(result.data) > 0:
                    return False
        return True
