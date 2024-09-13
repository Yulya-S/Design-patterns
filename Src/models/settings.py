import Src.checks as check

class settings:
    __inn = ""
    __account = ""
    __correspondent_account = ""
    __bic = ""
    __organization_name = ""
    __type_ownership = ""

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        check.type_check(value, str)
        check.value_check(len(value) == 12)
        self.__inn = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        check.type_check(value, str)
        check.value_check(len(value) == 11)
        self.__account = value

    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        check.type_check(value, str)
        check.value_check(len(value) == 11)
        self.__correspondent_account = value

    @property
    def bic(self):
        return self.__bic

    @bic.setter
    def bic(self, value: str):
        check.type_check(value, str)
        check.value_check(len(value) == 9)
        self.__bic = value

    @property
    def organization_name(self):
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        check.type_check(value, str)
        self.__organization_name = value

    @property
    def type_ownership(self):
        return self.__type_ownership

    @type_ownership.setter
    def type_ownership(self, value: str):
        check.type_check(value, str)
        check.value_check(len(value) == 5)
        self.__type_ownership = value