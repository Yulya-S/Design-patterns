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
        if not isinstance(value, str) or len(value) != 12:
            raise TypeError("Некорректно передан параметр!")
        self.__inn = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        if not isinstance(value, str) or len(value) != 11:
            raise TypeError("Некорректно передан параметр!")
        self.__account = value

    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        if not isinstance(value, str) or len(value) != 11:
            raise TypeError("Некорректно передан параметр!")
        self.__correspondent_account = value

    @property
    def bic(self):
        return self.__bic

    @bic.setter
    def bic(self, value: str):
        if not isinstance(value, str) or len(value) != 9:
            raise TypeError("Некорректно передан параметр!")
        self.__bic = value

    @property
    def organization_name(self):
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Некорректно передан параметр!")
        self.__organization_name = value

    @property
    def type_ownership(self):
        return self.__type_ownership

    @type_ownership.setter
    def type_ownership(self, value: str):
        if not isinstance(value, str) or len(value) != 5:
            raise TypeError("Некорректно передан параметр!")
        self.__type_ownership = value