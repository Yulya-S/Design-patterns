from Src.abstract_reference import abstract_reference
from Src.models.settings import settings

class organization_model(abstract_reference):
    __inn = ""
    __bic = ""
    __account = ""
    __type_ownership = ""

    def __init__(self, data: settings):
        self.__inn = data.inn
        self.__bic = data.bic
        self.__account = data.account
        self.__type_ownership = data.type_ownership
