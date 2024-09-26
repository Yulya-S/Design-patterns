from Src.Core.custom_exceptions import custom_exceptions


class settings:
    __inn: str = ""
    __account: str = ""
    __correspondent_account: str = ""
    __bic: str = ""
    __organization_name: str = ""
    __type_ownership: str = ""

    __report_format = None
    _custom_exception: custom_exceptions = custom_exceptions()

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        self._custom_exception.type(value, str)
        self._custom_exception.length_noequal(value, 12)
        self.__inn = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        self._custom_exception.type(value, str)
        self._custom_exception.length_noequal(value, 11)
        self.__account = value

    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        self._custom_exception.type(value, str)
        self._custom_exception.length_noequal(value, 11)
        self.__correspondent_account = value

    @property
    def bic(self):
        return self.__bic

    @bic.setter
    def bic(self, value: str):
        self._custom_exception.type(value, str)
        self._custom_exception.length_noequal(value, 9)
        self.__bic = value

    @property
    def organization_name(self):
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        self._custom_exception.type(value, str)
        self.__organization_name = value

    @property
    def type_ownership(self):
        return self.__type_ownership

    @type_ownership.setter
    def type_ownership(self, value: str):
        self._custom_exception.type(value, str)
        self._custom_exception.length_noequal(value, 5)
        self.__type_ownership = value

    @property
    def report_format(self):
        return self.__report_format

    @report_format.setter
    def report_format(self, value):
        self.__report_format = value
