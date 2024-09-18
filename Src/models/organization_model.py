from Src.Core.base_models import base_model_name
from Src.settings import settings


class organization_model(base_model_name):
    __inn = ""
    __account = ""
    __bic = ""
    __type_ownership = ""

    @property
    def inn(self):
        return self.__inn

    @property
    def account(self):
        return self.__account

    @property
    def bic(self):
        return self.__bic

    @property
    def type_ownership(self):
        return self.__type_ownership

    def __init__(self, data: settings):
        if not isinstance(data, settings):
            raise self.custom_exception.type(type(data), settings)
        self.__inn = data.inn
        self.__bic = data.bic
        self.__account = data.account
        self.__type_ownership = data.type_ownership
