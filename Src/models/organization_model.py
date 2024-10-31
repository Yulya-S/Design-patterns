from Src.Core.Abstract_classes.base_models import base_model_name
from Src.settings import settings_model
from Src.Core.custom_exceptions import custom_exceptions


class organization_model(base_model_name):
    __inn: str = ""
    __account: str = ""
    __bic: str = ""
    __type_ownership: str = ""

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

    def __init__(self, data: settings_model):
        super().__init__()
        custom_exceptions.type(data, settings_model)
        self.__inn = data.inn
        self.__bic = data.bic
        self.__account = data.account
        self.__type_ownership = data.type_ownership

    def __str__(self):
        return "organization_model"