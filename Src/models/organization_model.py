from Src.abstract_reference import abstract_reference
from Src.models.settings import settings
from Src.checks import type_check

class organization_model(abstract_reference):
    __inn = ""
    __bic = ""
    __account = ""
    __type_ownership = ""

    def __init__(self, data: settings):
        type_check(data, settings)
        self.__inn = data.inn
        self.__bic = data.bic
        self.__account = data.account
        self.__type_ownership = data.type_ownership
