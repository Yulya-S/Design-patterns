from Src.Core.custom_exceptions import custom_exceptions


class settings:
    __inn: str = ""
    __account: str = ""
    __correspondent_account: str = ""
    __bic: str = ""
    __organization_name: str = ""
    __type_ownership: str = ""

    _custom_exception: custom_exceptions = custom_exceptions()

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str):
            raise self._custom_exception.type(value, str)
        if len(value) != 12:
            raise self._custom_exception.length(len(value), 12, "!=")
        self.__inn = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        if not isinstance(value, str):
            raise self._custom_exception.type(value, str)
        if len(value) != 11:
            raise self._custom_exception.length(len(value), 11, "!=")
        self.__account = value

    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        if not isinstance(value, str):
            raise self._custom_exception.type(value, str)
        if len(value) != 11:
            raise self._custom_exception.length(len(value), 11, "!=")
        self.__correspondent_account = value

    @property
    def bic(self):
        return self.__bic

    @bic.setter
    def bic(self, value: str):
        if not isinstance(value, str):
            raise self._custom_exception.type(value, str)
        if len(value) != 9:
            raise self._custom_exception.length(len(value), 9, "!=")
        self.__bic = value

    @property
    def organization_name(self):
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        if not isinstance(value, str):
            raise self._custom_exception.type(value, str)
        self.__organization_name = value

    @property
    def type_ownership(self):
        return self.__type_ownership

    @type_ownership.setter
    def type_ownership(self, value: str):
        if not isinstance(value, str):
            raise self._custom_exception.type(value, str)
        if len(value) != 5:
            raise self._custom_exception.length(len(value), 5, "!=")
        self.__type_ownership = value
